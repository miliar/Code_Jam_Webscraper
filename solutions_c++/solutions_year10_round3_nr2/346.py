#include<algorithm>
#include<iostream>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<list>

#define mn(a,b) ( (a) < (b) ? (a) : (b) )
#define mx(a,b) ( (a) > (b) ? (a) : (b) )
#define ab(a) ( (a) < (0) ? (-a) : (a) )

#define MP make_pair
#define PB push_back
#define F first
#define S second

#define ll long long

using namespace std;


int T;
ll L,P,C;

ll power(ll x,int deg){
	ll res=1;
	for(int i=0;i<deg;i++)
		res*=x;
	return res;
}
int f(ll l,ll c,ll p){
//cout<<l<<" "<<c<<" "<<p<<endl;
	ll res=l*c;
	int step=1;
	while(res < p){
		step++;
		res*=c;		
	}
	if(step==1) return 0;
	return min(f(l*power(c,step/2),c,p),
                   f(l,c,l*power(c,step/2+step%2)))+1;
}

void solve(int x){
	scanf("%I64d%I64d%I64d",&L,&P,&C);
	printf("Case #%d: %d\n",x,f(L,C,P));	
	
}

int main(){

freopen("input.txt","r",stdin);
freopen("output.out","w",stdout);
scanf("%d",&T);
for(int i=1;i<=T;i++)
	solve(i);

return 0;
}