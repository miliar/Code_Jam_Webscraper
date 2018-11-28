#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <memory.h>
#pragma comment(linker,"/STACK:16777216")

using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define N 100000  
const int oo = int(1e6); 
const double pi = acos(-1.0);
const double eps = 1e-7;

typedef long long ll;
typedef __int64 int64;

int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int test,i,j;
	char alph[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char s1[35][110];
	scanf("%d\n",&test);
	for(i=0;i<test;i++)gets(s1[i]);
	for(i=0;i<test;i++)
	{
		for(j=0;j<strlen(s1[i]);j++)
			if(s1[i][j]!=' ')s1[i][j]=alph[s1[i][j]-'a'];
		printf("Case #%d: ",i+1);puts(s1[i]);
	}
	return 0;

}