#include<iostream>
#include<conio.h>
#include<fstream>
#include<algorithm>
using namespace std;
typedef long long int ll;
int main()
{
    int nt;
    ifstream din("A-large.in");
    ofstream dout("out.txt");
    din>>nt;
    int g=1;
    while(g<=nt)
    {
                ll p;
                ll k;
                ll l,i;
                din>>p>>k>>l;
                
                ll a[l],cost=0;
                for(i=0;i<l;i++)
                 din>>a[i];
                 if(p*k<l){
                          
                cout<<"Impossible\n";
                g++;
                continue;
              }
                   ll j=0;
                 sort(a,a+l);
                for(i=l-1;i>=0;i--)
                {
                
                    cost+=a[i]*(j/k+1);
                    j++;               
                }
                 dout<<"Case #"<<g<<": "<<cost<<endl;
                 cout<<cost<<endl;
             g++;    
    }
    getch();
    return 0;
}
