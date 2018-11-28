#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <string>
struct TrainEvent
{
    int t;
    int StartEnd; //0=start, 1=end
    int AB; //0=A, 1=B
};

bool CompareTrainEvent(struct TrainEvent a, struct TrainEvent b)
{
    return ( a.t < b.t ) || ( ( a.t==b.t ) && ( a.StartEnd > b.StartEnd ) );
}

int main()
{
    unsigned N, T, NA, NB;
    int i, j, k;
    char time[6];
    int minutes;
    std::vector<struct TrainEvent> eventList;
    struct TrainEvent trainEvent;
    std::vector<struct TrainEvent>::iterator it;
    int usageA, usageB, maxA, maxB;
    
    std::cin >> N;
    for ( i=0; i<N; ++i )
    {
        std::cin >> T >> NA >> NB;
        std::vector<struct TrainEvent>().swap(eventList);
        
        //read A trains
        for ( j=0; j<NA; ++j )
        {
            std::cin >> time;
            minutes = ( (time[0]-'0')*10 + (time[1]-'0') ) * 60 
                         + (time[3]-'0')*10 + time[4]-'0';
//            std::cout << minutes << std::endl;
            trainEvent.t = minutes;
            trainEvent.StartEnd = 0;
            trainEvent.AB = 0;
            eventList.push_back(trainEvent);

            std::cin >> time;
            minutes = ( (time[0]-'0')*10 + (time[1]-'0') ) * 60 
                         + (time[3]-'0')*10 + time[4]-'0';
//            std::cout << minutes << std::endl;
            trainEvent.t = minutes + T;
            trainEvent.StartEnd = 1;
            trainEvent.AB = 0;
            eventList.push_back(trainEvent);

        }
        //read B trains
        for ( j=0; j<NB; ++j )
        {
            std::cin >> time;
            minutes = ( (time[0]-'0')*10 + (time[1]-'0') ) * 60 
                         + (time[3]-'0')*10 + time[4]-'0';
//            std::cout << minutes << std::endl;
            trainEvent.t = minutes;
            trainEvent.StartEnd = 0;
            trainEvent.AB = 1;
            eventList.push_back(trainEvent);

            std::cin >> time;
            minutes = ( (time[0]-'0')*10 + (time[1]-'0') ) * 60 
                         + (time[3]-'0')*10 + time[4]-'0';
//            std::cout << minutes << std::endl;
            trainEvent.t = minutes + T;
            trainEvent.StartEnd = 1;
            trainEvent.AB = 1;
            eventList.push_back(trainEvent);
        }
        
        sort ( eventList.begin(), eventList.end(), CompareTrainEvent);
        
        //run events
        usageA=usageB=0;
        maxA = maxB = 0;
        for ( it=eventList.begin(); it<eventList.end(); it++ )
        {
            /* std::cout << "at time " << it->t << "  Train from "
                  << ( (it->AB)?"B":"A" ) 
                  << ( (it->StartEnd)?" arrive":" depart" )
                  << std::endl; */
                  
            if ( it->AB )
            {
                if ( it->StartEnd )
                {
                    //train from B, arrival
                    usageA--;
                }else
                {
                    //train from B, departure
                    usageB++;
                    if( maxB<usageB ) maxB=usageB;
                }
            }else
            {
                if ( it->StartEnd )
                {
                    //train from A, arrival
                    usageB--;
                }else
                {
                    //train from A, departure
                    usageA++;
                    if( maxA<usageA ) maxA=usageA;
                }
            }
        }
            
        //output
        std::cout << "Case #" << i+1 << ": "
                    << maxA << " " << maxB << std::endl;
    }
    
    return 0;
}
