#include<iostream>
int abs(int t)
{
	return t<0?-t:t;
}
int s2,l1,l2,t,c;
int cal(int x1,int y1,int x2,int y2,int x3,int y3)
{
	return abs(x1*y2-x2*y1+x2*y3-x3*y2+x3*y1-x1*y3);
}
int main()
{
	int cs,css,i,j,ii,jj,iii,jjj,n,m,A;
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d%d",&n,&m,&A);
		for(ii=0;ii<=n;ii++)
			for(iii=0;iii<=n;iii++)
				for(jj=0;jj<=m;jj++)
					for(jjj=0;jjj<=m;jjj++)
					{
						if(cal(0,0,ii,jj,iii,jjj)==A)goto loop;
					}
		loop:printf("Case #%d: ",css);
		if(ii>n)printf("IMPOSSIBLE\n");
		else printf("%d %d %d %d %d %d\n",0,0,ii,jj,iii,jjj);
	}
	return 0;
}
