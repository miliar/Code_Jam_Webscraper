#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<iostream>

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
const int xam=140;
const int max_t=110;

int tab[max_t][xam];
bool vis[max_t][xam];
int base[max_t];

void play(int t)
{
    string s;
    vector<int> v;
    cin >> s;
    
    int size=s.size();
    int maxi=1;
    int end;
    
    tab[t][s[0]]=1; vis[t][s[0]]=1; v.psh(1);
    for(int i=1; i<size; i++)
    {
	end=i;
	if(s[i]!=s[0]) {tab[t][s[i]]=0; vis[t][s[i]]=1; v.psh(0); break;}
	v.psh(1);
    }
    for(int i=end+1; i<size; i++)
    {
	if(vis[t][s[i]]) {v.psh(tab[t][s[i]]); continue;}
	maxi++;
	tab[t][s[i]]=maxi;
	vis[t][s[i]]=1;
	v.psh(tab[t][s[i]]);
    }
    
   // forit(it,v) printf("%d ", *it); printf("\n");
    long long wyn=0; maxi++;
    for(int i=0; i<v.size(); i++)
    {
	wyn+=(v[i])*pow(maxi,v.size()-i-1);
    }
    printf("Case #%d: %lld\n", t, wyn);
}

int main()
{
    int t;
    scanf("%d", &t);
    rep(i,t) play(i);


    return 0;
}