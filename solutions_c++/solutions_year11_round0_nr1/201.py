#include <iostream>

using namespace std;

int t[2],st[2];
int n,num,now;
char c;


void doing()
{
	scanf("%d",&n);
	t[0]=t[1]=0;
	st[0]=st[1]=1;
	for (int i=0;i<n;i++) 
	{
		scanf(" %c %d",&c,&num);
		if (c=='O') now=1;
			else now=0;
		t[now]=max(t[now]+abs(num-st[now]),t[now^1])+1;
		st[now]=num;
	}
	printf("%d\n",max(t[0],t[1]));
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
