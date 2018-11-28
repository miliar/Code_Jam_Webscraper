#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

int main(int argc,char *argv[])
{
    freopen("TrainTimetable.in", "r", stdin);
    freopen("TrainTimetable.out", "w", stdout);
    
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	printf("Case #%d: ",curCase);
	int tt,na,nb;
	scanf("%d%d%d",&tt,&na,&nb);
	int ad[na+1],aa[nb+1],bd[nb+1],ba[na+1];
	for(int k=0;k<na;k++)
	{
	    int dh,dm,ah,am;
	    scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
	    ad[k]=dh*60+dm,ba[k]=ah*60+am+tt;
	    //printf("%d %d\n",ad[k],ba[k]);
	}
	for(int k=0;k<nb;k++)
	{
	    int dh,dm,ah,am;
	    scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
	    bd[k]=dh*60+dm,aa[k]=ah*60+am+tt;
	    //printf("%d %d\n",bd[k],aa[k]);
	}
	sort(ad,ad+na);
	sort(aa,aa+nb);
	sort(bd,bd+nb);
	sort(ba,ba+na);
	ad[na]=aa[nb]=bd[nb]=ba[na]=24*60;
	int adi=0,bdi=0,aai=0,bai=0;
	int ac=0,bc=0,mxac=0,mxbc=0;
	while(true)
	{
	    int t=min(min(ad[adi],aa[aai]),min(bd[bdi],ba[bai]));
	    //printf("%d %d %d %d \t%d\n",ad[adi],aa[aai],bd[bdi],ba[bai],t);	    
	    if(t==24*60)
		break;
	    if(aa[aai]==t)
		aai++,ac--;	    
	    if(ad[adi]==t)
	    {
		adi++;
		ac++;
		if(ac>mxac)
		    mxac=ac;
	    }
	    if(ba[bai]==t)
		bai++,bc--;
	    if(bd[bdi]==t)
	    {
		bdi++;
		bc++;
		if(bc>mxbc)
		    mxbc=bc;
	    }
	}
	printf("%d %d\n",mxac,mxbc);
    }
    return 0;
}
   
