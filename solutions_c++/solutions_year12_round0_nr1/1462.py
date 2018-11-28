#include <map>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>


using namespace std;

long int temp,i,j,k,T;

#define CASE while(T--)
#define FOR(I,A,B) for(I=A;I<B;I++)
#define REP(i,n) FOR(i,0,n)
#define FORR(I,J,K) for(I=J;I>K;I--)
#define JAM(N) printf("Case #%ld: ",N)
#define INPUT(A) freopen(A,"r",stdin);
#define OUTPUT(A) freopen(A,"w",stdout);

#define EXP 1e-10
#define INF	(int)1e9

#define F first
#define S second


typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef unsigned long long ULL;

#define DEB cout<<"DEB"<<endl;
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%ld",&n)
#define sll(n) 					scanf("%I64d",&n)
#define sf(n) 					scanf("%f",&n)
#define slf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)

int next(){
    char c;int num=0;
    c=getchar_unlocked();
    while(!(c>='0' && c<='9')) c=getchar_unlocked();
    while(c>='0' && c<='9'){
        num=(num<<3)+(num<<1)+c-'0';
        c=getchar_unlocked();
    }
    return num;
}

//main code is here

main()
{
	INPUT("A-small-attempt0.in");
	char a[27]="yhesocvxduiglbkrztnwjpfmaq";
	sl(T);
	j=1;
	getchar();
	CASE
	{
		JAM(j++);
		char x[107]={0};
		gets(x);
		for(i=0;x[i];i++)
		{
			if(x[i]>='a' && x[i]<='z')
				cout<<a[x[i]-'a'];
			else cout<<x[i];
		}
		cout<<endl;
	}
	return 0;
}