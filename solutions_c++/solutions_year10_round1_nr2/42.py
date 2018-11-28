#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int abs(int x){
	return x>0 ? x : -x;
}

int eval(){
	int D, I, M, N;
	cin>>D>>I>>M>>N;
	int a[100];
	for(int i=0; i<N; i++)
		cin>>a[i];
	if(N==1)
		return 0;
	if(M==0){
		int res=D*N;
		for(int i=0; i<256; i++){
			int r=0;
			for(int j=0; j<N; j++){
				r+=min(D, abs(i-a[j]));
			}
			if(r<res)
				res=r;
		}
		return res;
	}
	int mc[100][256];
	for(int i=0; i<256; i++)
		mc[0][i]=abs(i-a[0]);
	for(int i=1; i<N; i++){
		for(int j=0; j<256; j++){
			int ch=abs(j-a[i]);
			mc[i][j]=ch+D*i;
			for(int k=i-1; k>=0; k--){
				int del=(i-k-1)*D;
				if(ch+del>=mc[i][j])
					break;
				for(int m=0; m<256; m++){
					int ins=j==m ? 0 : 
					  ((abs(j-m)-1)/M)*I;
					if(ch+del+ins+mc[k][m]<mc[i][j])
						mc[i][j]=ch+del+ins+mc[k][m];
				}
			}
		}
	}
	int res=D*N;
	for(int i=0; i<N; i++){
		for(int j=0; j<256; j++){
			int r=mc[i][j]+D*(N-1-i);
			if(r<res)
				res=r;
		}
	}
	return res;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		cout<<eval()<<endl;
	}
	return 0;
}
