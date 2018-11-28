#include <iostream>
#include <vector>
using namespace std;

#define INFTY 100000000

int main(){
	int N;
	cin>>N;
	for(int t=1; t<=N; t++){
		cout<<"Case #"<<t<<": ";
		int M;
		int V;
		cin>>M>>V;
		int M2=(M-1)/2;
		vector<int> G(M+1);
		vector<int> C(M2+1);
		for(int i=1; i<=M2; i++){
			cin>>G[i]>>C[i];
		}
		for(int i=M2+1; i<=M; i++){
			cin>>G[i];
		}
		if(!V){
			for(int i=1; i<=M; i++){
				G[i]=1-G[i];
			}
		}
		vector<int> Cost(M+1);
		for(int i=M; i>M2; i--){
			Cost[i]=G[i]?0:INFTY;
			for(int i=M2; i>0; i--){
				if(G[i]==1){
					Cost[i]=Cost[2*i]+Cost[2*i+1];
					if(C[i]==1){
						int tmp=1+min(Cost[2*i],Cost[2*i+1]);
						if(tmp<Cost[i]) Cost[i]=tmp;
					}
				}else{
					Cost[i]=min(Cost[2*i],Cost[2*i+1]);
				}
				if(Cost[i]>INFTY){
					Cost[i]=INFTY;
				}
			}
		}
		if(Cost[1]>=INFTY){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<Cost[1]<<endl;
		}
	}
	return 0;
}


