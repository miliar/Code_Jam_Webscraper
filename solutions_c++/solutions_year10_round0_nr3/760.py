#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}
inline int bitcnt(int n) {int ret = 0; while(n) { ret += n&1; n>>=1;}return ret; }

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int tests;
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		ll r,k,n;
		cin>>r>>k>>n;
		deque<pair<ll,ll> > g;
		for(int i=0;i<n;++i){
			ll now; cin>>now;
			g.push_back(make_pair(now,i));
		}

		vector<ll> process;	//몇명씩 태웠는지 저장하는값
		vector<ll> complete(n,-1);//i번째놈이 맨앞에 줄서있는 순간을 정의함 -> 여기까지 최초로 도달하는데 걸린 롤러코스터 돌아간횟수
		/*
			고려 사항
			1. 한바꾸 다타고 나서부터 그순간(b) 몇번 롤러코스터가 돌아갔는지 - a

			중복된 순간이 일어났다의 Definition ->  .... a .... a 
			
			if(여태동안의 검사한 사건이 r보다 작을경우)
				r까지의 합이 정답
			else
			{
				a + nd + k = r 이라고 정의할때...
				a = complete[b]			  -> 싸이클 시작하기전
				d = sz(process) - complete[b] -> 한싸이클의 길이
				cycle1 = 0 ~ complete[b]-1의 합
				cycle2 = complete[b] ~ sz(process)의 합 -> 한싸이클에 해당하는 값
				cycle3 = complete[b] ~ complete[b] + k까지의 합

				r-a = nd + k

				(r-a)%d = k
				(r-a)/d = n

				cycle2 * n + cycle1 + cycle3 = 답
			}
		deque<pair<ll,ll> > q(g);
		ll tcnt = 0;
		ll tnow = 0;
		ll tans = 0;
		while(true)
		{
			pair<ll,ll> res = q.front();
			if(res.first + tnow > k)
			{
				tcnt++;
				if(tcnt == r)
				{
					printf("%d\n",tans);
					break;
				}
				tnow = 0;
				continue;
			}
			q.pop_front();
			tnow += res.first;
			tans += res.first;
			q.push_back(res);
		}
		*/
		ll cnt = 0;
		ll now = 0;
		ll ans = 0;
		bool vis[1001]; memset(vis,false,sizeof(vis));
		while(true)
		{
			pair<ll,ll> item = g.front();
			if(now + item.first > k || vis[item.second]){
				memset(vis,false,sizeof(vis));
				if(now == 0){
					for(int i=0;i<sz(process);++i) ans += process[i];
					break;//존나 많은 그룹이다 젠장
				}
				process.push_back(now);	//now명이 탓다 이번엔
				if(cnt >= n){
					//한바꾸 돌았고, 나는 기다린다.
					if(complete[item.second] != -1)
					{
						//이미 저장된 값이 있다 아싸! 끝났따.
						if(sz(process) >= r){
							for(int i=0;i<r;++i) ans += process[i];
						}else{
							ll a = complete[item.second];
							ll d = sz(process) - complete[item.second];
							ll k = (r-a)%d;
							ll n = (r-a)/d;
							ll c1=0,c2=0,c3=0;
							for(int i=0;i<a;++i) c1 += process[i];
							for(int i=a;i<sz(process);++i) c2 += process[i];
							for(int i=a;i<a+k;++i) c3 += process[i];

							ans = c1 + c2*n + c3;
						}
						break;
					}
					else complete[item.second] = sz(process);
				}
				now = 0;
				continue;
			}
			//손님 입장이요~
			g.pop_front();
			now += item.first;
			vis[item.second] = true;
			g.push_back(item);
			++cnt;
		}
		printf("Case #%d: %lld\n",test,ans);
	}
} 