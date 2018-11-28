#include <string>
#include <iostream>
using namespace std;

int l,d,n;
string s[5012];

int sol(string& y,int t){
	int i,c=0,sz=y.size();
	for(i=0;i<l;i++){
		if(y[c]=='('){
			int r=c+1;int f=0;
			while(r<sz && y[r]!=')'){f|= y[r]==s[t][i];r++;}
			if(!f)return false;
			c=r+1;
		}else{
			if(y[c]!=s[t][i])return false;
			c++;
		}
	}return true;
}

int main(){
cin>>l>>d>>n;
int i,j;
for(i=0;i<d;++i)cin>>s[i];
for(i=0;i<n;i++){
string y;cin>>y;
int res=0;
for(j=0;j<d;j++)res+=sol(y,j);
cout<<"Case #"<<(i+1)<<": "<<res<<endl;
}
return 0;
}
