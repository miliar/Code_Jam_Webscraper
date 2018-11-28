#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>

#define ffor(i,n) for(int i=0; i<n; i++)
#define rep(i,n) for(int i=1; i<=n; i++)
#define forit(it,n) for(typeof(n.begin()) it=n.begin(); it!=n.end(); it++)
#define scf(n) scanf("%d", &n);
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
#define pii pair<int,int>
#define INF 1000000000
#define LL long long
#define LD long double

using namespace std;
const int max_t=510;
const int max_n=30;
const int liter=48;

vector<int> tab[max_t];
string s[max_t];
int t;

int main()
{
    scanf("%d ", &t);
    rep(j,t)
    {
	cin >> s[j];
	tab[j].psh(0);
	for(int i=0; i<s[j].size(); i++) tab[j].psh(s[j][i]-liter);
	//forit(it,tab[t]) printf("%d ", *it); printf("\n");
	next_permutation(tab[j].begin(),tab[j].end());
	printf("Case #%d: ", j);
	if(*tab[j].begin()==0) rep(i,tab[j].size()-1) printf("%d", tab[j][i]);
	else
	forit(it,tab[j]) printf("%d", *it); printf("\n");
    }
    


    return 0;
}