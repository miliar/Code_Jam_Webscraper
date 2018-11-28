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

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

void sort1(char *buf,char *buf2)
{
	char *temp;
	for(temp=buf;temp<buf2;temp++)
	{
		char *temp2;
		for(temp2=buf2;temp2>temp;temp2--)
		{
			if((*temp2)<(*(temp2-1)))
			{
				char t=*temp2;
				*(temp2)=*(temp2-1);
				*(temp2-1)=t;

			}
		}
	}
}

bool change(char *buf,int size)
{
	int addzero=1;

	char temp;
	int index=0;
	for(int i=size-2;i>=0;i--)
	{
		if(buf[i]<buf[i+1])
		{
			index=i;
			temp=buf[i];
			addzero=0;
			break;
		}
	}
	if(addzero==0)
	{
		int newindex=-1;
		for(int i=size-1;i>=index;i--)
	{
		if(buf[i]>temp)
		{
			newindex=i;
			temp=buf[i];

		}
		if(newindex!=-1)
		{
			for(;i>=index;i--)
			{
				if(buf[i]!=temp)
				{
				char t=buf[i+1];
				buf[i+1]=buf[index];;
				buf[index]=t;
				sort1(&buf[index+1],&buf[size-1]);
				return false;
				}
			}
		}
	}	
	}
	else
	{
		sort1(&buf[0],&buf[size-1]);
		for(int i=0;i<=size-1;i++)
	{
		if(buf[i]!='0')
		{
			temp=buf[i];
			buf[i]=buf[0];
			buf[0]=temp;
			break;
		}
	}
		memcpy(buf+2,buf+1,size);
		buf[1]='0';
		return true;
	}
}

void solve(int test)
{
	char buf[24];
	gets(buf);
	int size=strlen(buf);
	change(buf,size);
	fprintf(stderr,"test=%d\n",test);
	cout<<"Case #"<<test<<": "<<buf<<endl;
}


int main() {
	freopen("a.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	cin>>N;
	char buf[50];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}