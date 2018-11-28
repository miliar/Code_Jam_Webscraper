/// @file
/// @brief	문제: 
///	해결법 : 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<algorithm>
#include<cassert>
#include<cctype>
using namespace std;

#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,n) for (int (i)=0,_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b) for (int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset((x),0,sizeof(x));
#define CLEARA(x) memset(&(x),0,sizeof(x));
#define FILL(x,v) memset((x),(v),sizeof(x));
#define FILLA(x,v) memset(&(x),(v),sizeof(x));

//c++ 0x
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define rFOREACH(it,c) for(auto it=(c).rbegin();it!=(c).rend();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
//const double pi = acos(-1.0);
#define EPS 1e-9

#define PII pair<int,int> 
#define VI vector<int>
#define LL long long
template<typename T> inline T		gcd(T a, T b){if(a>b)swap(a,b);while(a!=0){b%=a;swap(a,b);}return b;}
template<typename T> inline T		lcm(T a, T b){return a/gcd(a,b)*b;}
//int pow(int a,int b){int c=1;while(b--)c*=a;return c;}


#define PROB   "d:\\A-large"
//#define PROB   "d:\\C-large-practice"

int checkWhoWin(char a,char b,char c,char d)
{
	char checker[5]={0,},*ptrT;
	checker[0]=a,checker[1]=b,checker[2]=c,checker[3]=d;
	ptrT= strchr(checker,'T');
	if(ptrT!=NULL)
		*ptrT=(ptrT==checker)?checker[1]:checker[0];
	if(strcmp(checker,"XXXX")==0)return 'X';
	else if(strcmp(checker,"OOOO")==0)return 'O';
	return 0;
}

int main(){
	freopen(PROB ".in","r",stdin);
	freopen(PROB ".out","w",stdout);

	char lines[4][81];

	int T;scanf("%d",&T);
	FOR(t,1,T){
		rep(i,4)scanf("%s",&lines[i]);
		int res=0;
		//Horizontal Check
		rep(r,4)if(res=checkWhoWin(lines[r][0],lines[r][1],lines[r][2],lines[r][3]))
			goto Print;
		//Vertical Check
		rep(c,4)if(res=checkWhoWin(lines[0][c],lines[1][c],lines[2][c],lines[3][c]))
			goto Print;
		//Diagonal Check
		if(res=checkWhoWin(lines[0][0],lines[1][1],lines[2][2],lines[3][3]))
			goto Print;
		if(res=checkWhoWin(lines[0][3],lines[1][2],lines[2][1],lines[3][0]))
			goto Print;
		//Empty Check
		res='D';
		rep(r,4)rep(c,4)if(lines[r][c]=='.')
		{res=0;goto Print;}
Print:
		fprintf(stderr,"Case #%d: \n",t);
		printf("Case #%d: ",t);
		if(res=='X')printf("X won\n");
		else if(res=='O')printf("O won\n");
		else if(res=='D')printf("Draw\n");
		else printf("Game has not completed\n");
	}
	fclose(stdout);
	return 0;
}