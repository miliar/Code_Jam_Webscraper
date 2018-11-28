
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N;

    cin >> N;

    for( int CASE = 1; CASE <= N; CASE++ )
    {
        int NA, NB, turnaround_time;

        cin >> turnaround_time;
        cin >> NA >> NB;

        vector<int> A_departures(NA, 0);
        vector<int> A_arrivals(NA, 0);
        for( int i = 0; i < NA; i++ )
        {
            int hours, minutes;
            char foo;
            cin >> hours >> foo >> minutes;
            A_departures[i] = hours*60+minutes;
            cin >> hours >> foo >> minutes;
            A_arrivals[i] = hours*60+minutes;
        }
        vector<int> B_departures(NB, 0);
        vector<int> B_arrivals(NB, 0);
        for( int i = 0; i < NB; i++ )
        {
            int hours, minutes;
            char foo;
            cin >> hours >> foo >> minutes;
            B_departures[i] = hours*60+minutes;
            cin >> hours >> foo >> minutes;
            B_arrivals[i] = hours*60+minutes;
        }

        int a, b, ca, cb;
        a = b = 0;
        ca = cb = 0;

        vector<int> A_arriving;
        vector<int> B_arriving;
        for( int time = 0; time < 24*60; time++ )
        {
            for( unsigned int j = 0; j < A_arriving.size(); j++ )
            {
                if( A_arriving[j] == time )
                {
                    ca++;
                    A_arriving.erase(A_arriving.begin()+j);
                }
            }
            for( unsigned int j = 0; j < B_arriving.size(); j++ )
            {
                if( B_arriving[j] == time )
                {
                    cb++;
                    B_arriving.erase(B_arriving.begin()+j);
                }
            }

            for( int j = 0; j < NA; j++ )
            {
                if( A_departures[j] == time )
                {
                    if( ca <= 0 )
                    {
                        a++;
                        ca++;
                    }
                    ca--;
                    B_arriving.push_back(A_arrivals[j]+turnaround_time);
                }
            }
            for( int j = 0; j < NB; j++ )
            {
                if( B_departures[j] == time )
                {
                    if( cb <= 0 )
                    {
                        b++;
                        cb++;
                    }
                    cb--;
                    A_arriving.push_back(B_arrivals[j]+turnaround_time);
                }
            }
        }

        cout << "Case #" << CASE << ": " << a << " " << b << endl;
    }

    return 0;
}


