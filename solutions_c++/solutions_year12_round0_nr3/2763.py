//Besm Allah

#include<iostream>
using namespace std;

int main(){
	int T,cas=0;
	cin>>T;
	while(T--){
		cas++;
		int a,b;
		int ans=0;
		cin>>a>>b;
		int arr[20];
		int cnt = 0;
		for(int i  = a ; i<=b ; i++){
			int x = i;
			cnt = 0;
			//if(x%10 == 0)
			//	continue;
			int cx = x;
			int power = 1;
			while(x){
				power*=10;
				x/=10;
			}
			power/=10;
			x=cx;
			while(x){
				int digit = x % 10;
				x/=10;
				cx/=10;
				cx+=digit * power;
				if(digit != 0 && cx > i && cx >= a && cx <= b){
					bool mark=false;
					for(int j = 0 ; j < cnt ; j++){
						if(arr[j] == cx)
							mark =true;
					}
					if(!mark){
					arr[cnt++] = cx;
					ans++;	
					}
				}
			}
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
}
