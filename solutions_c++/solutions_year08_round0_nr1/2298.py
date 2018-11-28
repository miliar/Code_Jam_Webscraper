#include<iostream>
#include<string>
#include<bitset>
#include<map>

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define mp make_pair
#define cs c_str()

#define GI ({int _;scanf("%d",&_);_;})
#define COUNT(f,x) ({int _=0;f _+=(x);_;})
#define EXISTS(f,x) ({int _=0;f if(x) {_=1;break;}_;})
#define ALL(f,x) (!EXISTS(f,!(x)))
#define MIN(f,x) ({LL _=LINF;f _<?=(x);_;})
#define MAX(f,x) (-MIN(f,-(x)))
using namespace std;
char engines[100][100],query[1000][100];
bitset<100> occured;
map<string,int> M;
int main()
{
	map<string,int> M;
	int N,S,Q;
	scanf("%d",&N);
	int cas = 1;
	while(N--)
	{
		scanf("%d",&S);
		getchar();
		REP(i,S)
		{
			gets(engines[i]);
			M[engines[i]] = i;
		}
		occured=0;
		long long res = 0;
		scanf("%d",&Q);
		getchar();
		REP(i,Q)
		{
			gets(query[i]);
			occured.set(M[query[i]]);
			if(occured.count()==S) { res++; occured=0; occured.set(M[query[i]]); }
		}
		cout<<"Case #"<<cas<<": "<<res<<endl;
		cas++;
	}
	return 0;
}
				
