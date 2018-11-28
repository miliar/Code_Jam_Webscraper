#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <stack>

#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i=0; i<(int)(n); i++)

using namespace std;
typedef long long int tint;

double wp[128];
double owp[128];
double oowp[128];
int jug[128];
char par[128][128];

int main(){
	ifstream in("a.in");
	ofstream out("a.out");
	
	int T, k=0;
	in>>T;
	while(k<T)
	{
	forn(i,128){
		wp[i]=0;
		owp[i]=0;
		oowp[i]=0;
		jug[i]=0;
		}
	k++;
	int N;
	in>>N;
	forn(i,N)forn(j,N)in>>par[i][j];
	
	forn(i,N)
	{
		int w=0, p=0;
		forn(j,N)
		{
			if(par[i][j]!='.')p++;
			if(par[i][j]=='1')w++;
			
		}
		//cout<<w<<' '<<p<<endl;
		wp[i]=w/(double)p;
		//cout<<wp[i]<<endl;
		jug[i]=p;
	}
	
	forn(i,N)
	{
		//cout<<wp[i]<<endl;

		double ac=0;
		forn(j,N)
		{
			if(par[i][j]!='.')
			{
				int w=0;
				forn(k,N)if(par[j][k]=='1' && k!=i)w++;
				ac+=w/(double)(jug[j]-1);
				}
			}
		owp[i]=ac/(double)jug[i];
		}

	forn(i,N)
	{
		//cout<<wp[i]<<endl;

		double ac=0;
		forn(j,N)
		{
			if(par[i][j]!='.')ac+=owp[j];
			}
		oowp[i]=ac/(double)jug[i];
		}
	

	out<<"Case #"<<k<<":"<<endl;
	//cout<<wp[2]<<endl;
	
	forn(i,N){
	//cout<<wp[2]<<endl;

		//cout<<wp[i]<<' '<<owp[i]<<' '<<oowp[i]<<endl;
		double res=(wp[i]/4.0)+(owp[i]/2.0)+(oowp[i]/4.0);
		out<<res<<endl;
		}
	
	}
}
