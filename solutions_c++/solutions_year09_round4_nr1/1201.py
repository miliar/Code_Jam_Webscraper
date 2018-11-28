#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
typedef long long LL;
typedef vector<string> vs;
typedef vector<int> vi;

int ntc,n,res,tres,tpos[10],pos[10];
char data[10][10];

int move(){
	int res=0,jar;
	for (int i=0;i<n;i++) tpos[i]=pos[i];
	for (int i=0;i<n;i++)
		for (int j=i;j<n;j++)
			if (tpos[j]==i){
				res+=(j-i);
				for (int k=j-1;k>=i;k--){
					jar=tpos[k+1];
					tpos[k+1]=tpos[k];
					tpos[k]=jar;
				}
			}
	return res;
}

int main(){
	freopen("Asmall.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		scanf("%d",&n);
		res=1000000;
		for (int i=0;i<n;i++) pos[i]=i;
		for (int i=0;i<n;i++)
				scanf("%s",data[i]);
		do{
			bool ok=true;
			for (int i=0;i<n;i++)
				for (int j=i+1;j<n;j++)
					if (data[pos[i]][j]!='0'){
						ok=false;
						break;
					}
			if (ok){
				tres=move();
				if (tres<res) res=tres;
			}
		}while (next_permutation(pos,pos+n));
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}