#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
 
#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))
 
int main(){
	int test;
	scanf("%d",&test);
	ree(T,1,test){
		printf("Case #%d: ",T);
		long long l,t,n,c;
		cin>>l>>t>>n>>c;
		vector<long long> dis(c,0);
		rei(i,0,c) cin>>dis[i];
		int pos=0;
		vector<long long> dist(n,0);
		rei(i,0,dist.size()){
			dist[i]=dis[pos];
			(++pos)%=c;
		}
		long long tot=0ll;
		rei(i,0,n) tot+=(dist[i]);
		if(l==0){
			cout<<tot*2ll<<endl;
			continue;
		}
		vector<long long> cumm(n+1,0ll);
		cumm[1]=(dist[0]);
		rei(i,1,n) cumm[i+1]=cumm[i]+dist[i];
		vector<long long> save(n,0ll);
		rei(i,0,n){
			if(t<=cumm[i]*2ll){
				save[i]=dist[i];
				continue;
			}
			if(t>=(cumm[i+1]*2ll)){
				continue;
			}
			save[i]=cumm[i+1]-(t/2ll);
		}	
		srt(save);
		rev(save);
		long long ans=0ll;
		rei(i,0,l) ans+=save[i];
//		cout<<tot<<endl;
		cout<<tot*2ll-ans<<endl;	
		
	}
	return 0;
}
