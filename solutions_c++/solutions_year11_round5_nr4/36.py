#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;
string s;
bool is_sq(ll v){
	ll l=0,u=1073741825LL;
	while (l!=u){
		ll m=(l+u)/2;
		if (m*m<v)
			l=m+1;
		else
			u=m;
	}
	return l*l==v;
}
void bt(int lev,ll val=0){
	if (lev==s.size()){
		if (is_sq(val))
			throw val;
		return;
	}
	if (s[lev]=='0')
		bt(lev+1,val*2);
	else if (s[lev]=='1')
		bt(lev+1,val*2+1);
	else{
		bt(lev+1,val*2);
		bt(lev+1,val*2+1);
	}
}
int main(){
	int tnum,tcou=0;cin>>tnum;
	while (tnum--){
		cin>>s;
		try{bt(0);cout<<"Warning!"<<endl;}
		catch(ll v){
			string out;
			while (v>0){
				out+=((v%2==0)?'0':'1');
				v/=2;
			}
			reverse(out.begin(),out.end());
			cout<<"Case #"<<++tcou<<": "<<out<<endl;
		}
	}
	return 0;
}
