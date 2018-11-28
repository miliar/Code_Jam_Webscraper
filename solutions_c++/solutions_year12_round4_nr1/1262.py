//Copyright (c) 2012 VDQD
//Start coding at 2012-05-26-21.08

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
using namespace std;

#define fs first
#define sd second
#define sz(a) (int(a.size()))
#define MP make_pair
#define PB push_back
#define FORE(it,c) for(typeof(c.begin())it=c.begin();it!=c.end();it++)
typedef long long llint;
typedef pair<int,int> II;

const int maxN=10000+10;

int n,last,l[maxN];
II a[maxN];

void solve(int test){
	scanf("%d",&n);
	//if (test==8) fprintf(stderr,"%d\n",n);
	for (int i=1;i<=n;i++){
	    scanf("%d%d",&a[i].fs,&a[i].sd);
	    //if (test==8) fprintf(stderr,"%d %d\n",a[i].fs,a[i].sd);
	}
    int d; scanf("%d",&d);
    //if (test==8)fprintf(stderr,"%d\n",d);
    memset(l,0,sizeof l);
    l[1]=min(a[1].fs,a[1].sd);
    bool ok=(a[1].fs+l[1]>=d);
	for (int i=2;i<=n;i++){
	    l[i]=0;
	    for (int j=1;j<i;j++) if (a[j].fs+l[j]>=a[i].fs){
	        l[i]=max(l[i],min(a[i].fs-a[j].fs,a[i].sd));
	    }
	    l[i]=min(l[i],a[i].sd);
	    if (a[i].fs+l[i]>=d) ok=true;
	    //printf("i=%d,l=%d\n",i,l[i]);
	}
	if (ok) printf("YES\n"); else printf("NO\n");
}

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
	    printf("Case #%d: ",i);
        solve(i);
	}
	return 0;
}
