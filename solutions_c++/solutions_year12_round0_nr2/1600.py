#include<iostream>
#include<algorithm>
#define all(c) c.begin(),c.end()
#define uni(c) c.erase(unique(all(c)),c.end())
#define pb push_back
#include<vector>
#include<string>
#include<map>
using namespace std;
typedef pair<char,char> P;
bool check(int x,int p){
	int minus=max(0,p-1);
	if(x-2*minus>=p){
		return 1;
	}else{
		return 0;
	}
}
bool check2(int x,int p){
	int minus=max(0,p-2);
	if(x-2*minus>=p){
		return 1;
	}else{
		return 0;
	}
}
int main(){
	int q;
	cin>>q;
	int n,t,p;
	int now=1;
	while(now++<=q){
		int a=0,b=0;
		cin>>n>>t>>p;
		for(int i=0;i<n;i++){
			int x;
			cin>>x;
			if(check(x,p)){
				a++;
			}else if(check2(x,p)){
				b++;
			}
		}
		int ans=min(n,min(b,t)+a);
		cout<<"Case #"<<now-1<<": ";
		cout<<ans<<endl;
	}
	return 0;
}