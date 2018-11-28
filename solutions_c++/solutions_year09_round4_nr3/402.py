#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;

const int MAXN=16;
const int MAXK=25;
int p[MAXN][MAXK];
int r[MAXN][MAXN];
int memo[MAXN][1<<MAXN];
vector<int> src;
int e;

int n,k;

int relation(int i,int j){

    // if i is under j return -1
    // if i is over j return 1
    // if i and j can't go return 0

    int stat=-2;
    for(int K=0;K<k;K++){
	if(stat==-2)
	    if(p[i][K]>p[j][K])
		stat=1;
	    else if(p[i][K]<p[j][K])
		stat=-1;
	    else return 0;
	else if(stat==1){
	    if(p[i][K]<=p[j][K])
		return 0;
	}
	else if(stat==-1)
	    if(p[i][K]>=p[j][K])
		return 0;
    }
    return stat;
}

int go(int c,int m){

    int &mem=memo[c][m];
    if(mem!=-1) return mem;

    m|=(1<<c);
    if(m==e) return 0;
    int res=2e9;
    bool f=1;
    for(int i=0;i<n;i++)
	if(!(m&(1<<i)))
	    if(r[c][i]==1){
		f=0;
		res=min(res,go(i,m));
	    }

    if(f){
	for(int i=0;i<n;i++)
	    if(!(m&(1<<i))){
		res=min(res,go(i,m)+1);
	    }
    }
    return mem=res;
}

main(){

    int T; scanf("%d",&T); for(int test=1;test<=T;test++){

	memset(memo,-1,sizeof(memo));

	printf("Case #%d: ",test);

	scanf("%d %d",&n,&k);
	for(int i=0;i<n;i++)
	    for(int j=0;j<k;j++)
		scanf("%d",&p[i][j]);

	for(int i=0;i<n;i++){
	    bool f=1;
	    for(int j=0;j<n;j++)
		if(i!=j){
		    r[i][j]=relation(i,j);
		    if(r[i][j]==-1) f=0;
		}
	}

	e = (1<<n)-1;

	int res=2e9;
	for(int i=0;i<n;i++)
	    res=min(res,go(i,0));
	cout<<res+1<<endl;

    }
}
