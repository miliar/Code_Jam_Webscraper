#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

int n;
char a[200][200];
ld wp[200];
int k[200];
ld owp[200],oowp[200];
int k2[200],k3[200];

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		printf("Case #%d:\n",z);
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
				scanf(" %c ",&a[i][j]);
		for (int i=0;i<n;++i){
			wp[i]=owp[i]=oowp[i]=0;
			k[i]=k2[i]=k3[i]=0;
		}
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j){
				if (a[i][j]!='.')
					++k[i];
				if (a[i][j]=='1')
					wp[i]+=1;
			}
		
		for (int i=0;i<n;++i){
			for (int j=0;j<n;++j)
				if (a[i][j]!='.'){
					++k2[i];
					if (a[i][j]=='1')
						owp[i]+=wp[j]/ld(k[j]-1);
					else owp[i]+=(wp[j]-1)/ld(k[j]-1);
				}
		}
		for (int i=0;i<n;++i)
			wp[i]=wp[i]/ld(k[i]);
		for (int i=0;i<n;++i)
			owp[i]=owp[i]/ld(k2[i]);
		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
				if (a[i][j]!='.'){
					++k3[i];
					oowp[i]+=owp[j];
				}
		for (int i=0;i<n;++i)
			oowp[i]=oowp[i]/ld(k3[i]);
		cout.precision(10);
		for (int i=0;i<n;++i)
			cout<<fixed<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
	}
	return 0;
}