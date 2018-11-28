#include <iostream>

#define LL long long

using namespace std;

LL gcd(LL a,LL b){return (b==0?a:gcd(b,a%b));}

bool small(LL n,LL pd,LL pg){
	for(LL i=1 ; i<=n ; i++){
		if((i*pd)%100==0){
			LL win = i*pd/100;
			LL lose = i-win;
			cout << lose << endl;
			if(pg==100){
				if(lose==0)return true;
			}
			else if(pg==0){
				if(lose==i)return true;
			}
			else return true;
		}
	}
	return false;
}

int main(){
	int T;cin>>T;
	for(int tt=1 ; tt<=T ; tt++){
		LL N,Pd,Pg;
		cin>>N>>Pd>>Pg;

		LL g = gcd(Pd,100);
		Pd /= g;
		LL und = 100/g;

		bool res = true; 
		if(und<=N){
			LL all = N/und*und;
			LL win = N/und*Pd;
			LL lose = all-win;
			if(lose>0 && Pg==100){
				res = false;
			}
			if(lose<all && Pg==0){
				res = false;
			}
		}
		else{
			res = false;
		}
		//if(small(N,Pd*g,Pg)!=res){
		//	cerr<<"!" << endl;
		//	cerr<<N<<" "<< Pd*g<<" "<<Pg<<endl;
		//}
		printf("Case #%d: %s\n",tt,(res?"Possible":"Broken"));
	}
	return 0;
}
