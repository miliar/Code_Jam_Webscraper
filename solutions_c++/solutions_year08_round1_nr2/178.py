#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <list>
#include <math.h>
#include <queue>
using namespace std;


#define LLI long long
#define INF 2147483600
#define FOR(i,start,end) for(int i=(start); i<(end); ++i)
//#define FORALL(it,A) for(typeof((A).begin()) it=(A).begin(); it!=(A).end(); ++it)
#define FORALL(tp,it,A) for(tp::iterator it=(A).begin(); it!=(A).end(); ++it)
#define DEB(x) cout << #x << ":" << x << endl


const double eps=1e-11;


int N,M;
vector< vector<int> > Cust;
vector<bool> Melt;
int toBeMelted;


bool isGood(){

	FOR(i,0,N)
		if (Cust[i].size()==1 && Cust[i][0]>0){
			toBeMelted = Cust[i][0];
			return false;
		}
	
	return true;
}


void Change(){
	Melt[toBeMelted] = true;
	FOR(i,0,N)
		FOR(j,0,Cust[i].size())
			if (Cust[i][j]==toBeMelted || Cust[i][j]==-toBeMelted){
				Cust[i].erase(Cust[i].begin()+j);
				--j;
			}
}

int main(){

	int D;
	scanf("%d", &D);
	FOR(d,1,D+1){
		scanf("%d%d",&M,&N);
		

		Cust.clear();
		Cust.resize(N);
		FOR(i,0,N){
			int m; scanf("%d",&m);
			int k,isk;
			FOR(j,0,m){
				scanf("%d%d",&k,&isk);
				if (isk) Cust[i].push_back(k);
				else Cust[i].push_back(-k);
			}
		}

		vector< vector<int> > Cust2 = Cust;

		Melt.clear();
		Melt.assign(M+1,false);

		while (!isGood())
			Change();

		vector<bool> passed(N);
		FOR(i,0,N)
			FOR(j,0,Cust2[i].size()){
				int mm=Cust2[i][j];
				if (Melt[abs(mm)] == ( mm>0 )){
					passed[i]=true;
					break;
				}
			}
		bool pass=true;
		FOR(i,0,N) if (!passed[i]){
			printf("Case #%d: IMPOSSIBLE\n",d);
			pass=false;
			break;
		}
		if (!pass) continue;
		printf("Case #%d:",d);
		FOR(i,1,M+1) printf(" %d",(int)Melt[i]);
		printf("\n");

	}

	return 0;
}

