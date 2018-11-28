#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int n,a[100][100];

int tmp[100][100];

void rotate(){
	int i,j,k;
	for (i=0; i<n; i++){
		for (j=0; j<n; j++)
			tmp[i][j]=a[j][n-1-i];
	}
	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			a[i][j]=tmp[i][j];	
}

int process(){
	int i,j,k;
/*	for (i=0; i<n; i++){ 
		for (j=0; j<n; j++){
			cout<<a[i][j];
		}
		cout<<endl;
	}
	*/
	for (k=n; k>=2; k--){
		for (i=0; i<k; i++){
			for (j=0; j<k; j++){
				if (a[i][j]!=a[k-1-j][k-1-i]) break;
			}
			if (j<k) break;
		}
		if (i==k) break;
	}
	//cout<<k<<endl;
	return k;
}

int main(){
	int i,j,k,t,u,L,s;
	int x[5];
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n;
		if (n<=0) k=0;
		else{
			for (k=0; k<n; k++){
				for (j=0; j<=k; j++){
					i=k-j;
					cin>>a[i][j];
				}
			}
			for (; k<2*n-1; k++){
				for (j=k-n+1; j<n; j++){
					i=k-j;
					cin>>a[i][j];
				}
			}
			if (n==1) k=0;
			else{
				L=0;
				for (k=0; k<4; k++){
					x[k]=process();
					rotate();
				}
				x[4]=x[0];
			//	for (k=0; k<5; k++) cout<<x[k]<<endl;
				s=(3*n-2);
				for (k=0; k<4; k++){
					i=n+(n-1-(x[k]-1))+(n-1-(x[k+1]-1));
	//				cout<<i<<" ";
					s=min(s,i);
				}
		//		cout<<endl;
				k=s*s-n*n;
			}
		}
		cout<<"Case #"<<(u+1)<<": "<<k<<endl;
	}
	return 0;
}

