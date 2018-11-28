//A

#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
	//vars
	int T,t;
	int a,i;
	int n,tim,o,b;
	bool press;
	char ch[105];
	int num[105];
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d",&n);
				for (a=0; a<n; a++)
					scanf(" %c %d",&ch[a],&num[a]);
			//simulate
			a=tim=0;
			o=b=1;
				while (a<n)
				{
					press=0;
					//move O
					for (i=a; i<n; i++)
						if (ch[i]=='O')
						{
								if (num[i]>o)
									o++;
								else
								if (num[i]<o)
									o--;
								else
								if (a==i)
									press=1;
							break;
						}
					//move B
					for (i=a; i<n; i++)
						if (ch[i]=='B')
						{
								if (num[i]>b)
									b++;
								else
								if (num[i]<b)
									b--;
								else
								if (a==i)
									press=1;
							break;
						}
					//press button?
						if (press)
							a++;
					tim++;
				}
			//output
			printf("Case #%d: %d\n",t,tim);
		}
	return(0);
}