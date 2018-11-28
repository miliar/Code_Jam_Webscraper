#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define A first
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;
int fact [] = { 1,1,2,6,24,120};
vector <int> combo;
int n;
char s[10000];
char t[10000];
int main()
{
	int KASES;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		scanf("%d",&n);
		scanf("%s",s);
		int l = strlen(s); 
		printf("Case #%d: ",kases+1);
		combo.clear();
		int minimum = 10000;
		for(int i=0;i<n;i++)
			combo.pb(i);
		for(int i=0;i<fact[n];i++)
		{
			for(int j = 0;j<(l/n);j++){
				for(int k=0;k<n;k++)
					t[j*n + combo[k]]=s[j*n+k];
			}
			int count = 1;
			for(int j=1;j<l;j++)
				if(t[j]!=t[j-1])
					count++;
	//		cout<<i<<" "<<count<<endl;
			if(count < minimum) minimum = count;
			next_permutation(combo.begin(),combo.end());
		}
		printf("%d\n",minimum);
	}
}

