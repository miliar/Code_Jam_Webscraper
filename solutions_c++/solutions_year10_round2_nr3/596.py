#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int z,n,s;
	cin>> z;
	int mat[600][600],modulo=100003;

	int comb[600][600];
	comb[0][0]=1;
	for(int i=1;i<550;i++){
		comb[i][0]=1;
		for(int j=1;j<i;j++){
			comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%modulo;
		}
		comb[i][i]=1;
	}
/*	
	for(int i=1;i<10;i++){
		cout<<comb[i][0]<<" ";
		for(int j=1;j<i;j++){
			cout<<comb[i][j]<<" ";
		}
		cout<<comb[i][i]<<endl;
	}
*/
	for(int i=2;i<=510;i++){
		mat[i][1]=1;
		for(int j=2;j<i;j++){
			mat[i][j]=0;
			for(int k=j-1;k>=1;k--){
				mat[i][j]=(mat[i][j]+mat[j][k]*comb[i-j-1][j-k-1])%modulo;
			}
//			cout<<mat[i][j]<<" ";
		}
//		cout<<endl;
	}
	
	for(int y=1;y<=z;y++){
		cin >> n;
		s = 0;
		for(int i=1;i<n;i++)
			s=(s+mat[n][i])%modulo;
		cout<< "Case #"<<y<<": "<<s<<endl;
	}
}
