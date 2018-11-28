#include<iostream>
#include<algorithm>
using namespace std;
const int MAXN=110;
int na,nb,t,ca[MAXN][MAXN],cb[MAXN][MAXN],ansa,ansb;
struct tim 
{
	int h;
	int m;
};
struct huo
{
		tim s;
		tim e;
}a[MAXN],b[MAXN];
bool operator <(tim x,tim y)
{
	if(x.h<y.h)return true;
	if(x.h==y.h&&x.m<y.m)return true;
	return false;
};
bool operator <=(tim x,tim y)
{
	if(x.h<y.h)return true;
	if(x.h==y.h&&x.m<=y.m)return true;
	return false;
};
tim operator +(tim x,int k)
{
	x.m+=k;
	if(x.m>=60)x.m-=60,x.h++;
	return x;
}
bool cmp(huo x,huo y){return x.s<y.s;}
void input()
{
	int i,j;
	tim k;
	char tmp[10];
	scanf("%d%d%d",&t,&na,&nb);
	for(i=0;i<na;++i)
	{
		scanf("%s",tmp);
		a[i].s.h=(tmp[0]-'0')*10+tmp[1]-'0';
		a[i].s.m=(tmp[3]-'0')*10+tmp[4]-'0';
		scanf("%s",tmp);
		a[i].e.h=(tmp[0]-'0')*10+tmp[1]-'0';
		a[i].e.m=(tmp[3]-'0')*10+tmp[4]-'0';

	}
	sort(a,a+na,cmp);
	for(i=0;i<nb;++i)
	{
		scanf("%s",tmp);
		b[i].s.h=(tmp[0]-'0')*10+tmp[1]-'0';
		b[i].s.m=(tmp[3]-'0')*10+tmp[4]-'0';
		scanf("%s",tmp);
		b[i].e.h=(tmp[0]-'0')*10+tmp[1]-'0';
		b[i].e.m=(tmp[3]-'0')*10+tmp[4]-'0';
	}
	sort(b,b+nb,cmp);
//	for(i=0;i<na;++i)printf("%d %d:%d-%d:%d\n",i,a[i].s.h,a[i].s.m,a[i].e.h,a[i].e.m);
//	printf("\n");
//	for(i=0;i<nb;++i)printf("%d %d:%d-%d:%d\n",i,b[i].s.h,b[i].s.m,b[i].e.h,b[i].e.m);
	memset(ca,0,sizeof(ca));
	memset(cb,0,sizeof(cb));
	for(i=0;i<na;++i)
	{
		for(j=0;j<nb;++j)
		{
			k=a[i].e+t;
			if(k<=b[j].s)
			{
				ca[i][++ca[i][0]]=j;
			}
			k=b[j].e+t;
			if(k<=a[i].s)
			{
				cb[j][++cb[j][0]]=i;
			}
		}
	}
}
void deal()
{
	int sa=0,sb=0,k,flag=0,p,j;
	bool va[MAXN],vb[MAXN];
    memset(va,0,sizeof(va));
	memset(vb,0,sizeof(vb));
	ansa=ansb=0;
	while(sa<na&&sb<nb)
	{
		if(a[sa].s<b[sb].s)
		{
			va[sa]=1;
			ansa++;
			k=ca[sa][0];
			p=sa;
			flag=0;
		//	printf("%c:%d\n",flag?'b':'a',p);
			while(k!=0)
			{
				flag^=1;
				if(flag)
				{
					for(j=1;j<=k;++j)
					{
						if(vb[ca[p][j]]==0)
						{
							p=ca[p][j],vb[p]=1;	
							break;
						}
					}
					if(j>k)break;
					k=cb[p][0];
				}
				else  
				{
					
						for(j=1;j<=k;++j)
						if(va[cb[p][j]]==0)
						{
							p=cb[p][j],va[p]=1;break;
						}
				
					if(j>k)break;
					k=ca[p][0];
				}
			//	printf("%c:%d\n",flag?'b':'a',p);
			}
		}
		else
		{
			vb[sb]=1;
			ansb++;
			k=cb[sb][0];
			p=sb;
			flag=1;
		//	printf("%c:%d\n",flag?'b':'a',p);
			while(k!=0)
			{
				flag^=1;
				if(flag)
				{
					for(j=1;j<=k;++j)
					{
						if(vb[ca[p][j]]==0)
						{
							p=ca[p][j],vb[p]=1;break;
						}
					}
					if(j>k)break;
					k=cb[p][0];
				}
				else  
				{
					
					for(j=1;j<=k;++j)
					{
						if(va[cb[p][j]]==0)
						{
							p=cb[p][j],va[p]=1;break;
						}
					}
					if(j>k)break;
					k=ca[p][0];
				}
				//printf("%c:%d\n",flag?'b':'a',p);
			}
		//	printf("\n");
		}
		while(sa<na&&va[sa]==1)sa++;
		while(sb<nb&&vb[sb]==1)sb++;
	}
	while(sa<na)if(va[sa++]==0)ansa++;
	while(sb<nb)if(vb[sb++]==0)ansb++;
}
int main()
{
	int t,p=0;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	for(scanf("%d",&t);t--;printf("Case #%d: %d %d\n",++p,ansa,ansb))
	{
		input();
		deal();
	}
	return 0;
}