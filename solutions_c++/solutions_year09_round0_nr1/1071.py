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
const int max_l=17;
const int max_d=5010;
const int max_n=510;
const int max_liter=30;
const int liter=96;

char dane[max_d][max_l];
bool vis[max_n][max_l][max_liter];
int l,d,n;


int main()
{
    scanf("%d%d%d", &l,&d,&n);
    ffor(i,d) ffor(j,l) {scanf(" %c", &dane[i][j]); dane[i][j]-=liter;}
    ffor(i,n)
    {
	int wyn=0;
	int count=0;
	string temp;
	cin >> temp;
	forit(it,temp)
	{
	    if(*it=='(')
	    {
		it++;
		for(; *it!=')'; it++) vis[i][count][(*it)-liter]=1;
	    }
	    else if(*it>96 && *it<123) vis[i][count][(*it)-liter]=1;
	    else continue;
	    count++;
	}
	
	bool bol;
	ffor(j,d)
	{
	    bol=1;
	    ffor(k,l)
	    {
		if(vis[i][k][dane[j][k]]) continue;
		else {bol=0; break;}
	    }
	    if(bol) wyn++;
	}
	printf("Case #%d: %d\n", i+1, wyn);
    }
    
    /*ffor(i,n)
    {
	printf("%d:\n\t", i);
	ffor(j,l)
	{
	    printf("(");
	    ffor(k,max_liter) if(vis[i][j][k]) printf("%c", k+liter);
	    printf(")");
	}
	printf("\n");
    }*/

    return 0;
}