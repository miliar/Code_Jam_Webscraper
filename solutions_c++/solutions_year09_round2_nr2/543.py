#include "iostream"
#include "algorithm"
#include "cstring"
#include "string"
#include "stack"
#include "queue"
#include "set"
#define N 101
#define M 101
using namespace std;
char a[N];
int t;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d\n",&t);
	for(int ncase=1;ncase<=t;ncase++)
	{
		int i,j,l;
		gets(a+1);
		a[0]='0';
		l=strlen(a);
		next_permutation(a,a+l);
		printf("Case #%d: ",ncase);
		i=0;
		while(a[i]=='0')
			i++;
		while(a[i]!='\0')
		{
			putchar(a[i++]);
		}
		putchar('\n');
	}
	return 0;
}