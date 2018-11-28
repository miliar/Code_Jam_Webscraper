#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long LL;
const int INF = 1000000001;
typedef pair<int, int> PII;
typedef vector< PII > VPII;
typedef vector< VPII > VVPII;

#define FOR(x,b,e) for(int x=b; x<=(e);++x)
#define FORD(x,b,e) for(int x=b; x>=(e);--x)
#define REP(x,n) for(int x=0;x<(n);++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

typedef vector<char> VC;
typedef vector< VC > VVC;

void print_tab(VC& tab)
{

	cout<<"[";
	REP(i,SIZE(tab))
	{
		cout<<tab[i];
		if(i<SIZE(tab)-1)
		{
			cout<<", ";
		}
	}
	cout<<"]";
}
void round()
{
	VVC arrC(256,VC(256,0));
	vector< vector<bool> > arrD(256,vector<bool>(256,0));
	int C,D,N;
	string tmp;

	cin>>C;
	VC c_s[C];
	REP(i,C)
	{
		cin>>tmp;
		REP(j,3)
		{
			c_s[i].PB(tmp[j]);
		}
	}
	cin>>D;
	VC d_s[D];
	REP(i,D)
	{
		cin>>tmp;
		REP(j,2)
		{
			d_s[i].PB(tmp[j]);
		}
	}
	cin>>N;
	VC n_s(N);
	cin>>tmp;
	REP(i,N)
	{
		n_s[i]=tmp[i];
	}
	REP(i,C)
	{
		arrC[c_s[i][0]][c_s[i][1]] = c_s[i][2];
		arrC[c_s[i][1]][c_s[i][0]] = c_s[i][2];
	}
	REP(i,D)
	{
		arrD[d_s[i][1]][d_s[i][0]] = 1;
		arrD[d_s[i][0]][d_s[i][1]] = 1;
	}
	VC out;
	REP(i,N)
	{
		if(out.size()>0)
		{
			bool did = false;
			if(arrC[out[out.size()-1]][n_s[i]]!=0)
			{
				char cc = out[out.size()-1];
				out.pop_back();
				did=true;

				out.PB(arrC[cc][n_s[i]]);
			}
			else
			{
				REP(j,out.size())
				{
					if(arrD[out[j]][n_s[i]])
					{
						out.clear();
						did = true;
						break;
					}
				}
			}
			if(!did)
			{
				out.PB(n_s[i]);
			}
		}
		else
			out.PB(n_s[i]);
	}
	print_tab(out);
	//REP(i,out.size())
	//{
	//	cout<<out[i];
	//}
	//cout<<C<<" ";
	//REP(i,C)
	//{
	//	cout<<" ";
	//	REP(j,3)
	//	{
	//		cout<<c_s[i][j];	
	//	}
	//}
	//cout<<D<<" ";
	//REP(i,D)
	//{
	//	cout<<" ";
	//	REP(j,2)
	//	{
	//		cout<<d_s[i][j];
	//	}
	//}
	//cout<<N<<" ";
	//REP(i,N)
	//{
	//	cout<<n_s[i];
	//}

}

int main() {
	
	int N;
	cin>>N;
	FOR(i,1,N)
	{
		cout<<"Case #"<<i<<": ";
		round();
		cout<<endl;
	}

	return 0;
}
