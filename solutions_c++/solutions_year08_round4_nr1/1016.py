#include<stdio.h>

int min(int aa, int bb)
{
	if(aa<bb)
		return aa;
	return bb;
}

int c[1111], a[1111], val[1111], cst[1111][5], m1, m;
int getval(int i)
{
	if(i>m1)
		return val[i];
	int x=getval(i*2);
	int y=getval(i*2+1);
	if(a[i]==1)
	{
		val[i]=x&y;
		cst[i][val[i]]=0;
		if(val[i]==1 && c[i]==0)
		{
			cst[i][1-val[i]]=min( cst[i*2][0]+cst[i*2+1][0] ,  min(cst[i*2][1]+cst[i*2+1][0] , cst[i*2][0]+cst[i*2+1][1] ));
		}
		else if(val[i]==1 && c[i])
		{
			cst[i][0]=cst[i*2][0]+cst[i*2+1][0];
		}
		if(val[i]==0 && c[i])
		{
			cst[i][1-val[i]]=min( cst[i*2][1]+cst[i*2+1][1] ,  min(cst[i*2][1]+cst[i*2+1][0] , cst[i*2][0]+cst[i*2+1][1] )+1);
		}
		else if(val[i]==0 && c[i]==0)
		{
			cst[i][1]=cst[i*2][1]+cst[i*2+1][1];
		}
	}
	else
	{
		val[i]= x|y;
		cst[i][val[i]]=0;
		
		if(val[i]==1 && c[i])
		{
			cst[i][1-val[i]]=min( cst[i*2][0]+cst[i*2+1][0] ,  min(cst[i*2][1]+cst[i*2+1][0] , cst[i*2][0]+cst[i*2+1][1] )+1);
		}
		else if(val[i]==1 && c[i]==0)
		{
			cst[i][0]=cst[i*2][0]+cst[i*2+1][0];
		}
		if(val[i]==0 && c[i]==0)
		{
			cst[i][1-val[i]]=min( cst[i*2][1]+cst[i*2+1][1] ,  min(cst[i*2][1]+cst[i*2+1][0] , cst[i*2][0]+cst[i*2+1][1] ));
		}
		else if(val[i]==0 && c[i])
		{
			cst[i][1]=cst[i*2][1]+cst[i*2+1][1];
		}
	}
	cst[i][val[i]]=0;
	return val[i];

}


int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("aa.ans", "w", stdout);
	int i, fl, t, test, v,res;
	scanf("%d", &test);
	for(t=1; t<=test; t++)
	{
		fl=1;
		scanf("%d %d", &m, &v);
		
		for(i=1; i<=m; i++)
		{
			cst[i][0]=cst[i][1]=222222222;
		}
		m1=(m-1)/2;
		for(i=1; i<=m1;i++)
			scanf("%d %d", &a[i], &c[i]);
		for(i=i; i<=m; i++)
		{
			scanf("%d", &val[i]);
			cst[i][val[i]]=0;
		}
		res=getval(1);

	
	
		res=cst[1][v];

		if(res<222222222)
		printf("Case #%d: %d\n", t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}