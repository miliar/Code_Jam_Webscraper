#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
#include <cstring>
#include <ctime>
using namespace std;

#define pii pair<int,int>
#define MPII make_pair<int,int>
#define PLL pair<lng,lng>
#define MPLL make_pair<lng,lng>
#define PI 3.1415926535897932384626433832795
#define DEG2RAD (PI/180.0)
#define RAD2DEG (1.0/DEG2RAD)
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define forn(i,n) for(int i=0;i<n;++i)
#define fornr(i,n) for(int i=n-1;i>=0;--i)
#define forn1(i,n) for(int i=0;i<n+1;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define maxll ((1LL<<62)-1+(1LL<<62))
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define abs(a) ((a)<0?-(a):(a))
#define ALL(a) (a).begin(),(a).end()

long long L;
long long t;
long long N;
long long C;

int num[1000001];
int dist[1000001];

int sortFunction( const void *a, const void *b)
{
	 return ( *(int*)b - *(int*)a );
}


int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tc;
	cin>>tc;
	long long res=-1;

	forn(q,tc){
		memset(num,0, sizeof(num));
		memset(dist,0, sizeof(dist));
		cin >> L;
		cin >> t;
		cin >> N;
		cin >> C;
		forn(i, C) 
			scanf("%d", &num[i]);
		
		long long time = 0, count = 0; 
		while (time < t && count < N) {
			if (time+num[count%C]*2 <= t) {
				time+=num[count%C]*2;
				count++;
				continue;
			} else {
				break;
			}
		}
		if (count < N) {
			int temp_dist=-1;
			if (time<=t && (time+num[count%C]*2)>t) {
				temp_dist=num[count%C]-(t-time)*0.5;
				time=t;
			}
			for (long long i=count+1;i<N;i++) {
				dist[i-count-1]=num[i%C];
			}
			dist[N-count-1]=temp_dist;
			long long temp_count=N-count;
			qsort(dist, temp_count, sizeof(int), sortFunction);
			long long l=0;
			while(l<N-count) {
				if (l<L) time+=dist[l]; else time+=dist[l]*2;
				l++;
			} 
			
		}

		cout<<"Case #"<<q+1<<": "<<time<<endl;
	}

	return 0;
}
