#include<iostream>
#include<algorithm>

using namespace std;

#define N 105
int tc,ans;
int n,m;
int data[N],table[N][N];
int main(){
	int i,j,k,mink;
	FILE *in=fopen("in.txt","r");
	FILE *out=fopen("out.txt","w");

	fscanf(in,"%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		fscanf(in,"%d %d",&m,&n);
		for(i=1;i<=n;i++)
			fscanf(in,"%d",&data[i]);
		data[0]=0;
		data[++n]=m+1;
		for(i=2;i<=n;i++){ 
			for(j=0;j<=n-i;j++){
				table[j][j+i]=data[j+i]-data[j]-2;
				mink=-1;
				for(k=j+1;k<j+i;k++){
					if (mink==-1 || mink>table[j][k]+table[k][j+i])
						mink=table[j][k]+table[k][j+i];
				}
				if (mink!=-1) table[j][j+i]+=mink;
			}
		}
		fprintf(out,"Case #%d: %d\n",tcc,table[0][n]);
	}
	return 0;
}