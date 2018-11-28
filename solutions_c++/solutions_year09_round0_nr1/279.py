#include<iostream>
#include<string>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=5002;
int ans,i,ti,l,d,ca;
string s[maxn],t;
bool ok(string a,string b){
	int i,j=0;
	fr(i,0,l-1)
		if(b[j]=='('){
			bool pd=false;
			while(b[j]!=')'){
				if(b[j]==a[i])
					pd=true;
				++j;
			}
			++j;
			if(!pd)
				return false;
		}
		else{
			if(b[j]!=a[i])
				return false;
			++j;
		}
	return true;
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>l>>d>>ca;
	fr(i,1,d)
		cin>>s[i];
	fr(ti,1,ca){
		cin>>t;
		ans=0;
		fr(i,1,d)
			if(ok(s[i],t))
				++ans;
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}
