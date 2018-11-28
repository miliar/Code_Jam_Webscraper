#include <iostream>

using namespace std;

int c[505][505];
int d[505][505];
int t,n;
int main(){
	int sss = 50;
	for(int i=0;i<sss;i++)
		c[0][i] = 0;
	c[0][0] = 1;
	for(int i=1;i<sss;i++)
		for(int j=0;j<sss;j++)
			c[i][j] = c[i-1][j] + ((j>0)?c[i-1][j-1]:0);
	for(int i=0;i<sss;i++)
		for(int j=0;j<sss;j++)
			d[i][j] = 0;
	//printf("%d\n",c[3][2]);
	cin >> t;
	d[2][1] = 1;
	for(n=3;n<sss;n++){ //each n
		d[n][1]=1;
		for(int i=2;i<n;i++){ //set size
			d[n][i] = 1;
			for(int j=1;j<=i-2 &&  n-i>0;j++){
				d[n][i] += d[i][i-j-1]*c[n-i-1][j];
			}
		}
	}
	
	for(int f=1;f<=t;f++){
		cin >> n;
		/*
		int cnt = 1;
		d[1][0]= 1;
		for(int i=2;i<n;i++){ //set size
			for(int j=0;j<=i-2 &&  n-i>0;j++){
				d[i][j] += d[c[n-i-1][j];
			}
				//printf("!!!set:%d total:%d\n",i,ccc);
			cnt+=ccc;
		}
		*/
		int cnt = 1;
		for(int i=2;i<n;i++)
			cnt += d[n][i];
		printf("Case #%d: %d\n",f,cnt%100003);
	}
	return 0;
}
