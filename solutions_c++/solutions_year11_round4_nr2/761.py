#include<iostream>
using namespace std;
#define eps 1e-6
int _node[11][11];
int sgn(const double &t)
{
	return t>eps?1:(t<-eps?-1:0);
}
char str[1000];
int main()
{
	int r,c,si,sj,i,j,k,d,cas,i1,j1;
	double x,y,ansx,ansy,tmp;
	bool flag;
	//freopen("1.txt","r",stdin);
	//freopen("B-s.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;i++)
		{
			scanf("%s",str);
			for(j=0;j<c;j++)
				_node[i][j]=str[j]-'0'+d;
		}
		flag=false;
		for(k=min(r,c);k>=3;k--)
		{
			tmp=1.0*(k-1)/2;
			for(si=0;si<r;si++)
				if(si+k<=r)
					for(sj=0;sj<c;sj++)
						if(sj+k<=c)
						{
							//x=si+1.0*(k-1)/2;y=sj+1.0*(k-1)/2;
							x=si+tmp;y=sj+tmp;
							ansx=ansy=0;
							for(i1=0;i1<k;i1++)
								for(j1=0;j1<k;j1++)
								{
									if(i1==0&&j1==0)
										continue;
									if(i1==0&&j1==k-1)
										continue;
									if(i1==k-1&&j1==0)
										continue;
									if(i1==k-1&&j1==k-1)
										continue;
									ansx+=_node[si+i1][sj+j1]*(tmp-i1);ansy+=_node[si+i1][sj+j1]*(tmp-j1);
								}
							if(sgn(ansx)==0&&sgn(ansy)==0)
							{
								flag=true;
								goto A;
							}
						}
		}
A:      if(flag)
			printf("%d\n",k);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}