/*
Author		:taser ghar
Algorithm	:	
Complexity	:	
Problem		:
Comments	:balir badh amar venge gele hai , taser ghar jeno hoibe shohai
LightOJ		:)
*/
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define inf 987654321
#define pi (2*acos(0.0))
#define eps 1e-7
using namespace std;

char A[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char B[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char C[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
char D[]="our language is impossible to understand";
char E[]="there are twenty six factorial possibilities";
char F[]="so it is okay if you want to just give up";
char str[300];
char S[300];
void init(){
	int ln, i, a;
	ln = strlen( A );
	str['z'] = 'q';
	str['a'] = 'y';
	str['o'] = 'e';
	str['q'] = 'z';
	for( i= 0 ; i < ln; i++){
		a = A[i];
		str[a]=D[i];
	}

	ln = strlen( B );
	for( i= 0 ; i < ln; i++){
		a = B[i];
		str[a]=E[i];
	}

	ln = strlen( C );
	for( i= 0 ; i < ln; i++){
		a = C[i];
		str[a]=F[i];
	}
}
int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A.out","w",stdout);
	init();
	int kase, ct  =1, ln, i, a;
	scanf("%d", &kase);
	getchar();
	while(kase--){
		gets(S);
		ln = strlen( S );
		printf("Case #%d: ", ct++);
		for( i= 0 ; i  < ln; i++){
			a = S[i];
			printf("%c", str[a]);
		}
		printf("\n");
	}
	return 0;


}