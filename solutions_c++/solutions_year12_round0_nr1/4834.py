#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <iostream>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

string s = "yhesocvxduiglbkrztnwjpfmaq";
int T,t,n,i;
char a[111111];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d\n",&T);
	for(t=1;t<=T;t++)
	{
		gets(a);
		n = strlen(a);
		printf("Case #%d: ",t);
		for(i=0;i<n;i++)
			if(a[i]==' ')
				printf(" "); else
				printf("%c",s[a[i]-'a']);
		printf("\n");
	}
	return 0;
}