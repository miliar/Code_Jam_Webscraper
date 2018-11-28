#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
struct node
{
	int smin,ssec;
	int emin,esec;
};
bool cmp(node a,node b)
{
	return a.smin<b.smin || (a.smin == b.smin &&a.ssec < b.ssec);
}
bool cmp2(node a,node b)
{
	return a.emin<b.emin || (a.emin == b.emin &&a.esec < b.esec);
}

int wt,na,nb;
node ta[102],tb[102];
int ansa,ansb;
int tcmp(node a,node b)
{
	b.esec += wt;
	if(b.esec >=60)
	{
		b.esec = b.esec%60;
		b.emin ++;
	}
	if(a.smin > b.emin)
		return 1;
	if(a.smin == b.emin &&a.ssec>=b.esec)
		return 1;
	return 0;
}
void solve()
{
	int i,j;	
	sort(ta,ta+na,cmp);
	sort(tb,tb+nb,cmp2);
	ansa = 0;
	int cntb = 0;
	for(j=0,i=0;i<na;i++)
	{
		while(j<nb&&tcmp(ta[i],tb[j])>0)
		{
			j++;
			cntb ++;
		}
	//	cout<<i<< " "<<ta[i].smin <<" "<<ta[i].ssec<<" "<<ta[i].emin<<" "<<ta[i].esec<<" "<<j<<" "<<cntb<<endl;
		if(cntb >0)
			cntb --;
		else
			ansa ++;
	}
	int cnta =0 ;
	sort(ta,ta+na,cmp2);
	sort(tb,tb+nb,cmp);
	for(j=0,i=0;i<nb;i++)
	{
		while(j<na&&tcmp(tb[i],ta[j])>0)
		{
			j++;
			cnta ++;
		}
		if(cnta >0)
			cnta --;
		else
			ansb ++;
	}
	return;
}
int main()
{
	//freopen("a.txt","r",stdin);
	//freopen("a.out","w",stdout);
	int ii,i,cas;
	char st[100],end[100];
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d",&wt);
		scanf("%d%d",&na,&nb);
		for(i=0;i<na;i++)
		{
			scanf("%s%s",st,end);
			ta[i].smin = (st[0]-'0')*10+ st[1]-'0';
			ta[i].ssec = (st[3]-'0')*10+ st[4]-'0';
			ta[i].emin = (end[0]-'0')*10+ end[1]-'0';
			ta[i].esec = (end[3]-'0')*10+ end[4]-'0';
		}
		for(i=0;i<nb;i++)
		{
			scanf("%s%s",st,end);
			tb[i].smin = (st[0]-'0')*10+ st[1]-'0';
			tb[i].ssec = (st[3]-'0')*10+ st[4]-'0';
			tb[i].emin = (end[0]-'0')*10+ end[1]-'0';
			tb[i].esec = (end[3]-'0')*10+ end[4]-'0';
		}
		ansa = 0; ansb=0;
		solve();
		printf("Case #%d: %d %d\n",ii,ansa,ansb);
	}
	return 0;
}