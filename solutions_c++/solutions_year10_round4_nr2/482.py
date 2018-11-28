#include <iostream>

using namespace std;
const int maxx = 123456789;
int d[2100][13]; // which node, no of miss left
int c[1030];
int m[2100];


int main(){
	int t;
	cin >> t;
	int p;
	int no;
	for(int f=1;f<=t;f++){
		for(int i=0;i<2100;i++)
			for(int j=0;j<13;j++)
				d[i][j]=maxx;
		//printf("!!!\n");
		scanf("%d",&p);
		no = 1 << p;
		for(int i=no;i<no*2;i++){
			scanf("%d",&m[i]);
			for(int j=m[i];j>=0;j--)
				d[i][j] =0;
		}
		for(int i=p-1;i>=0;i--)
			for(int j=1<<i;j<1<<(i+1);j++)
				scanf("%d",&c[j]);
		
		for(int i=no-1;i>=1;i--){
			for(int j=p;j>=0;j--){
				if(d[i][j+1] < d[i][j]) d[i][j] = d[i][j+1];
				if(d[i*2][j]+d[i*2+1][j] + c[i]< d[i][j]) d[i][j] = d[i*2][j]+d[i*2+1][j]+c[i];
				//if(d[i*2][j]+d[i*2+1][j+1] +c[i]< d[i][j]) d[i][j] = d[i*2][j]+d[i*2+1][j+1]+c[i];
				//if(d[i*2][j+1]+d[i*2+1][j] +c[i]< d[i][j]) d[i][j] = d[i*2][j+1]+d[i*2+1][j]+c[i];
				if(d[i*2][j+1]+d[i*2+1][j+1] < d[i][j]) d[i][j] = d[i*2][j+1]+d[i*2+1][j+1];
				//printf("!!!%d %d %d\n",i,j,d[i][j]);
			}
		}
		int ccc = maxx;
		for(int j=p;j>=0;j--) if(d[1][j] < ccc) ccc=d[1][j];
		printf("Case #%d: %d\n",f,ccc);
	}
}
