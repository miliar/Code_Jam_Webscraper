#include <cstdio>
#define mx 110
int bl[mx],orng[mx],tn[mx];
char tc[mx],lin[3];
int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	int t,cas,n,o,b,i,ib,jo,sec,orcur,blcur,turn,fl;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		o = b = 0;
		for(i=0;i<n;i++){
			scanf("%s %d",lin,&tn[i]);
			tc[i] = lin[0];
			if(tc[i]=='B')bl[b++] = tn[i];
			else orng[o++] = tn[i];
		}
		sec = 0;
		orcur = blcur = 1;
		turn = 0;
		ib = jo = 0;
		while(turn<n){
			if(tc[turn]=='O' && tn[turn]==orcur && orcur==orng[jo]){jo++;turn++;fl = 1;}//sec++;continue;}
			else if(orng[jo]<orcur){orcur = ((orcur==1)?100:orcur-1);}
			else if(orng[jo]>orcur){orcur = ((orcur==100)?1:orcur+1);}
			
			if(tc[turn]=='B' && tn[turn]==blcur && blcur==bl[ib] && !fl){ib++;turn++;}//sec++;continue;}
			else if(bl[ib]<blcur){blcur = ((blcur==1)?100:blcur-1);}
			else if(bl[ib]>blcur){blcur = ((blcur==100)?1:blcur+1);}
			fl = 0;
			sec++;
		}
		printf("Case #%d: %d\n",cas,sec);
	}
	return 0;
}