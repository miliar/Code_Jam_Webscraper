#include<cstdio>
const bool dbg = 0;
const int MAXK = (1<<27);
//const int MAXK = (1<<4);
const int MAXN = 31;
int snap[MAXK];
void bitPrint(int i){
	for(int j=0;j<MAXN;j++)
		printf("%d",(int)(bool)(i&(1<<j)));
	printf("\n");
}
void preprocess(){
	snap[0] = 0;
	for(int i=1;i<MAXK;i++){
		snap[i] = snap[i-1];
		for(int j=0;j<MAXN;j++){
			int b = (1<<j);
			if(snap[i] & b){
				snap[i] ^= b;
				continue;
			}else{
				snap[i] ^= b;
				break;
			}
		}
		if(dbg)bitPrint(snap[i]);
	}
}
void solveCase(int c){
	int n,k;
	scanf("%d%d",&n,&k);
	printf("Case #%d: ",c);
	bool on = true;
	for(int i=0;i<n;i++)
		if(!(snap[k]&(1<<i)))on = false;
	if(on)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main(){
	int cas;
	preprocess();
	scanf("%d",&cas);
	for(int i=0;i<cas;i++)
		solveCase(i+1);
	return 0;
}
