#include <stdio.h>

int N,S,p;

int t[110];


int solve()
{
	int i,need=0,tol=0;
	for(i=0;i<N;i++)
		if(t[i]%3==1)
		{
			if((t[i]+2)/3>=p)
                 tol++;
		} 
		else if(t[i]%3==2)
		{
            int sc = (t[i]+1)/3;
			if(sc>=p) tol++;
			else if(sc==p-1) 
				need++;
		}
		else 
		{
            int sc = (t[i]+1)/3;
			if(sc>=p) tol++;
			else if(sc==p-1 && t[i]!=0) 
				need++;
		}

		if(need<=S) return need + tol;
		else
			return tol + S;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int ct,caset = 1;
	scanf("%d",&ct);

	while(ct--)
	{
		printf("Case #%d: ",caset++);         
		scanf("%d%d%d",&N,&S,&p);
        int i;
		for(i=0;i<N;i++)
            scanf("%d",&t[i]);
		printf("%d\n",solve());
	}
	return 0;
}