#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;
#define All(x) x.begin(),x.end()
#define push_back pb

int lcm(int a, int b){
	return (a*b)/__gcd(a,b);
}
int Fre[103];
int N,L,H;
bool FF(int u){
	bool res = true;
	for(int i = 0;i < N && res;i++){
		if(u >= Fre[i]){
			if(u%Fre[i])
			   res=false;
		}
		else if(Fre[i]%u) res = false;
	}
	return res;
}
int main(){
	
	int runs;
	cin>>runs;
	for(int r = 1; r <= runs; r++){

			cin>>N>>H>>L;
               for(int i=0;i<N;i++)
                       cin>>Fre[i];
                       

               bool F=false;
               int res=0;
               for(int i = H;i <= L && !F;i++){
					if(FF(i)){
						F=true;
						res=i;
					}					
               }
               printf("Case #%d: ",r);
               if(!F)
                     
                       cout<<"NO"<<endl;
               else
					cout<<res<<endl;
	}
	
		
	return 0;
}
