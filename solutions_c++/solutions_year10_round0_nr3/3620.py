#include <iostream>
#include <queue>
using namespace std;

int i,j;
long tests,r,k,n,euro,seats;
int main(){

	freopen("C-small-attempt1.in","r",stdin);
	freopen("RESULT_C_small.out","w",stdout);
	cin>>tests;
	for(j=1;j<=tests;j++){
		cin>>r>>k>>n;
		queue<int>cola;
		for(i=0;i<n;i++){
			int temp;
			cin>>temp;
			cola.push(temp);
		}
		euro=0;
		for(i=0;i<r;i++){
			int ncola=n;
			seats=0;
			while(ncola>0){
				int out=cola.front();
				if(out+seats<=k){
					ncola--;
					seats+=out;
					cola.push(out);
					cola.pop();
				}
				else break;

			}
			euro+=seats;
		}
		cout<<"Case #"<<j<<": "<<euro<<endl;
	}
}
