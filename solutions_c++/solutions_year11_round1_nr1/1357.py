#include <iostream>
#include <vector>
#include <stdint.h>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

inline bool check(int N,int Dw,int Gw,int D,int G,int PD,int PG)
{
if (D>N) return false;
if (D>G) return false;

if (Dw*100!=PD*D) return false;
if (Gw*100!=PG*G) return false;
if (Dw>Gw) return false;
if (D-Dw>G-Gw) return false;

//cout<<"N: "<<N<<" Dw:"<<Dw<<" Gw: "<<Gw<<" D:"<<D<<" G: "<<G<<" PD:"<<PD<<" PG: "<<PG<<endl;

return true;
}

int main(int argc,char** argv)
{
int Dmax=100;
int Gmax=100;
int T=0,N=0,PD=0,PG=0;

cin>>T;

for(int i=0;i<T;++i)
{
cin>>N;
cin>>PD;
cin>>PG;

bool result=false;
for(int G=1;G<=Gmax && result==false;G++)
	for(int D=1;D<=Dmax && D<=N && D<=G;D++)
		{
		int Dw=D*PD/100;
		int Gw=G*PG/100;
		result|=check(N,Dw,Gw,D,G,PD,PG);
		}

cout<<"Case #"<<(i+1)<<": ";
if (result) cout<<"Possible"<<endl;
    else cout<<"Broken"<<endl;

}

return 0;
}