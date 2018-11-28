#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

inline void apply_permutation(int k, int n, vi &perm, char S1[], char S2[])
{
	for(int i=0,j;i<n;i+=k)
	{
		for(j=0;j<k;j++) S2[i+j]=S1[i+perm[j]];
	}
}

inline int get_rle_len(int n, char S[])
{
	int res=1;
	char last_char=S[0];
	for(int i=1;i<n;i++)
		if(S[i]!=last_char)
		{
			res++;
			last_char=S[i];
		}

	return res;
}

int main()
{
	int a,b,c,d,tests;

	const string strFile = "d-small";
	string fin = strFile+".in";
	string fout = strFile+".out";

	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);

	char S[50001];
	char curS[50001];
	int k;
	scanf("%d\n", &tests);

for(int test=1;test<=tests;test++)
{

	scanf("%d\n",&k);
	scanf("%s\n",&S);

	int n = strlen(S);

	vi perm;
	fo(a,k) perm.push_back(a);

	int best=1000000;

	do
	{
		apply_permutation(k,n,perm,S,curS);
		best=min(best, get_rle_len(n, curS));
	} while(next_permutation(perm.begin(), perm.end()));

	printf("Case #%d: %d\n",test,best);
}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
