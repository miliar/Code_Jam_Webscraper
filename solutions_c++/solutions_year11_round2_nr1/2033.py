/*
name:A
By Tony
2011-5-21 обнГ11:53:43
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <string>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <cassert>

using namespace std;
const int maxn=120;
char g[maxn][maxn];

typedef double Dt[maxn];

Dt rpi,wp,owp,oowp,opnum,win;

void init(){
	fill(rpi,rpi+maxn,0);
	fill(wp,wp+maxn,0);
	fill(owp,owp+maxn,0);
	fill(oowp,oowp+maxn,0);
	fill(opnum,opnum+maxn,0);
}

double calwp(int i,int n){
	int j;
	int c0,c1;
	c0=c1=0;
	for(j=0;j<n;j++)
	{
		if(g[i][j]=='1')
			++c1;
		else if(g[i][j]=='0')
			++c0;
	}
	opnum[i]=double(c0+c1);
	win[i]=c1;
	return double(c1)/opnum[i];
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("A","r",stdin);
	//freopen("A.out","w",stdout);
#endif
    int cas,icas=0;
	int n;
	int i,j;
    cin>>cas;
    while(cas--){
    	init();
    	icas++;
    	printf("Case #%d: \n",icas);
    	cin>>n;

    	for(i=0;i<n;++i)
    		for(j=0;j<n;++j)
    			cin>>g[i][j];

    	//cal wp
    	for(i=0;i<n;++i)
    	{
    		wp[i]=calwp(i,n);
    	}

    	//cal owp
    	for(i=0;i<n;++i){
    		for(j=0;j<n;++j){
    			if(g[i][j]=='0')
    			    owp[i]+=((win[j]-1.0)/(opnum[j]-1.0));
    			 else if(g[i][j]=='1')
    			    owp[i]+=(win[j]/(opnum[j]-1.0));
    		}
    		owp[i]/=opnum[i];
    	}

    	//cal oowp

    	for(i=0;i<n;++i){
    		for(j=0;j<n;++j){
    			if(g[i][j]!='.')
    				oowp[i]+=owp[j];
    		}
    		oowp[i]/=opnum[i];
    	}

    	//cal rpi
    	for(i=0;i<n;++i)
    		rpi[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
    	//output

    	for(i=0;i<n;++i)
    		printf("%.12f\n",rpi[i]);




    }


	return 0;
}
