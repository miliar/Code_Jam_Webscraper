#include<cstdio>
#include<algorithm>
using namespace std;
struct node
{
	int a,b;
}ea[200],eb[205];
int cmp(node c,node d)
{
	return c.a<d.a;
}
int readtime(char str[])
{
	return ((str[0]-'0')*10+str[1]-'0')*60+(str[3]-'0')*10+(str[4]-'0');
}
bool marka[200],markb[200];
char str1[100],str2[100];
int main()
{
	int t,cc,tt,na,nb,ca,cb,sa,sb,i,cura,curb,curt,ta,tb;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d",&tt);
		scanf("%d%d",&na,&nb);
		for(i=0;i<na;i++)marka[i]=0;
		for(i=0;i<nb;i++)markb[i]=0;
		for(i=0;i<na;i++)
		{
			scanf("%s%s",str1,str2);
			ea[i].a=readtime(str1);
			ea[i].b=readtime(str2);
		}
		for(i=0;i<nb;i++)
		{
			scanf("%s%s",str1,str2);
			eb[i].a=readtime(str1);
			eb[i].b=readtime(str2);
		}
		sort(ea,ea+na,cmp);
		sort(eb,eb+nb,cmp);
		cura=curb=ca=cb=sa=sb=0;
		while(true)
		{
			while(cura<na&&marka[cura])cura++;
			while(curb<nb&&markb[curb])curb++;
			if(cura>=na||curb>=nb)break;
			if(ea[cura].a<eb[curb].a)
			{
				curt=ea[cura].b+tt;
				ta=cura+1;tb=curb;
				marka[cura]=1;ca++;
				while(true)
				{
					while(tb<nb&&(markb[tb]==1||eb[tb].a<curt))
					tb++;
					if(tb==nb)break;
					markb[tb]=1;
					curt=eb[tb].b+tt;
					while(ta<na&&(ea[ta].a<curt||marka[ta]==1))
					ta++;
					if(ta==na)break;
					marka[ta]=1;
					curt=ea[ta].b+tt;
				}
			}
			else
			{
				curt=eb[curb].b+tt;
				ta=cura;tb=curb+1;
				markb[curb]=1;cb++;
				while(true)
				{
					while(ta<na&&(ea[ta].a<curt||marka[ta]==1))
					ta++;
					if(ta==na)break;
					marka[ta]=1;
					curt=ea[ta].b+tt;
					while(tb<nb&&(eb[tb].a<curt||markb[tb]==1))
					tb++;
					if(tb==nb)break;
					markb[tb]=1;
					curt=eb[tb].b+tt;
				}
			}
		}
		while(cura<na)
		{
			if(marka[cura]==0)
			ca++;
			cura++;
		}
		while(curb<nb)
		{
			if(markb[curb]==0)
			cb++;
			curb++;
		}
		printf("Case #%d: %d %d\n",cc,ca,cb);
	}
	return 0;
}
				
					
					








