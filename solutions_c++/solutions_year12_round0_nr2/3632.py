#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int t,n,s,a,r,p,x;
    fstream f,g;
    f.open("B-large.in",ios::in);
    g.open("output.out",ios::out);
    f>>t;
    for(int i=1;i<=t;i++)
    {
        f>>n>>s>>p; 
        r=0; 
        while(n--)
        {
            f>>a;
            if(a%3==0)
            {
                    x=a/3;
                    if(x>=p) r++;
                    else if((x+1)==p&&s&&x>0) {r++;s--;}
            }
            else if(a%3==1)
            {
                    x=(a/3)+1;
                    if(x>=p){r++;}
            }
            else if(a%3==2)
            {
                    x=(a/3)+1;
                    if(x>=p) r++;
                    else if((x+1)==p&&s) {r++;s--;}
            }
        }
        g<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
