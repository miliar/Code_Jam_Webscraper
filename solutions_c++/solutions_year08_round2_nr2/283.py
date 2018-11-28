#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#include <set>
#include <vector>
#include <utility>
#include <map>

#include <algorithm>

using namespace std;


typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;

typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define forn(i,N) for(int i=0;i<(N); ++i)

//FILE * f = fopen("a.in","rt",stdin);
//FILE * g = fopen("b-small.out","wt");
ifstream f("b-small-attempt0.in",ifstream::in);
ofstream g("b-small.out",ofstream::out);

bool G[1002][1002];
bool taken[1002];

vector<int> primes;

void generateprimes()
{
	primes.clear();
	primes.push_back(2);
	for(int i=3;i<=1000;i++)
	{
		int j;
		for(j=0;j<primes.size();j++)
			if (i % primes[j]==0) break;
		if (j==primes.size())
			primes.push_back(i);
	}
}

int getgcd(int a, int b)
{
	while (b>0)
	{
		a = a % b;
		int tmp = a;
		a = b;
		b = tmp;
	};
	return a;
}

bool hasdiv(int a, int b, int p)
{
	int d = getgcd(a,b);
	for (int i=0;i<primes.size();i++)
		if ( (primes[i]>=p) && (d%primes[i]==0))
			return true;
	return false;
}

int main()
{
	generateprimes();
	
	int nTests; f>>nTests;
	//string s;
	ll a, b, p;
	forn(TestIndex,nTests)
	{
		f>>a>>b>>p;
		memset(G,0,sizeof(G));
		memset(taken,0,sizeof(taken));
		
		for(int i=a;i<=b;i++)
			for(int j=i+1;j<=b;j++)
				G[j][i] = G[i][j] = hasdiv(i,j,p);
		
		for(int i=a;i<=b;i++)
			G[i][i]=true;

		//floyd
		forn(k,b+1)
			forn(i,b+1)
				forn(j,b+1)
					G[i][j]= G[i][j] || (G[i][k]&&G[k][j]);
		
		int count = 0;
		for(int i=a;i<=b;i++)
		{
			if (taken[i])
				continue;
			taken[i]=true;
			count ++;
			for(int j=a;j<=b;j++)
				if (G[i][j]) taken[j]=true;
		}

		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": "<<count<<endl;
		cout<<"Case #"<<TestIndex+1<<": "<<count<<endl;

	}
	return 0;
}
