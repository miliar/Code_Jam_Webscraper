//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}

const int N=24*60;
vector<int> A[N*2],B[N*2];
int TA[N*2],TB[N*2];
int gettime(){
	int a,b;
	scanf("%d:%d",&a,&b);
	return a*60+b;
}
int main(){
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;test++){
		for(int i=0;i<N;i++)
			A[i].clear(),B[i].clear();
		memset(TA,0,sizeof(TA));
		memset(TB,0,sizeof(TB));
		int na,nb,T;
		scanf("%d%d%d",&T,&na,&nb);
		for(int i=0;i<na;i++){
			int a=gettime(),b=gettime();
			A[a].push_back(b+T);
		}
		for(int i=0;i<nb;i++){
			int a=gettime(),b=gettime();
			B[a].push_back(b+T);
		}
		int NA=0,NB=0;
		int RA=0,RB=0;
		for(int i=0;i<N;i++){
			NA+=TA[i],NB+=TB[i];
			for(int j=0;j<A[i].size();j++){
				if(NA==0)
					NA++,RA++;
				NA--,TB[A[i][j]]++;
			}
			for(int j=0;j<B[i].size();j++){
				if(NB==0)
					NB++,RB++;
				NB--,TA[B[i][j]]++;
			}
		}
		printf("Case #%d: %d %d\n",test,RA,RB);
	}
scanf("%*s");
}
