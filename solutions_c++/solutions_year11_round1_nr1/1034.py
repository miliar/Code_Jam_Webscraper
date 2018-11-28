#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;
#define MAX 50
#define br false;
#define po true;
long long int n,pg,pd;
bool solution()
{
 int i;
     if(pd<pg && pg==100)
     {
                       return br;
     }
     else
     {
         if((pd==0 && pg!=0 ) || (pd!=0 && pg==0 ))
                    return br;
     
         if(n>100)
                  return po;
         for(i=1;i<=n;i++)
         {
                            if(pd*i%100==0)
                                           return po;
         }
         return br;
     }
}
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    int i,j;
    for(i=0;i<T;i++)
    {
                    fin>>n>>pd>>pg;
                    cout<<n;
                    fout<<"Case #"<<i+1<<": "<<(solution()?"Possible":"Broken")<<"\n";
                    //cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
