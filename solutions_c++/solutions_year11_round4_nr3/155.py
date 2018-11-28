#include<stdio.h>
#include<math.h>
#define max 1000000
FILE *in=fopen("INPUT.TXT","r");
FILE *out=fopen("OUTPUT.TXT","w");
__int64 n;
int cnt1,cnt2;
int check[max+5];
void input(){
	fscanf(in,"%I64d",&n);
}
void process(){
	int r=(int)sqrt((double)n)+1;
	cnt1=cnt2=0;
	for(__int64 i=2;i*i<=n;i++) check[i]=0;
	for(__int64 i=2;i*i<=n;i++){
		if(check[i]==1) continue;
		for(__int64 j=i+i;j*j<=n;j+=i) check[j]=1;
		if(i<=n){
			cnt1++;
			__int64 p=i;
			while(p<=n){
				cnt2++;
				p*=i;
			}
		}
	}
	if(n>1) cnt2++;
}
void output(int tc){
	fprintf(out,"Case #%d: %d\n",tc,cnt2-cnt1);
}
int main(){
	int t;
	fscanf(in,"%d",&t);
	for(int i=0;i<t;i++){
		input();
		process();
		output(i+1);
	}
	fcloseall();
	return 0;
}
