#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;
int N,K,B,T;
double tt[200];
int dis[200];
int v[200];
int main() {
	//freopen("f:\\b-small.in","r",stdin); freopen("f:\\b-small.out","w",stdout);
	freopen("f:\\b-large.in","r",stdin); freopen("f:\\b-large.out","w",stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		cin>>N>>K>>B>>T;
		for(int i=0;i<N;i++){
			cin>>dis[i];
			dis[i]=B-dis[i];
		}
		for(int i=0;i<N;i++) cin>>v[i];
		for(int i=0;i<N;i++){
			tt[i]=dis[i]*1.0/v[i];
		}
		int a[101];
		memset(a,0,sizeof(a));
		int cnt=0;
		/*
		for(int i=0;i<N;i++)
			cout<<tt[i]<<" ";
		cout<<endl;
		*/
		for(int i=0;i<N;i++){
			if(T-tt[i]>=-0.00001){
				a[i]=1;
				cnt++;
			}
		}
		if(cnt<K) { cout<<"IMPOSSIBLE"<<endl; continue;}
		cnt = 0;
		int start;
		for(int i=N-1;i>=0;i--) {
			if(a[i]==1) cnt++;
			if(cnt>=K) {
				start = i;
				break;
			}
		}
		int res = 0;
		cnt =0;
		int inx=start;
		while(inx<N) {
			if(a[inx]==0) res+=cnt;
			if(a[inx]==1) cnt+=1;
			inx+=1;
		}
		cout<<res<<endl;
	}
}