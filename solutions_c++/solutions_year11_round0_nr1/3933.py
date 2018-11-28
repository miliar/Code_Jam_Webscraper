#include <stdio.h>
#include <memory.h>
#define abs(x) ((x)>0?(x):(-1*(x)))
#define max(a,b) ((a)>(b)?(a):(b))
FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

int T,n,anstime;

struct DATA{
	int button;
	char robot;
}data[101];

int main(){
	int i,k;
	int lasto_time, lasto_loc, lastb_time, lastb_loc;
	fscanf(in,"%d",&T);
	for(k=0;k<T;k++){
		fscanf(in,"%d ",&n);
		memset(data,0,sizeof(data));
		anstime = 0;
		lasto_time = lastb_time = 0;
		lasto_loc = lastb_loc = 1;
		for(i=0;i<n;i++){
			fscanf(in,"%c %d ",&data[i].robot, &data[i].button);
			if(data[i].robot=='O'){
				anstime = max(anstime, lasto_time+abs(data[i].button-lasto_loc))+1;
				lasto_time=anstime;
				lasto_loc=data[i].button;
			}else if(data[i].robot=='B'){
				anstime = max(anstime, lastb_time+abs(data[i].button-lastb_loc))+1;
				lastb_time=anstime;
				lastb_loc=data[i].button;
			}
		}
		fprintf(out,"Case #%d: %d\n",k+1,anstime);
	}
	return 0;
}
