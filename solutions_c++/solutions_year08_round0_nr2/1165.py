#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int process_time(int hour,int minute)
{
    return hour*60 + minute;
}

int main()
{
    unsigned int n_test;                                        
    ifstream input;
    input.open("B-small.in");
    input>>n_test;
    ofstream output;
    output.open("b-out");
    for (int i=0;i<n_test;i++)
    {
        vector<int> A_departure,A_arrival,B_departure,B_arrival;
        int turntime,NA,NB;
        input>>turntime>>NA>>NB;
        unsigned int a_ready=0,a_total=0,b_ready=0,b_total=0;

        for(int ia=0;ia<NA;ia++)
        {
            char clear;
            int hr,min;
            input>>hr>>clear>>min;
            A_departure.push_back(process_time(hr,min));
            input>>hr>>clear>>min;
            B_arrival.push_back(process_time(hr,min)+turntime);
        }

        for(int ib=0;ib<NB;ib++)
        {
            char clear;
            int hr,min;
            input>>hr>>clear>>min;
            B_departure.push_back(process_time(hr,min));
            input>>hr>>clear>>min;
            A_arrival.push_back(process_time(hr,min)+turntime);
        }

        sort(A_departure.begin(),A_departure.end());
        sort(B_departure.begin(),B_departure.end());
        sort(A_arrival.begin(),A_arrival.end());
        sort(B_arrival.begin(),B_arrival.end());

        vector<int> merge_dep;
        vector<char> station;
        vector<int>::iterator iter_A=A_departure.begin(),iter_B=B_departure.begin();
        
        while( (iter_A!=A_departure.end()) && (iter_B!=B_departure.end()) )
        {
            if (*iter_A<=*iter_B)
            {
                merge_dep.push_back(*iter_A);
                station.push_back('A');
                ++iter_A;
            }
            else
            {
                merge_dep.push_back(*iter_B);
                station.push_back('B');
                ++iter_B;
            }
        }

        while( iter_A!=A_departure.end() )
        {
            merge_dep.push_back(*iter_A);
            station.push_back('A');
            ++iter_A;

        }

        while( iter_B!=B_departure.end() )
        {
            merge_dep.push_back(*iter_B);
            station.push_back('B');
            ++iter_B;

        }

        iter_A=A_arrival.begin();
        iter_B=B_arrival.begin();
        vector<int>::iterator iter_M=merge_dep.begin();
        vector<char>::iterator iter_S=station.begin();
        
        
        while(iter_M!=merge_dep.end())
        {
            if(*iter_S=='A')
            {
                while(iter_A!=A_arrival.end())
                {
                    if(*iter_A<=*iter_M)
                    {
                        a_ready++;
                        iter_A++;
                    }
                    else
                        break;
                }

                if(a_ready>0)
                {
                    iter_M++;
                    iter_S++;
                    a_ready--;
                }
                else
                {
                    iter_M++;
                    iter_S++;
                    a_total++;
                }
            }
            else
            {
                while(iter_B!=B_arrival.end())
                {
                    if(*iter_B<=*iter_M)
                    {
                        b_ready++;
                        iter_B++;
                    }
                    else
                        break;
                }

                if(b_ready>0)
                {
                    iter_M++;
                    iter_S++;
                    b_ready--;
                }
                else
                {
                    iter_M++;
                    iter_S++;
                    b_total++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<a_total<<" "<<b_total<<endl; 
        output<<"Case #"<<i+1<<": "<<a_total<<" "<<b_total<<endl; 
        
    }
    input.close();
    output.close();
    return 0;
}















