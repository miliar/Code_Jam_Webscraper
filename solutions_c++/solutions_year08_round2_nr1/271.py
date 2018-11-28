#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;
#define x first
#define y second
#define INF 1000000

vector<pair<long long int,long long int> > p;
long long int n,N,A,B,C,D,x0,yy0,M,i,o,j,k,sol;
long long int maxi(long long int n1){
if(n1>=0) return n1;
else return 0;

}

int main(){
long long int i1,j1,i2,i3,j2,j3,px,py;
vector<vector<long long int> > g;
cin >> N;
for(o=0;o<N;o++){
	cin >> n >> A >> B >> C >> D >> px >> py >> M;

	g.resize(3);
	for(i=0;i<3;i++){
		g[i].resize(3);
		for(j=0;j<3;j++) g[i][j]=0;
	}
	g[px%3][py%3]++;	
	for (i=1;i<n;i++){
		px=(A * px + B)%M;
		py=(C * py + D)%M;
		g[px%3][py%3]++;
	}

/*	for(i=0;i<3;i++){
		for(j=0;j<3;j++) cout << i << "-" << j << "  " << g[i][j]<< endl;
	}*/

	long long int sol=0,cero=0;

	for(i1=0;i1<3;i1++){
	for(i2=0;i2<3;i2++){
	for(i3=0;i3<3;i3++){
	
	for(j1=0;j1<3;j1++){
		for(j2=0;j2<3;j2++){
			for(j3=0;j3<3;j3++){
				if((i1+i2+i3)%3==0 && (j1+j2+j3)%3==0){
//				cout << i1 << j1 << " " << i2 << j2 << " " << i3 << j3;
				  if(i1==i2 && i2 == i3 && j1==j2 && j2 == j3) sol+=maxi(g[i1][j1]*(g[i2][j2]-1)*(g[i3][j3]-2));
				  else if(i1==i2 && j1==j2) sol+=maxi((g[i1][j1])*(g[i2][j2]-1)*(g[i3][j3]));
				  else if(i1==i3 && j1==j3) sol+=maxi((g[i1][j1])*(g[i2][j2])*(g[i3][j3]-1));
				  else if(i2==i3 && j2==j3) sol+=maxi((g[i1][j1])*(g[i2][j2]-1)*(g[i3][j3]));
				  else sol+=maxi((g[i1][j1])*(g[i2][j2])*(g[i3][j3]));
//				  cout << "--->" << sol << " " << max((g[i1][j1])*(g[i2][j2])*(g[i3][j3]),0) << endl;
				  }
			}}
		}}
	}}
			


	cout << "Case #" << o+1 << ": " << sol/6 << endl;




}

}
