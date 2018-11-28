//Besm Allah

#include<iostream>
#include<algorithm>
using namespace std;

int arr[1000];
int ans;

int unsurp(int x){
	int aa = x/3;
	if(x%3 !=0){
		aa++;
	}
	return aa;
}
int surp(int x){
	int aa  = x/3;
	aa++;
	if(x%3==2)
		aa++;
	return aa;

}
bool mark[1000];

int main(){
	int T;int cas = 0;
	cin>>T;
	while(T--){
		cas++;
		int n,s,p;
		cin>>n>>s>>p;
		for(int i = 0 ; i < n ; i++){
			cin>>arr[i];
		}
		ans = 0;
		int cnt = 0;
		for(int i = 0 ; i < n  && cnt < s; i++){
			if(arr[i]<= 28 && arr[i]>=2){
				if(surp(arr[i]) >= p && unsurp(arr[i])<p){
					cnt++;
					mark[i]=1;
				}
			}
		}
		for(int i = 0 ; i < n && cnt < s; i++){
			if(arr[i]<=28 && arr[i]>=2 && mark[i] == 0){
				mark[i] = 1;
				cnt++;
			}
		}
		for(int i = 0 ; i < n  ; i ++){
			if(mark[i]){
				if(surp(arr[i])>=p){
					ans++;
				}
			}else{
				if(unsurp(arr[i])>=p){
					ans++;
				}
			}
			

		}
		for(int i = 0 ; i < n ; i++)
			mark[i]=0;
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
}
