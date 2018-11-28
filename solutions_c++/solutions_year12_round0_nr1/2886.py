#pragma comment(linker, "/STACK:65777216")
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <queue>
#include <string>
#include <memory.h>
#include <iterator>
#define y1 trololoy1
#define y0 trololoy0
#define mem(A,X) memset(A,X,sizeof(A))
#define memo(A) memset(A,0,sizeof(A))
#define forn(I,B) for (int I=1;I<=(B);I++)
#define forg(H,V) for (int H=first[V];h;h=next[H])
#define rep(I,B) for (int I=0;I<(B);I++) 
#define labs(X) (((X)>0)?(X):(-(X)))
#define ropen(X) freopen(X,"r",stdin)
#define wopen(X) freopen(X,"w",stdout)
#define rwopen(X) freopen(X".in","r",stdin);freopen(X".out","w",stdout)
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define sqr(X) ((X)*(X))

using namespace std;

typedef pair <int,int> pii;
typedef double ld;
typedef long long ll;
typedef pair <ll,ll> pll;
typedef vector<int> vi;
const int N=501;
const int M=20001;
const int INF=111111111;
const double eps=1e-9;
const double pi=3.14159265358979;

int t,n;
char s[N],g[]="yhesocvxduiglbkrztnwjpfmaq";

void solve(int num){
	printf("Case #%d: ",num);
	n=strlen(s);
	rep(i,n) if (s[i]>='a' && s[i]<='z') putchar(g[s[i]-'a']);
		else putchar(s[i]);
	putchar('\n');
}

int main(){
	ropen("input.txt");
	wopen("output.txt");
	scanf("%d\n",&t);
	forn(i,t){
		gets(s);
		solve(i);
	}
	return 0;
}