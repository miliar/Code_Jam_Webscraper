#include <cstdio>
#include <string>
#include <fstream>
#include <map>
#include <iostream>
using namespace std;

int main()
{
    ifstream cin("i.txt");
    ofstream cout("o.txt");
    int T;
    cin>>T;
    for (int tc=1;tc<=T;tc++)
    {
        int N,S,p;
        cin>>N>>S>>p;
        int t[N];
        for (int i=0;i<N;i++) cin>>t[i];
        int sb[N],nb[N];
        bool sp[N],np[N];
        int answer=0;
        for (int i=0;i<N;i++)
        {
            sb[i]=0;
            nb[i]=0;
            for (int k=0;k<=10;k++)
            {
                if (k+k+k==t[i]) nb[i]>?=k;
                if (k+1<=10)
                {
                   if (k+k+k+1==t[i]) nb[i]>?=k+1;
                   if (k+k+1+k+1==t[i]) nb[i]>?=k+1;
                   if (k+2<=10)
                   {
                      if (k+k+k+2==t[i]) sb[i]>?=k+2;
                      if (k+k+1+k+2==t[i]) sb[i]>?=k+2;
                      if (k+k+2+k+2==t[i]) sb[i]>?=k+2;
                   }
                }
            }
            sp[i]=sb[i]>=p;
            np[i]=nb[i]>=p;
            if (np[i]) answer++;
            else if (S&&sp[i]) answer++,S--;
        }
        cout<<"Case #"<<tc<<": "<<answer<<endl;
    }
}
