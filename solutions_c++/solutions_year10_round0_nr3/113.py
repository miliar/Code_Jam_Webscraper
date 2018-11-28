#include<iostream>
using namespace std;

bool again;
int T,t,R,K,N,i,j,crnt,turn;
int ar[1002];
long long int total,earned;
pair<long long int,int> ride[1002]; //total, next
pair<long long int,int> pertamax[1002]; //total, berapa ride

int main() {
	cin>>T;
	for(t=1;t<=T;t++){
		cin>>R>>K>>N;
		for(i=0;i<N;i++) cin>>ar[i];
		i=0;j=0;
		total=0;
		while(i<N) {
			if(total+ar[j]>K||(j==i&&total>0)) {
				ride[i]=make_pair(total,j);
				total-=ar[i];
				i++;
			}
			else {
				total+=ar[j];
				j=(j+1)%N;
			}
		}
		for(i=0;i<N;i++) pertamax[i]=make_pair(-1,-1);
		again=true;
		crnt=0;
		total=0;
		turn=0;
		while(R>0&&again) {
			if(pertamax[crnt].first==-1) {
				pertamax[crnt]=make_pair(total,R);
				total+=ride[crnt].first;
				R--;
				crnt=ride[crnt].second;
			}
			else {
				again=false;
				earned=total-pertamax[crnt].first;
				turn=pertamax[crnt].second-R;
			}
		}
		if(R>0) {
			total=total+(R/turn)*earned;
			R%=turn;
		}
		while(R>0) {
			total+=ride[crnt].first;
			R--;
			crnt=ride[crnt].second;
		}
		cout<<"Case #"<<t<<": "<<total<<endl;
	}
}
