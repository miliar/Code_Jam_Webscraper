

#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 



using namespace std; 

#define mp make_pair
#define pb push_back

template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
template<class T> string tostring(T a){ostringstream os;os<<a;return os.str();}
int toint(string a){istringstream is(a);int p;is>>p;return p;}
long long toll(string a){istringstream is(a);long long p;is>>p;return p;}

void printcase(int i)
{
	cout<<"Case #"<<i<<": ";
}

#define N 100;
bool b[100][26];
bool have[100][26];
bool remain[100];
int sum[26];


map<string,int> ma;

int cmp(const pair<int,string> &s1,const pair<int,string> &s2)
{
	if(s1.first!=s2.first)return s1.first<s2.first;
	return ma[s1.second]>ma[s2.second];
}

pair<int,string> js2(vector<string> &vs,int id,string s2)
{
	memset(b,0,sizeof(b));
	memset(have,0,sizeof(have));	
	memset(sum,0,sizeof(sum));
	memset(remain,1,sizeof(remain));
	for(int i=0;i<vs.size();i++)
		for(int k=0;k<vs[0].size();k++)
		{
			if(vs[i][k]!=vs[id][k])
			{
				b[i][vs[i][k]-'a']=b[i][vs[id][k]-'a']=true;
			}
		}
	for(int i=0;i<vs.size();i++)
		for(int k=0;k<vs[0].size();k++)
			have[i][vs[i][k]-'a']=true;
	for(int i=0;i<vs.size();i++)
		for(int k=0;k<26;k++)
		{
			sum[k]+=have[i][k];
		}
	int res=0;
	for(int i=0;i<s2.size();i++)
	{
		if(sum[s2[i]-'a']==0)continue;
		for(int j=0;j<vs.size();j++)
		{
			if(!remain[j])continue;
			if(b[j][s2[i]-'a'])
			{
				remain[j]=false;
				for(int k=0;k<26;k++)
				{
					sum[k]-=have[j][k];
				}
			}
		}
		if(!have[id][s2[i]-'a'])res++;
	}
	return make_pair(res,vs[id]);
}

pair<int,string> js(vector<string> &vs,string s)
{
	pair<int,string> res;
	for(int i=0;i<vs.size();i++)
	{
		res=max(res,js2(vs,i,s),cmp);
	}
	return res;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long T;
	cin>>T;
	for(long long i=1;i<=T;i++)
	{
		ma.clear();ma[""]=1000000;
		vector<vector<string> > vs;
		int m,n;
		vs.resize(10);
		cin>>n>>m;
		string s,s2;
		for(int i=0;i<n;i++)
		{
			cin>>s;
			vs[s.size()-1].push_back(s);
			ma[s]=i;
		}

		printcase(i);
		for(int i=0;i<m;i++)
		{
			cin>>s2;
			pair<int,string> res;
			for(int i=0;i<10;i++)
			{
				res=max(res,js(vs[i],s2),cmp);
			}
			if(i>0)cout<<' ';
			cout<<res.second;
		}
		cout<<endl;
	}
	//system("pause");
}