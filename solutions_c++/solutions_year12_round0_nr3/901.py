#include <cstdio>
#include <string>
#include <fstream>
#include <map>
#include <iostream>
#include <set>
using namespace std;

int main()
{
    ifstream cin("i.txt");
    ofstream cout("o.txt");
    int T;
    cin>>T;
    for (int tc=1;tc<=T;tc++)
    {
        int A,B,answer=0;        
        cin>>A>>B;
        int length=0;
        int t=B;
        while (t) length++,t/=10;
        int moder[length];
        moder[0]=1;
        for (int i=1;i<length;i++)
            moder[i]=moder[i-1]*10;
        for (int i=A;i<=B;i++)
        {
            set<int> s;        
            for (int j=1;j<length;j++)
            {
                int t=i;    
                if (t/moder[j]<10)
                   do
                   {
                     t=(t%moder[j])*10+t/moder[j];
                     if (A<=t&&t<=B&&i<t) s.insert(t);                  
                   }
                   while (t!=i);
            }              
            for (int j=1;j<length;j++)
            {
                int t=i;
                if (t/moder[j]<10)
                   do
                   {    
                     t=(t%10)*moder[j]+t/10;
                     if (A<=t&&t<=B&&i<t) s.insert(t);
                   }
                   while (t!=i);
            }
            answer+=s.size();
        }        
        cout<<"Case #"<<tc<<": "<<answer<<endl;
    }
}
