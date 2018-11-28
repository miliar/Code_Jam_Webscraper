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

short int val[5005];
int k,n;

int main(){
	int casos,i,c;
	
	cin>>casos;
	for (c=0;c<=casos;c++){
		cin>>k>>n;
		vector<int> rta(n);
		
		for (i=0;i<n;i++){
			cin>>rta[i];
			rta[i]--;
		}
		memset(val,0,sizeof(val));
		int pos=0,turno;
		for (turno=1;turno<=k;turno++){
			int falta=turno-1;
			while (falta){
				if (!val[pos]){
					falta--;
				}
				pos=(pos+1)%k;
			}
			while (val[pos]){
				pos=(pos+1)%k;
			}
			val[pos]=turno;
		}
		cout<<"Case #"<<c<<":";
		for (i=0;i<n;i++) cout<<" "<<val[rta[i]];
		cout<<endl;
		
	}
	
	return 0;
}
