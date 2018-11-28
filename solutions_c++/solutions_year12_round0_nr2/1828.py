#include<fstream>
#include<algorithm>
#include<cmath>
#define N 102
using namespace std;
int tt;
int t[N],n,p,s;
int main(void){
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	int i,j,d;
	fscanf(in,"%d",&tt);
	for(i=0;i<tt;i++){
		fscanf(in,"%d %d %d",&n,&s,&p);
		p*=3; d=0;
		for(j=0;j<n;j++){
			fscanf(in,"%d",&t[j]);
			if(p-t[j]<=2) d++;
			else if(s>0 && p>3 && p-t[j]<=4){
				d++; s--;
			}
		}
		fprintf(out,"Case #%d: %d\n",i+1,d);
	}
	return 0;

}