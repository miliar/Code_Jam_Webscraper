// TrainTimetable.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include "math.h"
using namespace std;

typedef struct {
    int time;
    bool arrival; 
} Time;

struct Comparator
{
     bool operator()(Time& t0, Time& t1)
     {
         if (t0.time != t1.time) return (t0.time < t1.time); 
         if (t0.arrival && !t1.arrival) return true;
         if (!t0.arrival && t1.arrival) return false;
         return true;
     }
};

int _tmain(int argc, _TCHAR* argv[])
{
    int num_cases;
    ifstream input_file; 
    int turn_around_time;
    int num_A_to_B_trips;
    int num_B_to_A_trips;
    vector<Time> departures_and_arrivals_at_A;
    vector<Time> departures_and_arrivals_at_B;
    int hour, minutes; 
    Time time;
    char colon;
    int num_trains_at_A = 0;
    int num_trains_at_B = 0;
    int num_trains_currently_at_A = 0;
    int num_trains_currently_at_B = 0;
    int current_time = 0;
    int num_total_trips = 0;

    if (argc < 2) return 1;

    input_file.open(argv[1]);
    if (!input_file.good()) return 1;

    input_file >> num_cases;
    //cout << num_cases << endl;

    for (int i = 0; i < num_cases; i++) {
        input_file >> turn_around_time;
        //cout << turn_around_time << endl;

        input_file >> num_A_to_B_trips >> num_B_to_A_trips;
        //cout << num_A_to_B_trips << " " << num_B_to_A_trips << endl;

        for (int j = 0; j < num_A_to_B_trips; j++) {
            input_file >> hour >> colon >> minutes;
            time.time = hour*60 + minutes;
            time.arrival = false; 
            departures_and_arrivals_at_A.push_back(time);
            //cout << hour << colon << minutes << " "; 
            //cout << time.time << " " << time.arrival << "; ";

            input_file >> hour >> colon >> minutes;
            time.time = hour*60 + minutes + turn_around_time;
            time.arrival = true; 
            departures_and_arrivals_at_B.push_back(time);
            //cout << hour << colon << minutes << " "; 
            //cout << time.time << " " << time.arrival << endl;
        }

        for (int j = 0; j < num_B_to_A_trips; j++) {
            input_file >> hour >> colon >> minutes;
            time.time = hour*60 + minutes; 
            time.arrival = false; 
            departures_and_arrivals_at_B.push_back(time);
            //cout << hour << colon << minutes << " ";
            //cout << time.time << " " << time.arrival << "; ";

            input_file >> hour >> colon >> minutes;
            time.time = hour*60 + minutes + turn_around_time; 
            time.arrival = true; 
            departures_and_arrivals_at_A.push_back(time);
            //cout << hour << colon << minutes << " ";
            //cout << time.time << " " << time.arrival << endl;
        }

        //sort vectors
        sort(departures_and_arrivals_at_A.begin(), departures_and_arrivals_at_A.end(), Comparator());
        sort(departures_and_arrivals_at_B.begin(), departures_and_arrivals_at_B.end(), Comparator());
        
        num_trains_at_A = 0;
        num_trains_at_B = 0;
        num_trains_currently_at_A = 0;
        num_trains_currently_at_B = 0;
        num_total_trips = num_A_to_B_trips+num_B_to_A_trips;

        /*
        cout << endl;
        for (int j = 0; j < num_total_trips; j++) {
            cout << departures_and_arrivals_at_A[j].time << " " << departures_and_arrivals_at_A[j].arrival << endl;
        }
        cout << endl;
        for (int j = 0; j < num_total_trips; j++) {
            cout << departures_and_arrivals_at_B[j].time << " " << departures_and_arrivals_at_B[j].arrival << endl;
        }
        cout << endl;
        */

        for (int j = 0; j < num_total_trips; j++) {
            //arrival
            if (departures_and_arrivals_at_A[j].arrival) { 
                num_trains_currently_at_A++;
                //cout << "arrival!     ";
            } else { //departure
                if (num_trains_currently_at_A > 0) {
                    num_trains_currently_at_A--;
                } else {
                    num_trains_at_A++;
                }
                
                //cout << "departure! ";
            }
            current_time = departures_and_arrivals_at_A[j].time;
            //cout << "current_time " << current_time;
            //cout << " " << num_trains_at_A << " " << num_trains_currently_at_A << endl;
        }
        //cout << endl;

        for (int j = 0; j < num_total_trips; j++) {
            //arrival
            if (departures_and_arrivals_at_B[j].arrival) { 
                num_trains_currently_at_B++;
                //cout << "arrival!     ";
            } else { //departure
                if (num_trains_currently_at_B > 0) {
                    num_trains_currently_at_B--;
                } else {
                    num_trains_at_B++;
                }
                current_time = departures_and_arrivals_at_B[j].time;
                //cout << "departure! ";
            }
            current_time = departures_and_arrivals_at_B[j].time;
            //cout << "current_time " << current_time;
            //cout << " " << num_trains_at_B << " " << num_trains_currently_at_B << endl;
        }
        //cout << endl;

        cout << "Case #" << i+1 << ": " << num_trains_at_A << " " << num_trains_at_B << endl;

        /*
        cout << "\nchecking answer! \n";

        num_trains_currently_at_A = num_trains_at_A;
        num_trains_currently_at_B = num_trains_at_B;

        for (int j = 0; j < num_total_trips; j++) {
            //arrival
            if (departures_and_arrivals_at_A[j].arrival) { 
                num_trains_currently_at_A++;
                cout << "arrival!     ";
            } else { //departure
                num_trains_currently_at_A--;
                cout << "departure! ";
            }
            current_time = departures_and_arrivals_at_A[j].time;
            cout << "current_time " << current_time;
            cout << " " << num_trains_currently_at_A << endl;
        }
        cout << endl;

        for (int j = 0; j < num_total_trips; j++) {
            //arrival
            if (departures_and_arrivals_at_B[j].arrival) { 
                num_trains_currently_at_B++;
                cout << "arrival!     ";
            } else { //departure
                num_trains_currently_at_B--;
                cout << "departure! ";
            }
            current_time = departures_and_arrivals_at_B[j].time;
            cout << "current_time " << current_time;
            cout << " " << num_trains_currently_at_B << endl;
        }
        cout << endl;

        cout << "total starting trains: " << num_trains_at_A+num_trains_at_B << endl;
        cout << "total ending trains: " << num_trains_currently_at_A+num_trains_currently_at_B << endl;
        if ((num_trains_at_A+num_trains_at_B) != (num_trains_currently_at_A+num_trains_currently_at_B)) cout << "ERROR!\n";

        cout << "++++++++++++++++++++++++++++++++++++++++++++" << endl << endl;
        */

        departures_and_arrivals_at_A.clear();
        departures_and_arrivals_at_B.clear();
    }

	return 0;
}

