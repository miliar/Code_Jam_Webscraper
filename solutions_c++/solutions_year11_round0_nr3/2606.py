#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main()
{
    //ifstream input ("C-small-attempt0.in");
    ifstream input ("C-large.in");
    //ofstream output ("C-small.out");
    ofstream output ("C-large.out");

    int t;

    input >> t;

    for (int i=0; i<t; i++)
    {
        list<int> l;
        int n;
        input >> n;
        for (int j=0; j<n; j++)
        {
            int temp;
            input >> temp;
            l.push_back(temp);
        }
        output <<"Case #"<<i+1<<": ";
        list<int>::iterator it;
        int result = 0;
        for(it=l.begin(); it != l.end(); it++)
        {
            result ^= *it;
        }

        if (result)
        {
            output <<"NO"<<endl;
            continue;
        }
        
        l.sort();
        l.pop_front();
        result = 0;
        for(it = l.begin(); it != l.end(); it++)
        {
            result += *it;
        }

        output << result<<endl;
    }
    return 0;
}



        

        

