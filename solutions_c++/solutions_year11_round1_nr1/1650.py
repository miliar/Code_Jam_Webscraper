#include <iostream>
using namespace std;
int main(){
	int t;
	int pd, pg;
	long long int n;
	long long int n_min;
	cin>> t;
	for(int ii = 0 ; ii < t; ii++){
		cin>>n>>pd>>pg;
		n_min = 1;
		if(pd!=100&&pg==100||pd!=0&&pg==0){
			cout << "Case #"<<ii+1<<": Broken"<<endl;
			continue;
		}
		if(pd==0&&pg!=100){
			cout << "Case #"<<ii+1<<": Possible"<<endl;
			continue;
		}
		while(n_min <= n && (n_min * pd)%100!=0){
			n_min++;
		}
		if(n_min > n){
			cout << "Case #"<<ii+1<<": Broken"<<endl;
			continue;
		}
		bool result = false;
		long long addon = n_min;
		while(n_min <= n && result==false){
			long long int wins = (n_min * pd) / 100;
			while((wins * 100) % pg != 0){
				wins++;
			}
			if(wins*100 / pg >= n_min)	result = true;
			n_min += addon;  
		}
		if(!result){
			cout << "Case #"<<ii+1<<": Broken"<<endl; 
		}
		else {
			cout << "Case #"<<ii+1<<": Possible"<<endl;
		}
	}
}