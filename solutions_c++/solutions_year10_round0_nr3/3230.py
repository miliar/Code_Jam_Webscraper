#include<iostream>
#include<queue>

using namespace std;

queue<int> Q;
int R,K,N;

long double Solve(){
	int k,numb=0,time=0;
	long int size=0;
	long double sum=0;

	while(!Q.empty() && time<R){
		if(numb==N){
			sum+=size;
			size=0;
			numb=0;
			time++;
		}

		else{
			k=Q.front();
		
			if(size+k>K){
				sum+=size;
				size=k;
				numb=1;
				time++;
			}

			else{
				size+=k;
				numb++;
			}
			Q.pop();
			Q.push(k);
		}
	}

	while(!Q.empty())Q.pop();
return sum;
}

int main(){
	int T,a;
	cin>>T;

	for(int i=1; i<=T; i++){
		cin>>R>>K>>N;
		
		for(int j=1; j<=N; j++){
			cin>>a;
			Q.push(a);
		}
		cout<<"Case #"<<i<<": "<<Solve()<<endl;
	}
	return 0;
}