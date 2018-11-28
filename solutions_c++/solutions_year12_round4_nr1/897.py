#include <stdio.h>
int n,su[100001][2],m,tbl[100001];
bool check(){
	int i,j;
	for(i=0;i<n;i++)
		tbl[i]=0;
	tbl[0]=su[0][0];
	for(i=0;i<n;i++){
		if(tbl[i]!=0){
			if(tbl[i]>su[i][1])
				tbl[i]=su[i][1];
			if(tbl[i]+su[i][0]>=m) return true;
			for(j=i+1;j<n;j++){
				if(su[i][0]+tbl[i]>=su[j][0] && tbl[j]<su[j][0]-su[i][0])
					tbl[j]=su[j][0]-su[i][0];
			}
		}
	}
	return false;
}
int main(){
	int testt,i,test;
	FILE *in,*out;
	in=fopen("input.txt","r");
	fscanf(in,"%d",&testt);
	out=fopen("output.txt","w");
	for(test=1;test<=testt;test++){
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++){
			fscanf(in,"%d %d",&su[i][0],&su[i][1]);
		}
		fscanf(in,"%d",&m);
		if(check())
			fprintf(out,"Case #%d: YES\n",test);
		else
			fprintf(out,"Case #%d: NO\n",test);
	}
	fcloseall();
	return 0;
}
