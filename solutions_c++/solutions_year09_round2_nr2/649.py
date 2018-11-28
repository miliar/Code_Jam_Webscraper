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

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tn;
	int ti=0;
	scanf("%d",&tn);
	while(tn--)
	{
		char p[128];
		char p2[128];
		int n;
		scanf("%s",p);
		strcpy(p2,p);
		n=strlen(p);
		sort(p2,p2+n);
		printf("Case #%d: ", ++ti);
		if(next_permutation(p,p+n))
		{
			printf("%s\n",p);
		}
		else
		{
			char ch;
			For(i,n) if(p2[i]!='0') {ch=p2[i]; break;}
			p2[n++]='0';
			p2[n]=0;
			sort(p2,p2+n);
			For(i,n) if(p2[i]==ch) {swap(p2[0],p2[i]); break;}
			sort(p2+1,p2+n);
			p2[n]=0;
			printf("%s\n",p2);
		}
		
	}
}

/*
3
115
1051
6233
*/