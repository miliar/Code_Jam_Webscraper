#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Sort(a) sort(All(a))
#define Eo(x) { cerr << #x << " = " << (x) << endl; } 
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

int memo[51][51];
int memo2[51][51];
int N;
int K;
int ans;
int dx[]={-1,0,-1,-1};
int dy[]={0,-1,-1,1};
int cache[51][51][4][3];
void relocate()
	{
	Fill(memo2,0);
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				{
					memo2[i][j]=memo[N-1-j][i];
				}
			for(int i=0;i<N;i++)
				{
					int cur=N-1;
					for(int j=N-1;j>=0;j--)
						{
							if(memo2[j][i]!=0)
								{
									memo2[cur][i]=memo2[j][i];
									if(j!=cur)
									 memo2[j][i]=0;
									cur--;
								}
						}
				}
	}
void computer()
	{
		Fill(cache,0);
		Rep(i,N)
			Rep(j,N)
			{
				Rep(k,4)
					{
						cache[i][j][k][memo2[i][j]]++;

							int x=i+dx[k];
							int y=j+dy[k];
							if((x<0)||(x>=N)||(y<0)||(y>=N)) continue;
							cache[i][j][k][memo2[i][j]]+=cache[x][y][k][memo2[i][j]];
					}
			}
	}

void solve(int test)
{
  Fill(memo,0);
  cin>>N>>K;
	Rep(i,N)
		{
			string s;
			cin>>s;
			Rep(j,N)
				{
					if(s[j]=='R')
						memo[i][j]=1;
					if(s[j]=='B')
						memo[i][j]=2;
				}
		}
	relocate();
  computer();
	bool red=false;
	bool blue=false;
	Rep(i,N)
		Rep(j,N)
		 Rep(k,4)
		{
				if(cache[i][j][k][1]>=K)
					red=true;
				if(cache[i][j][k][2]>=K)
					blue=true;
		}
  Eo(test);
	string res="";
	if(red&&blue)
		res+="Both";
	if(red&&!blue)
		res+="Red";
	if(!red&&blue)
		res+="Blue";
	if(!red&&!blue)
		res+="Neither";


	cout<<"Case #"<<test<<": "<<res<<endl;
}


int main() {
	freopen("a.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	cin>>N;
	char buf[90];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}