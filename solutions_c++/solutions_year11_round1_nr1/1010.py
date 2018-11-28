#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
typedef long long ll;
using namespace std;
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		ll n,d,g,det=-1;
		cin>>n>>d>>g;
		for(ll i=1;i<=n;i++){
			if(i*d%100==0){
				det=i;
				break;
			}
		}
		printf("Case #%d: ",cas);
		if(det==-1){
			puts("Broken");
			continue;
		}
		bool succ=false;
		for(ll i=det;i<=100000;i++)
			if(i*g%100==0&&i*g>=det*d&&(i*(100-g)>=det*(100-d))){
				succ=true;
				cerr<<i<<"---"<<det<<"\n";
				break;
			}
		puts(succ?"Possible":"Broken");
	}
}
