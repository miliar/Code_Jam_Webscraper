
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int dad[100*100];

const int di[4]={-1,0,0,1};
const int dk[4]={0,-1,1,0};

int root(int a){
	if(dad[a]<0)return a;
	return dad[a]=root(dad[a]);
}

void connect(int a, int b){
	int aa=root(a);
	int bb=root(b);
	if(aa==bb)return ;
	dad[aa]=bb;
}

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		memset(dad,-1,sizeof(dad));

		int n,m;scanf("%d%d",&n,&m);
		int v[n][m];
		for(int i=0;i<n;i++)for(int k=0;k<m;k++)scanf("%d",v[i]+k);

		for(int i=0;i<n;i++)for(int k=0;k<m;k++){
			int lowest=v[i][k]-1;
			for(int t=0;t<4;t++){
				int ii=i+di[t],kk=k+dk[t];
				if(ii<0 || kk<0 || n<=ii || m<=kk)continue;

				lowest=min(lowest,v[ii][kk]);
			}

			int found=0;
			for(int t=0;found==0 && t<4;t++){
				int ii=i+di[t],kk=k+dk[t];
				if(ii<0 || kk<0 || n<=ii || m<=kk)continue;

				if(v[ii][kk]!=lowest)continue;
				connect(i*100+k,ii*100+kk);

				found=1;
			}
		}

		static int npr=1;
		printf("Case #%d:\n",npr++);

		int nused=0;
		for(int i=0;i<n;i++)for(int k=0;k<m;k++){
			//cout<<"A"<<" i"<<i<<" k"<<k<<endl;
			int rt=root(i*100+k);
			//cout<<"A"<<rt<<endl;
			if(-30<dad[rt] && dad[rt]<0){
				dad[rt]=-1000+nused++;
			}
			printf("%c%c",'a'+(dad[rt]+1000),(k==m-1)?'\n':' ');
			//cout<<"B"<<rt<<endl;
		}
		//cout<<"C"<<endl;
	}
	return 0;
}
