#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<int64> vl;
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

char grpid[1024*1024]={0};
int64 tum;
//vi a,b;
int64 me=1,pn=0;
vl primes;
int64 keylimit,keys,letters;
vi frequency;

int64 kamal[1001],fcopy[1001];

void sortfre()
{
	for(int64 i=0;i<letters;i++)
	{
		fcopy[i]=frequency[i];
		kamal[i]=i;
	}	

	for(int64 i=0;i<letters;i++)
	{
		for(int64 j=i+1;j<letters;j++)
		{
			if(fcopy[j]>fcopy[i])
			{
				swap(fcopy[i],fcopy[j]);
				swap(kamal[i],kamal[j]);			
			}		
		}	
	}
}
int64 calcpress()
{
	int64 press=0,over=letters,cnt=0,keyid=1;

	while(over>keys)
	{
		for(int64 i=cnt;i<cnt+keys;i++)
		{
			press+= frequency[kamal[i]]*keyid;		
		}

		cnt+=keys;
		keyid++;
		over-=keys;
	}

	for(int64 i=cnt;i<cnt+over;i++)
	{
		press+= frequency[kamal[i]]*keyid;		
	}

	return press;
	
}
int main() {
	char temp[1000];
	ifstream obj1("A-large.in");
	ofstream obj2("output.txt");
	obj1.getline(temp,100);
	int n = atoi(temp);		
	 
	int64 count = 1;
	while(n--)
	{			
		obj2<<"Case #"<<count++<<": ";
		obj1>>keylimit;
		obj1>>keys;
		obj1>>letters;
		frequency.resize(letters);
		for(int64 i=0;i<letters;i++)
		{
			obj1>>frequency[i];		
		}
		double ans = (letters/keys);
		if( keylimit < ans )
		{
			obj2<<"Impossible";
		}
		else
		{
			sortfre();		
			obj2<<calcpress();
		}
		obj2<<"\n";
	}
	return 0;
}
