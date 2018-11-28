/* Author - Anshuman Singh */
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
#include<complex>
using namespace std;

#define Debug 0
#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define FORD(i,a,b) 	for(int i=(a);i>=(b);--i)
#define	REP(i,n)    	FOR(i,0,n)
#define SZ		size()
#define PB		push_back
#define PF		push_front
#define PRINT(x)	cout<<#x<<" = "<<x<<endl
#define PRINTI(x,n)	REP(i,n) cout<<(x)[i]<<" ";cout<<endl
#define PRINTIJ(x,m,n)	for(__typeof(m) i=0;i<m;++i,cout<<"\n") REP(j,n) cout<<(x)[i][j]<<" "
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define EPS		1e-9
#define D_EQ(a,b) 	(a>b-EPS && a<b+EPS)
#define D_LT(a,b) 	((a)<((b)-EPS))
#define D_LTEQ(a,b) 	((a)<((b)+EPS))
#define D_GT(a,b) 	((a)>((b)+EPS))
#define D_GTEQ(a,b) 	((a)>((b)-EPS))
#define ABS(a) 		((a)>=0?(a):(-1.0*(a)))
#define ALL(f,x) 	({bool st=true;f if(!(x)) {st=false;break;};st;})
#define EXISTS(f,x) 	({bool st=false;f if(x) {st=true;break;};st;})
#define COUNT(f,x) 	({int cnt=0;f cnt+=(x);cnt;})
#define getint() 	({int e=0;for(gets(q=s);*q;)e=(e<<3)+(e<<1)+*q++-48;e;})
#define putint(a) 	({int tmp=a,tmp2;*(q=s+10)='\0';for(;;){tmp2=tmp/10;*--q=tmp-(tmp2<<3)-(tmp2<<1)+48;tmp=tmp2;if(!tmp)break;}puts(q);})
#define V(x) vector< x >
#define INF 100000000
#define LIES(a,i) ((a>=min1[i] && a<=max1[i]))
typedef V(int)		VI;
typedef V(string) 	VS;typedef long long	LL;
typedef pair<int,int>	II;
int given[1001][2];
int min1[2],max1[2],n,m;
string g[1001];
int visited[1001];
II invalid[2];
void extend(int a,int i){
	int m1=INF,m2=-INF;
	if(min1[i]>a){
		m1=0;m2=a;
	}
	else if(a>max1[i]){
		m1=a;m2=INF;
	}
	if(m1==INF)return;
	if(m2==INF){
		invalid[i].first=min(m1,invalid[i].first);
	}
	else invalid[i].second=max(m2,invalid[i].second);
	return;
}
int InValid(int a,int i){
	if(a<min1[i] && invalid[i].second>=a)return 1;
	if(a>max1[i] && invalid[i].first<=a)return 1;
	return 0;
}
int Equal(int a,int b){
	REP(i,n)if(!visited[i] && a==given[i][0] && b==given[i][1])return 1;
	return 0;
}
int main(){
	int t;
	cin>>t;
	FOR(cas,1,t+1){
		cout<<"Case #"<<cas<<":\n";
		cin>>n;
		REP(i,2){
			min1[i]=INF;
			max1[i]=-INF;
		}
		memset(visited,0,sizeof(visited));
		invalid[0].first=INF;
		invalid[1].first=INF;
		invalid[0].second=-INF;
		invalid[1].second=-INF;
		REP(i,n){
			cin>>given[i][0]>>given[i][1];
			getchar();
			getline(cin,g[i]);
			if(g[i]=="BIRD"){
				min1[0]=min(min1[0],given[i][0]);
				max1[0]=max(max1[0],given[i][0]);
				min1[1]=min(min1[1],given[i][1]);
				max1[1]=max(max1[1],given[i][1]);
				visited[i]=1;
			}
		}
		REP(i,n)if(!visited[i]){
			if(LIES(given[i][0],0)){
				extend(given[i][1],1);
				visited[i]=1;
			}
			else if(LIES(given[i][1],1)){
				extend(given[i][0],0);
				visited[i]=1;
			}
		}
		cin>>m;
		REP(i,m){
			int a,b;
			cin>>a>>b;
			if(LIES(a,0) && LIES(b,1)){
				cout<<"BIRD\n";
			}
			else if(InValid(a,0)||InValid(b,1)){
				cout<<"NOT BIRD\n";
			}
			else if(Equal(a,b)){
				cout<<"NOT BIRD\n";
			}
			else {
				//assuming that it is a bird
				int m1[2],m2[2];
				REP(i,2){
					m1[i]=min1[i];m2[i]=max1[i];
				}
				min1[0]=min(min1[0],a);max1[0]=max(max1[0],a);
				min1[1]=min(min1[1],b);max1[1]=max(max1[1],b);
				int done=0;
				REP(i,n)if(LIES(given[i][0],0) && LIES(given[i][1],1) && g[i]!="BIRD"){
					cout<<"NOT BIRD\n";
					done=1;
					break;
				}
				if(!done)cout<<"UNKNOWN\n";
				REP(i,2){
					min1[i]=m1[i];max1[i]=m2[i];
				}
			}
		}
	}
	return 0;
}
