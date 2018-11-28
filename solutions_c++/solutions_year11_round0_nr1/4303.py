#include<stdio.h>
int main()
{
	int t,n,k;
	scanf("%d",&t);
	for(k=0;k<t;k++){
		char bot[101];
		int but[101],Opos[101],Bpos[101],oc=0,bc=0,i,time=0,curPosO=1,curPosB=1,tm;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf(" %c %d",&bot[i],&but[i]);
			if(bot[i]=='O'){
				Opos[oc++]=but[i];
			}
			else	Bpos[bc++]=but[i];
		}
		oc=0;bc=0;
		for(i=0;i<n;i++){
			tm=0;
			if(bot[i]=='O'){
				tm=but[i]>curPosO?but[i]-curPosO+1:curPosO-but[i]+1;
				curPosO=but[i];
				oc++;
				if(curPosB!=Bpos[bc])
				curPosB=Bpos[bc]>curPosB?tm>=(Bpos[bc]-curPosB)?Bpos[bc]:curPosB+tm:tm>=(-Bpos[bc]+curPosB)?Bpos[bc]:curPosB-tm;
			}
			else{
				tm=but[i]>curPosB?but[i]-curPosB+1:curPosB-but[i]+1;
				curPosB=but[i];
				bc++;
				if(curPosO!=Opos[oc])
				curPosO=Opos[oc]>curPosO?tm>=(Opos[oc]-curPosO)?Opos[oc]:curPosO+tm:tm>=(-Opos[oc]+curPosO)?Opos[oc]:curPosO-tm;
			}
			time+=tm;
		}
		printf("Case #%d: %d\n",k+1,time);
	}
	return 0;
}
		
