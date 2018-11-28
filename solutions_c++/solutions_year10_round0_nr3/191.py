#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef pair<int,LL> PIL;

const int mn = 1005;
PIL a[mn];
int n,r,k;
LL inp[mn]; 

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		r=GI,k=GI,n=GI;
		REP(i,n)	inp[i]=GI,a[i].first=a[i].second=-1;
		printf("Case #%d: ",kase);
		int curpos=0,curround=0;
		LL cursum=0;
		REP(i,n)	cursum+=inp[i];
		if(cursum<=k){
			cout<<cursum*r<<endl;
			continue;
		}
		cursum=0;
		while(curround<r){
			if(a[curpos].first!=-1)	break;
			a[curpos].first=curround++;
			a[curpos].second=cursum;
			int j;
			LL s=0;
			for(j=curpos;;(j=j+1)%=n){
				s+=inp[j];
				if(s>k)	break;
			}
			curpos=j;
			cursum+=s-inp[j];
		}
		if(curround<r){
			int cyclen=curround-a[curpos].first;
			LL cycsum=cursum-a[curpos].second;
			int v=(r-curround)/cyclen;	//I can have v cycles
			cursum+=v*cycsum;
			curround+=cyclen*v;
			while(curround<r){
				int j;
				LL s=0;
				for(j=curpos;;(j=j+1)%=n){
					s+=inp[j];
					if(s>k)	break;
				}
				curpos=j;
				cursum+=s-inp[j];
				curround++;
			}
		}
		cout<<cursum<<endl;
	}
	
	cerr<<"Completed"<<endl;
	while(1);
	return 0;
}
