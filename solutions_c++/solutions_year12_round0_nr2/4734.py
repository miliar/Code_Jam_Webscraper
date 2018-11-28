#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int T,m=0;
	cin>>T;
	while(T--){
		m++;
		int s,p,i,j,num,n;
		cin>>n>>s>>p;
		int score[n];
		for(i=0;i<n;i++){
			cin>>score[i];	
		}
		int ans=0,taken=s;
		for(i=0;i<n;i++){
			num = score[i];
			int q = num / 3;
			int rem = num % 3;
			if(q<p){
				int score_rem=score[i]-p;
				if(score_rem>=0 && score_rem/2 == (p-1)){
					ans++;
					//cout<<score[i]<<" ";
				}else if(score_rem >= 0 && score_rem/2 == (p-2) && taken > 0){
					ans++;
					taken--;
					//cout<<score[i]<<" hell ";
				}
			}else if(q>=p){
				ans++;
				//cout<<score[i]<<" ";
			}
		}
		cout<<"Case #"<<m<<": "<<ans<<endl;

	}
}
