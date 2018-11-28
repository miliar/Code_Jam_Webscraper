#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int table[31];

int main()
{
    for (int i=0; i<=8; i++)
    {
        int j=i+2;
        for(int k=i; k<=j; k++)
            table[i+j+k] = 1;
    }

    ofstream output;
    ifstream input("B-large.in");
    output.open("B-large.out");

    int t;
    input >> t;
    for(int case_n = 0; case_n <t; case_n ++)
    {
        output<<"Case #"<<case_n+1<<": ";
        int n,s,p;
        input >>n>>s>>p;
        vector<int> v(n);
        vector<int> vv(n);
        for(int i=0; i<n; i++)
        {
            input >> v[i];
        }

        for(int i=0; i<n; i++)
        {
            int ret = 0;
            if(table[v[i]])
            {
                if (v[i] % 3 == 0)
                {
                    if ( (v[i]+3)/3 >= p )
                        ret ++;
                }
                else if (v[i] %3 == 1)
                {
                    if ((v[i]+2)/3 >=p)
                        ret ++;
                }
                else
                {
                    if ((v[i]+4)/3 >= p)
                        ret++;
                }
                if (ret) 
                {
                    vv[i] += 2;
                }
            }
            
            ret = 0;
            if (v[i] % 3 == 0)
            {
                if (v[i]/3 >= p)
                    ret ++;
            }
            else if (v[i] % 3 == 1)
            {
                if ((v[i]+2)/3 >= p)
                    ret ++;
            }
            else
            {
                if((v[i]+1)/3 >= p)
                    ret ++;
            }
            if (ret)
            {
                vv[i] += 1;
            }
        }
        
        int value = 0; 
        vector<int> count(5);
        for (int i=0; i<v.size(); i++)
        {
            count[vv[i]] ++;
        }

        for (int i=0; i<v.size(); i++)
        {
            if (vv[i] == 0 && table[v[i]] )
                count[4] ++;
        }
        
        if (count[2] >= s)
            value = count[1]+count[3]+s;
        else if ( count[2] + count[3] >= s)
            value = count[1]+count[2]+count[3];
        else  
        {
            int ss = s-count[2]-count[3];
            if (ss > count[4])
            {
                value = count[2]+count[3]+count[1]-(ss-count[4]);
            }
            else
            {
                value = count[1]+count[2]+count[3];
            }
        }
        output << value <<endl;
    }
}
            



            




