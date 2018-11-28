
#include <cstdio>
#include <fstream>

#define L 505
#define N 19

using namespace std;


FILE *in=fopen("input.txt","r");
FILE *out=fopen("output.txt","w");

char data[L],ptrn[L]="welcome to code jam";
int t[N+5];
int n;

int main(){
	int len,i,j;
	fscanf(in,"%d ",&n);
	for(int tc=1;tc<=n;tc++){
		memset(t,0,sizeof(t));
		t[0]=1;
		fgets(data,L,in);
		len=strlen(data);
		for(i=0;i<len;i++){
			for(j=0;j<N;j++){
				if (ptrn[j]==data[i]){
					t[j+1]+=t[j];
					t[j+1]%=1000;
				}
			}
		}
		fprintf(out,"Case #%d: %04d\n",tc,t[N]);
	}
	return 0;
}