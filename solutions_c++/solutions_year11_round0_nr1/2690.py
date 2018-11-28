#include<iostream>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;
int main()
{
    int i,j,b1,b,f,t,o1,o,n,po,pb,s;
    char c,s1;
    cin>>t;
    for(i=0;i<t;i++)
    {
        s1='1';
        pb=po=s=0;
        o=b=1;
        cin>>n;
        for(j=0;j<n;j++)
        {
            cin>>c;
            cin>>f;
            if(c=='O')
            {
                if(abs(o-f)+1-po>0){s+=abs(o-f)+1-po;pb+=abs(o-f)+1-po;}
                else {s++;pb++;}
                po=0;
                o=f;
            }
            else
            {
                if(abs(b-f)+1-pb>0){s+=abs(b-f)+1-pb;po+=abs(b-f)+1-pb;}
                else {s++;po++;}
                pb=0;
                b=f;
            }
        }
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
}
