#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 11000;

int f[maxn];


int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,j,k;

	
	string str;
	int nca;
	int N,L,H;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		
		
		cin>>N>>L>>H;
		for(i=0;i<N;i++){
			cin>>f[i];
		}

		for(i=L;i<=H;i++){
			for(j=0;j<N;j++)
			{	
				if( (f[j]%i == 0) || (i%f[j] == 0)){
				
				}else {
					break;
				}
			}
			if( j==N )break;
		}

		
		
		printf("Case #%d: ",cid);
		if( i<=H ){
			cout<<i<<endl;
		}
		else {
			cout<<"NO"<<endl;
		}
		
	}

		
}

/*
4
4
.11.
0.00
01.1
.10.


*/