#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<bitset>

using namespace std;

int main()
{
    unsigned int n_test;
    ifstream input;
    input.open("A-small.in");
    input>>n_test;
    ofstream output;
    output.open("a-out");
    for(int i=0;i<n_test;i++)
    {
        unsigned int min_switches=0,S,Q;
        vector<string> engine_list,query_list;
        vector<int> engine_code,query_code;
        string clear;
        
        input>>S;
        getline(input,clear);

        for(int is=0;is<S;is++)
        {
            string temp;
            getline(input,temp);
            engine_list.push_back(temp);
            engine_code.push_back(is);
        }

        input>>Q;
        getline(input,clear);

        for(int iq=0;iq<Q;iq++)
        {
            string temp;
            getline(input,temp);
            query_list.push_back(temp);
        }

        for(int iq=0;iq<Q;iq++)
        {
            for(int is=0;is<S;is++)
            {
                if(query_list[iq]==engine_list[is])
                {
                    query_code.push_back(is);
                    break;
                }
            }
        }
        
        
        vector<int>::iterator iter_Q=query_code.begin();
        bitset<101> test,full;
        test.reset();
        full.reset();
        
        for(int is=0;is<S;is++)
            full.set(is);

        while(iter_Q!=query_code.end())
        {
            test.set(*iter_Q);
            if(test==full)
            {
                test.reset();
                min_switches++;

            }
            else
            {
                iter_Q++;
            }
        }

        cout<<"Case #"<<i+1<<": "<<min_switches<<endl; 
        output<<"Case #"<<i+1<<": "<<min_switches<<endl; 
    }
    input.close();
    output.close();
    return 0;

}

