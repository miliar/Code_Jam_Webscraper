// Problem B: Train Timetable
// Problem's source: Google Code Jam, Qualification Round
// Program by Plamen Petrov (C) 2008
// e-mail: digphys@gmail.com

#include <cstdio>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
using namespace std;

#define ALL(x) x.begin(),x.end()

typedef list<int> LI; 
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector <PIII> VIII;

//converts time string HH:MM into minutes since 00:00
inline int minutes(char time[6])
{
    time[2]=0; //devide string 
    return 60*atoi(time) + atoi(&time[3]);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    const int A=0, B=1; 
    
    int i, test, min_dep, min_arr, min_ab, min_avail_dep, N, NA, NB, T, trains[2];
    VIII time; // <departure_time, <arrival_time, station_number>>
    LI avail[2]; //lists of available trains
    LI::iterator it;
    char dep_time[6], arr_time[6];
    
    //input
    scanf("%d", &N);
    for(test=1; test<=N; test++)
    {
        scanf("%d%d%d", &T, &NA, &NB);
        
        //clear departure & arrival vectors
        time.clear();
        
        //read NA trips
        for(i=0; i<NA; i++) 
        {
            scanf("%s%s", dep_time, arr_time);
            time.push_back(PIII(minutes(dep_time), PII(minutes(arr_time), A)));
        }
        
        //read NB trips
        for(i=0; i<NB; i++) 
        {
            scanf("%s%s", dep_time, arr_time);
            time.push_back(PIII(minutes(dep_time), PII(minutes(arr_time), B)));
        }
        
        //clear lits of available trains at A and B
        avail[A].clear();
        avail[B].clear();
        
        //clear number of trains
        trains[A]=trains[B]=0;
        
        //sort departure times
        sort(ALL(time));
        
        for(i=0; i<time.size(); i++)
        {
            min_dep=time[i].first; //min departure time
            min_arr=(time[i].second).first; //arrival time of min departure trip
            min_ab=(time[i].second).second; //station number (0 or 1) of min departure trip
            
            it=min_element(ALL(avail[min_ab]));
            min_avail_dep=*it;
            
            if(min_avail_dep>min_dep) 
            {
                //add new (available) train
                trains[min_ab]++;
            }
            else
            {
                //use old (available) train
                avail[min_ab].erase(it); //erase used train from list min_ab
            }
            
            avail[1-min_ab].push_back(min_arr+T); //add new train to the other list
        }

        printf("Case #%d: %d %d\n", test, trains[A], trains[B]);
    }

    return 0;
}
