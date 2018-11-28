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

		vector<ll> process;	//��� �¿����� �����ϴ°�
		vector<ll> complete(n,-1);//i��°���� �Ǿտ� �ټ��ִ� ������ ������ -> ������� ���ʷ� �����ϴµ� �ɸ� �ѷ��ڽ��� ���ư�Ƚ��
		/*
			��� ����
			1. �ѹٲ� ��Ÿ�� �������� �׼���(b) ��� �ѷ��ڽ��Ͱ� ���ư����� - a

			�ߺ��� ������ �Ͼ���� Definition ->  .... a .... a 
			
			if(���µ����� �˻��� ����� r���� �������)
				r������ ���� ����
			else
			{
				a + nd + k = r �̶�� �����Ҷ�...
				a = complete[b]			  -> ����Ŭ �����ϱ���
				d = sz(process) - complete[b] -> �ѽ���Ŭ�� ����
				cycle1 = 0 ~ complete[b]-1�� ��
				cycle2 = complete[b] ~ sz(process)�� �� -> �ѽ���Ŭ�� �ش��ϴ� ��
				cycle3 = complete[b] ~ complete[b] + k������ ��

				r-a = nd + k

				(r-a)%d = k
				(r-a)/d = n

				cycle2 * n + cycle1 + cycle3 = ��
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
					break;//���� ���� �׷��̴� ����
				}
				process.push_back(now);	//now���� ſ�� �̹���
				if(cnt >= n){
					//�ѹٲ� ���Ұ�, ���� ��ٸ���.
					if(complete[item.second] != -1)
					{
						//�̹� ����� ���� �ִ� �ƽ�! ������.
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
			//�մ� �����̿�~
			g.pop_front();
			now += item.first;
			vis[item.second] = true;
			g.push_back(item);
			++cnt;
		}
		printf("Case #%d: %lld\n",test,ans);
	}
} 