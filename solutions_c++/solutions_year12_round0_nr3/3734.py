#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<set>

using namespace std;

int main()
{
    int t;
    unsigned int A,B;
    unsigned int n,m;
    unsigned int count;
    set<unsigned int>s;
    cin>>t;

    for(int k=1;k<=t;k++)
    {   count = 0;
        cin>>A>>B;
        char str[10];

        //int prev_m = 0;
        for(int n=A;n<=B;n++)
        {
            //prev_m = 0;
            sprintf(str,"%d",n);
            int len = strlen(str);

            //cout<<len<<endl;
            for(int i=1;i<len;i++)
            {
                m = (n%(int)pow(10,i))*(int)pow(10,len-i) + (n/(int)pow(10,i));
               // cout<<m<<endl;
                if(m>n && m<=B)
                {
                    s.insert(m);
                }
            }
            count += s.size();
            s.clear();

        }
        cout<<"Case #"<<k<<": "<<count<<endl;
    }


    return 0;
}
