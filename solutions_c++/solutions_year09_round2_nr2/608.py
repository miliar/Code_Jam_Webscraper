#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
using namespace std;

char s[30],ss[30];
int n;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%s",s);
		n = strlen(s);
		strcpy(ss,s);
		next_permutation(s,s+n);
		if(strcmp(s,ss)<=0)
		{
			for (i = 1 ; i < n ; i++)
				if(s[i]!='0'&&(s[i]<s[0]||s[0]=='0'))
				  swap(s[i],s[0]);
			sort(s+1,s+n);
			n++;
			for (i = n-1 ; i > 1 ; i--)s[i]=s[i-1];
			s[1] = '0';
			s[n]=0;
		}
		printf("Case #%d: %s\n",ca,s);
	}

	return 0;
}
