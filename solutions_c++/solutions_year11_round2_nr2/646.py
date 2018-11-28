#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>

#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define eps 1e-07

using namespace std;
typedef long long int tint;

int C, D;
double pos[256];
int val[256];
double nue[256];

bool bs(double t)
{
	double prim=pos[0]-t;
	double ult=prim+(double)D*(val[0]-1);
	if(ult-pos[0]>t)return false;
	else nue[0]=ult;
	
	forn(i,C-1)
	{
		prim=max(nue[i]+D, pos[i+1]-t);
		ult=prim+(double)D*(val[i+1]-1);
		if(ult-pos[i+1]>t)return false;
		else nue[i+1]=ult;
		}
	return true;
	}

int main(){
	ifstream in("b.in");
	ofstream out("b.out");
	
	int T, k=0;
	in>>T;
	while(k<T)
	{
	k++;
	in>>C>>D;
	forn(i,C)in>>pos[i]>>val[i];
	
	double tmin=0.0, tmax=1000.0;
	while(tmax-tmin>eps)
	{
	double tm=(tmax+tmin)/2.0;
	bool chk=bs(tm);
	if(chk)tmax=tm;
	else tmin=tm;
	}
	
	
	
	out<<"Case #"<<k<<": ";
	out<<tmin<<endl;
	}
}
