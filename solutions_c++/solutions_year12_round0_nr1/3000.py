#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define LL long long
#define bit __builtin_popcountll
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
int p[] = {24,13,5,8,2,22,11,1,10,20,14,12,23,18,4,21,25,15,3,17,9,6,19,7,0,16};
int ob[26]; 
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	for(int i = 0; i < 26; i++)
		ob[p[i]] = i;
	int T;
	scanf("%d\n",&T);
	string s;
	for(int t = 0; t < T; t++)
	{
		printf("Case #%d: ",t + 1);		
		getline(cin,s);
		for(int i = 0; i < sz(s); i++)
		{
			if (s[i] == ' ')
			{
				putchar(' ');
				continue;
			}
			putchar(ob[s[i] - 'a'] + 'a');
		}
		puts("");
	}
	return 0;
}
