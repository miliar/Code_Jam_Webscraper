#include<iostream>
#include<string>
#include<sstream>
#include<conio.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {       
            string a,b;
            cin>>a;
            cin>>b;
            int p,q,r,s,count=0;
            if(a.length()==1 && b.length()==1)
            cout<<"Case #"<<i<<": 0"<<endl;
            else
            {
            stringstream(a)>>p;
            stringstream(b)>>q;
            for(int j=p;j<=q;j++)
            {
                    stringstream temp;
                    string x;
                    temp<<j;
                    temp>>x;;
                    for(int l=1;l<x.length();l++)
                    {
                            string y;        
                            y=x.substr(l);
                            y+=x.substr(0,l);
                            stringstream(x)>>r;
                            stringstream(y)>>s;
                            if(p<=r && r<s && s<=q)
                            
                            count++;
                                          }
            }
            cout<<"Case #"<<i<<": "<<count<<endl;
            }
    }
    return 0;
}
            
    
