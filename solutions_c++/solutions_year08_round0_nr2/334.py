// 
// File:   egg_drop.cpp
// Author: rsalmeidafl
//
// Created on 26 de Junho de 2008, 22:52
//

#include <iostream>
#include <list>

using namespace std;

enum EDirection {
    ETowardsA = 0,
    ETowardsB = 1
};

char sDirection[] = {'A','B'};

class Trip {
public:
    int         starts;
    int         ends;
    EDirection  direction;
    
    bool operator < (const Trip& other);
    
    int         from() const;
    int         to() const;
};

EDirection default_direction = ETowardsB;

typedef std::list<Trip> CTripList;

bool Trip::operator < (const Trip& other) {
    if (starts < other.starts)
        return true;
    else 
        return (starts == other.starts && ends < other.ends);
}

int Trip::from() const {
    return (this->direction == ETowardsA) ? 1 : 0;
}

int Trip::to() const {
    return (int)this->direction;
}


istream& operator >> (istream& input, Trip& output) {
    int hr[2], min[2];
    char c;
    
    input >> hr[0] >> c >> min[0] >> hr[1] >> c >> min[1];
    
    output.direction = default_direction;
    output.starts = 60*hr[0] + min[0];
    output.ends = 60*hr[1] + min[1];
    
    return input;
}

int main(int argc, char** argv) {
    
    int num_of_instances;
    int current_instance = 0;
    
    scanf("%d", &num_of_instances);
    
    while (current_instance++ < num_of_instances) {
        int turnaround_time;
        int trains_at[2]= {0, 0};
        int trains_starting_at[2] = {0, 0};
        int trips_starting_from[2];
        
        CTripList   trip_list;
        CTripList   ongoing_trips;

        /* Reading */
        cin >> turnaround_time >> trips_starting_from[0] >> trips_starting_from[1];
        
        Trip iterTrip;
        default_direction = ETowardsB;
        while (trips_starting_from[0]--) {
            cin >> iterTrip;
            trip_list.push_back(iterTrip);
        }
        
        default_direction = ETowardsA;
        while (trips_starting_from[1]--) {
            cin >> iterTrip;
            trip_list.push_back(iterTrip);
        }
        trip_list.sort();
        
        /* Computing */
        while (!trip_list.empty()) {
            /* Next trip time */
            Trip next_trip = trip_list.front();            
            
            /* Check for released trains */
            int cur_release_time = next_trip.starts - turnaround_time;
            CTripList::iterator iter = ongoing_trips.begin();
            
            while (iter != ongoing_trips.end()) {              
                if (iter->ends <= cur_release_time) {
                    ++trains_at[iter->to()];
                    iter = ongoing_trips.erase(iter);
//                    cout << "Train departed from " << sDirection[iter->from()] << " at " << iter->starts << " got at " << sDirection[iter->to()] << " at " << iter->ends << " and is now ready to use\n";
//                    cout << "Balance: " << trains_at[0] << " trains in A, " << trains_at[1] << " trains in B.\n\n";
                }
                else
                    ++iter;
            }
            
            /* Check if we have enough trains */
            if (!trains_at[next_trip.from()]) {
                ++trains_at[next_trip.from()];
                ++trains_starting_at[next_trip.from()];
//                cout << "No train available at " << sDirection[next_trip.from()] << ", allocating new one\n";
//                cout << "Balance: " << trains_at[0] << " trains in A, " << trains_at[1] << " trains in B.\n\n";
            }
            --trains_at[next_trip.from()];
                       
            /* Mark current trip as ongoing */
//            cout << "Trip departing from " << (char)('A' + next_trip.from()) << " at " << next_trip.starts << '\n';            
//            cout << "Balance: " << trains_at[0] << " trains in A, " << trains_at[1] << " trains in B.\n\n";           
            
            trip_list.pop_front();
            ongoing_trips.push_back(next_trip);
        }
        
        /* Output */
        cout << "Case #" << current_instance << ": " << trains_starting_at[0] << ' ' << trains_starting_at[1] << '\n';
    }    
    
    return (EXIT_SUCCESS);
}

