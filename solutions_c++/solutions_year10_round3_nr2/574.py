#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int l,p,c,mct;
int xx=1<<31;


int main(){
	int zz,zzn,i;
	char s[500];
	for(zzn=1,scanf("%d",&zz);zzn<=zz;zzn++){
		scanf("%d%d%d",&l,&p,&c);
		
		i=l;
		for(mct=0;i<p;mct++)i*=c;
		mct--;
		for(i=32;i;i--){
			if(xx&mct)break;
			mct<<=1;
		}
		
		
		printf("Case #%d: %d\n",zzn,i);
	}
	return 0;
}
