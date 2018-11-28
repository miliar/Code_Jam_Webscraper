#include <iostream>
using namespace std;

typedef long long ll;
int groups[1005];

int main(){
	int tt,t,r,k,n,i,j;
	FILE *fin = /*stdin;//*/ fopen("C-small-attempt0.in","r");
	FILE *fout =  fopen("QC.out","w");
	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		fscanf(fin,"%d %d %d",&r,&k,&n);
		for(i = 0; i < n; i++)
		{
			fscanf(fin,"%d",groups+i);
		}

		int index = 0;
		ll ans = 0;
		for(i = 0; i < r; i++){
			int tmp = 0;
			int preIndex = index;
			while(tmp+groups[index] <=  k){
				tmp += groups[index];
				index++;
				if(index==n)
					index = 0;
				if(index == preIndex)break;
			}
			ans +=ll(tmp);
		}
		fprintf(fout,"Case #%d: %I64d\n",tt,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}