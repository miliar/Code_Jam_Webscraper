#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>

#define PB push_back
#define M 100
#define N 100
#define LL long long


using namespace std;

struct ins {
char color;
int button;
int ord_in_org;
};




int main()
{
	int tc,ti;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		int i,j,k,bc,oc,nos=0,noi;
		ins blue[N],orange[N],input[N];
		char ch;
		bc=0;oc=0;
		scanf("%d",&noi);
		
		//printf("%d %d\n",tc,noi);
		for(i=0;i<noi;++i)
		{
			scanf("%c",&ch);//the space
			scanf("%c",&ch);
			scanf("%d",&j);
			//scanf("%c %d",&ch,&j);
			input[i].color=ch;
			input[i].button=j;
			input[i].ord_in_org=i;
		/*	printf("col %c pos %d \n",input[i].color,input[i].button);
			if(ch=='B')
			{
				blue[bc].color=ch;
				blue[bc].button=j;
				blue[bc].ord_in_org=i;
				++bc;
			} else {
				orange[oc].color=ch;
				orange[oc].button=j;
				orange[oc].ord_in_org=i;
				++oc;
			}*/
		}
		int tsblm=0,tsolm=0,bpos=1,opos=1,tr;nos=0;
		for(i=0;i<noi;++i)
		{
		//	printf("col %c pos %d nos %d tsolm %d tsblm %d\n",input[i].color,input[i].button,nos,tsolm,tsblm);
			if(input[i].color=='O')
			{
				tr=input[i].button-opos;
				if(tr<0)
				tr=-tr;
				if(tsolm>=tr)
				{
					tsolm=0;
					tsblm=1;
					nos+=1;
				} else {
					nos+=tr-tsolm+1;
					tsblm+=tr-tsolm+1;
					tsolm=0;
					
					
				}
				opos=input[i].button;
			} else {
				tr=input[i].button-bpos;
				if(tr<0)
				tr=-tr;
				if(tsblm>=tr)
				{
					tsblm=0;
					tsolm=1;
					nos+=1;
				} else {
					nos+=tr-tsblm+1;
					tsolm+=tr-tsblm+1;
					tsblm=0;
					
					
				}
				bpos=input[i].button;
			}
		}
		printf("Case #%d: %d\n",ti,nos);
	}
	return 0;
}
