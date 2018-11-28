#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0x3FFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 
//#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it) 


int main()
{
	FILE *in = fopen("D-small-attempt0.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;
	int tn;
	int ti = 0;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int K;
		char p[1024];
		fscanf(in,"%d",&K);
		fscanf(in,"%s",p);
		int n = strlen(p);
		int a[10];
		For(i,K) a[i] = i;
		int ans = MAX;
		do
		{
			char p2[1024];
			for(int i = 0; i < n; i += K) For(j,K) p2[i+j] = p[i+a[j]];
			char ch = 0;
			int t = 0;
			For(i,n) {if(ch != p2[i]) ++t; ch = p2[i];}
			ans = min(ans, t);
		} while(next_permutation(a,a+K));
		fprintf(out,"Case #%d: %d\n",++ti, ans);
	}
}

/*
2
4
abcabcabcabc
3
abcabcabcabc

*/