

#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------

#define INF  (1<<30)
#define EPS  1e-10
#define pb   push_back
#define sz   size()
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLEAR(A,N)  (memset(A,0,(N)*sizeof(A[0])))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))

template<class Type>
Type Maximum(Type a,Type b){
	return (a>b)?a:b;
}
template<class Type>
Type Maximum(Type a,Type b,Type c){
	Type t=(a>b)?a:b;
	return (c>t)?c:t;
}
template<class Type>
Type Minimum(Type a,Type b){
	return (a<b)?a:b;
}
template<class Type>
Type Minimum(Type a,Type b,Type c){
	Type t=(a<b)?a:b;
	return (c<t)?c:t;
}
//--------------------------------------------------------
char str[502],wel[100]="welcome to code jam";
int memo[503][30],l2=strlen(wel),l1;
void reset(){

	SET(memo);
}

int lcs(int i,int j){

	if(j>=l2) return 1;
	if(i>=l1) return 0;
	if(memo[i][j]>-1) return memo[i][j];
	int r=0;
	if(str[i]==wel[j]) 
		r=lcs(i+1,j+1);
	return memo[i][j]=(r+lcs(i+1,j))%10000;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
		int t,cas=1;
		scanf("%d",&t);
		gets(str);
		while(t--)
		{
			gets(str);
			l1=strlen(str);
			reset();
			printf("Case #%d: ",cas++);
			printf("%04d\n",lcs(0,0));
		
		}
	return 0;
}
