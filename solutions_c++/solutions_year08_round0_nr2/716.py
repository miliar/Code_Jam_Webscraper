#pragma warning (disable:4786)
#include <iostream>
#include <string>
#include <fstream> 
#include <algorithm>


using namespace std;

#define eage 100

#define string2minutes(str_time)  ( ( (str_time[0]-'0')*10 + (str_time[1]-'0') )*60 +(str_time[3]-'0')*10 + (str_time[4]-'0') )


int less_train(int turnaround_time, int *arrive_time, int N_arrive, int *departure_time, int N_departure)
{
    int lesstrain = N_departure;
    int p = 0;
    for (int i = 0; i < N_arrive; i++)
    {
        while (p < N_departure)
        {
            if (arrive_time[i] + turnaround_time <= departure_time[p++])
            {
                --lesstrain;
                break;
            }
        }
        if (p == N_departure)
            break;
    }
    return lesstrain;
}

int main(int argc, char *argv[])
{
    ifstream cin("B-large.in"); 
    ofstream cout("B-large.out");

    int N = 0;
    cin >> N;
    int casei = 1;

    while (N-- > 0)
    {
        int i;
        int T, NA, NB;
        cin >> T >> NA >> NB;
        string str_time;

        int A_departure_t[eage];
        int A_arrive_t[eage];
        int B_departure_t[eage];
        int B_arrive_t[eage];

        for (i = 0; i < NA; i++)
        {
            // start time
            cin >> str_time;
            int minutes = string2minutes(str_time);
            A_departure_t[i] = minutes;

            // end time
            cin >> str_time;
            minutes = string2minutes(str_time);
            A_arrive_t[i] = minutes;
        }

        for (i = 0; i < NB; i++)
        {
            // start time
            cin >> str_time;
            int minutes = string2minutes(str_time);
            B_departure_t[i] = minutes;

            // end time
            cin >> str_time;
            minutes = string2minutes(str_time);
            B_arrive_t[i] = minutes;
        }

        // sort
        sort(A_departure_t, A_departure_t + NA);
        sort(A_arrive_t, A_arrive_t + NA);
        sort(B_departure_t, B_departure_t + NB);
        sort(B_arrive_t, B_arrive_t + NB);

        // the max number of trains that must start at A is  NA
        int retA = less_train(T, B_arrive_t, NB, A_departure_t, NA);

        // calcuate the max number of trains that must start at B
        int retB = less_train(T, A_arrive_t, NA, B_departure_t, NB);

        cout << "Case #"<< casei++ << ": " << retA << " " << retB << endl;
    }
    return 0;
}
