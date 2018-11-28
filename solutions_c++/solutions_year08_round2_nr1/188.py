#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long n,A,B,C,D,x0,Y0,M;
long long tabla[3][3]; 

long long comb3(long long n){
	return (n*(n-1)*(n-2))/6;
}

int main(){
	int casos,i,j,c;
	
	cin>>casos;
	for (c=1;c<=casos;c++){
		cin>>n>>A>>B>>C>>D>>x0>>Y0>>M;
		memset(tabla,0,sizeof(tabla));
		
		long long X=x0, Y=Y0;
		
		tabla[X%3][Y%3]++;
		for (i=1;i<n;i++){
			X=(A * X + B)%M;
			Y=(C * Y + D)%M;
			tabla[X%3][Y%3]++;
		}
		long long rta=0;
		
		for (i=0;i<3;i++) for (j=0;j<3;j++) rta+=comb3(tabla[i][j]);
		
		for (i=0;i<3;i++){
			long long tmp1=1,tmp2=1;
			
			for (j=0;j<3;j++){
				tmp1*=tabla[i][j];
				tmp2*=tabla[j][i];
			}
			rta+=tmp1+tmp2;
		}
		vector<int> p(3);
		
		for (i=0;i<3;i++) p[i]=i;
		do{
			long long tmp=1;
			
			for (i=0;i<3;i++) tmp*=tabla[i][p[i]];
			rta+=tmp;
		}while (next_permutation(p.begin(),p.end()));
		cout<<"Case #"<<c<<": "<<rta<<endl;
	}
	return 0;
}
