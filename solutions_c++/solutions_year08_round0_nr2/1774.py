#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#define cls(x) x.ad=x.ar=x.br=x.bd=0
using namespace std;
struct node
{
	int h,m;
	int ar,br;
	int ad,bd;
};
vector<node>tm;
vector<node>tb;
bool cmp(node n1,node n2)
{
	if (n1.h==n2.h) return n1.m<n2.m;
	else return n1.h<n2.h;
};
int main()
{
	int i,j,k,na,nb;
	node tmp;
	int la,lb,maxa,maxb;
	int tc,o,t;
	//freopen("gcj_Bx.out","w",stdout);
	scanf("%d",&tc);
	for (o=1;o<=tc;o++)
	{
		tm.clear();
		scanf("%d",&t);
		scanf("%d%d",&na,&nb);
		for(i=0;i<na;i++)
		{
			cls(tmp);
			scanf("%d:%d",&tmp.h,&tmp.m);
			tmp.ad=1;
			tm.push_back(tmp);
			
			cls(tmp);
			scanf("%d:%d",&tmp.h,&tmp.m);
			tmp.m+=t;
			if (tmp.m>=60) 
			{
				tmp.h+=1;
				tmp.m-=60;
			}
			tmp.br=1;
			tm.push_back(tmp);
		}
		for (i=0;i<nb;i++)
		{
			cls(tmp);
			scanf("%d:%d",&tmp.h,&tmp.m);
			tmp.bd=1;
			tm.push_back(tmp);
			
			cls(tmp);
			scanf("%d:%d",&tmp.h,&tmp.m);
			tmp.m+=t;
			if (tmp.m>=60) 
			{
				tmp.h+=1;
				tmp.m-=60;
			}
			tmp.ar=1;
			tm.push_back(tmp);
		}
		sort(tm.begin(),tm.end(),cmp);
		tb.clear();
		tb.push_back(tm[0]);
		for (i=1;i<tm.size();i++)
		{
			if (tm[i].h==tm[i-1].h&&tm[i].m==tm[i-1].m)
			{
				tb[tb.size()-1].ad+=tm[i].ad;
				tb[tb.size()-1].ar+=tm[i].ar;
				tb[tb.size()-1].bd+=tm[i].bd;
				tb[tb.size()-1].br+=tm[i].br;
			}else tb.push_back(tm[i]);
		}
		maxa=0;
		maxb=0;
		la=0;lb=0;
		for (i=0;i<tb.size();i++)
		{
			node nd=tb[i];
			la+=nd.ar;
			lb+=nd.br;
			la-=nd.ad;
			lb-=nd.bd;
			if (la<0)
			{
				maxa+=-la;
				la=0;
			}
			if (lb<0)
			{
				maxb+=-lb;
				lb=0;
			}
		}
		printf("Case #%d: %d %d\n",o,maxa,maxb);
	}
	//fclose(stdout);
	return 0;
}
