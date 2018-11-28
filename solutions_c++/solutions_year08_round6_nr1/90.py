#include <iostream>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <stdio.h>
using namespace std;

#define MAX 300

struct gao
{
	int h,w;
	bool f;
}a[1001];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//freopen("lin.txt","r",stdin);
	//freopen("lout.txt","w",stdout);

	int cases,casenum;
	bool ff;
	scanf("%d",&cases);
	for(casenum=1;casenum<=cases;casenum++)
	{
		printf("Case #%d:\n",casenum);


		int n,m,i,j,W,H,wx,wy,hx,hy,pwx,pwy,phx,phy;
		char s[101];
		scanf("%d",&n);
		hx=wx=pwx=phx=1000001;
		hy=wy=pwy=phy=0;
		bool f;

		ff=false;
		for(int ii=0;ii<n;ii++)
		{
			f=true;
			scanf("%d%d",&a[ii].w,&a[ii].h);
			scanf("%s",s);
			if(strcmp(s,"NOT")==0)
			{
				f=false;
				scanf("%s",s);
			}
			if(f)
			{
				if(a[ii].w<wx)
					wx=a[ii].w;
				if(a[ii].w>wy)
					wy=a[ii].w;
				if(a[ii].h<hx)
					hx=a[ii].h;
				if(a[ii].h>hy)
					hy=a[ii].h;
				ff=true;
			}
			a[ii].f=f;
		}

		for(int ii=0;ii<n;ii++)
		{
			if(!a[ii].f)
			{
				if(a[ii].w<=wy&&a[ii].w>=wx)
				{
					if(a[ii].h>phy)
						phy=a[ii].h;
					if(a[ii].h<phx)
						phx=a[ii].h;
				}
				if(a[ii].h<=hy&&a[ii].h>=hx)
				{
					if(a[ii].w>pwy)
						pwy=a[ii].w;
					if(a[ii].w<pwx)
						pwx=a[ii].w;
				}
			}
		}

		if(phx>hx)
			phx=1000001;
		if(phy<hy)
			phy=0;
		if(pwx>wx)
			pwx=1000001;
		if(pwy<wy)
			pwy=0;

		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%d%d",&W,&H);
			if(ff)
			{
				if(W>=wx&&W<=wy&&H>=hx&&H<=hy)
					printf("BIRD\n");
				else if(W>=wx&&W<=wy)
				{
					if(H>phy&&phy>0)
						printf("NOT BIRD\n");
					else if(H<phx&&phx<1000001)
						printf("NOT BIRD\n");
					else
						printf("UNKNOWN\n");
				}
				else if(H>=hx&&H<=hy)
				{
					if(W>pwy&&pwy>0)
						printf("NOT BIRD\n");
					else if(W<pwx&&pwx<1000001)
						printf("NOT BIRD\n");
					else
						printf("UNKNOWN\n");
				}
				else
				{
					if((W>=pwy&&pwy>0))
						printf("NOT BIRD\n");
					else if((H<=phx&&phx<1000001))
						printf("NOT BIRD\n");
					else if((W<=pwx&&pwx<1000001))
						printf("NOT BIRD\n");
					else if((H>=phy&&phy>0))
						printf("NOT BIRD\n");
					else
					{
						for(j=0;j<n;j++)
						{
							if(!a[j].f)
							{
								if(a[j].w>=W&&a[j].h>=H&&a[j].w<wx&&a[j].h<hx)
								{
									printf("NOT BIRD\n");
									break;
								}
								if(a[j].w>=W&&a[j].h<=H&&a[j].w<wx&&a[j].h>hx)
								{
									printf("NOT BIRD\n");
									break;
								}
								if(a[j].w<=W&&a[j].h>=H&&a[j].w>wx&&a[j].h<hx)
								{
									printf("NOT BIRD\n");
									break;
								}
								if(a[j].w<=W&&a[j].h<=H&&a[j].w>wx&&a[j].h>hx)
								{
									printf("NOT BIRD\n");
									break;
								}
							}
						}
						if(j==n)
							printf("UNKNOWN\n");
					}
				}
			}
			else
			{
				for(j=0;j<n;j++)
					if(a[j].w==W&&a[j].h==H)
					{
						printf("NOT BIRD\n");
						break;
					}
				if(j==n)
					printf("UNKNOWN\n");
			}
		}
	}

	return 0;
}
