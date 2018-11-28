#include <iostream>
#include <cstring>
using namespace std;

int T;
int N,K;
bool elec[31];
bool status[31];

int main(void){
	freopen("small.in","r",stdin);
    freopen("small.out","w",stdout);
	cin>>T;
	int count=1;
	while(T--){
		cin>>N>>K;
		memset(elec,0,sizeof(elec));
		memset(status,0,sizeof(status));
		elec[1]=true;
		for(int i=1;i<=K;i++){
			for(int j=1;j<=N;j++){
				if(elec[j]==1){
					status[j]=!status[j];
				}
				if(j>1){
					if(elec[j-1]==1&&status[j-1]==1){
						elec[j]=true;
					}
					else{
						elec[j]=false;
					}
				}
			}
		}
		if(elec[N]==1&&status[N]==1)
			cout<<"Case #"<<count++<<": ON"<<endl;
		else
			cout<<"Case #"<<count++<<": OFF"<<endl;

	}
	return 0;
}