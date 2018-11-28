#include<iostream>
using namespace std;

string s,templ;
char st[700];
int dp[2][700];
int T,tc,i,j,z,k,ans;

int main() {
	templ="welcome to code jam";
	cin>>T;
	getchar();
	for(tc=1;tc<=T;tc++) {
		scanf("%[^\n]",st);
		getchar();
		s=st;
		for(j=0;j<600;j++) {
			dp[0][j]=0;
			dp[1][j]=0;
		}
		for(j=0;j<s.length();j++) if(s[j]=='w') dp[0][j]=1;
		z=0;
		for(i=1;i<templ.size();i++) {
			z=1-z;
			for(j=0;j<s.length();j++) {
				dp[z][j]=0;
				if(s[j]!=templ[i]) continue;
				for(k=0;k<j;k++) {
					if(s[k]!=templ[i-1]) continue;
					dp[z][j]+=dp[1-z][k];
					dp[z][j]%=10000;
				}			
			}
		}
		cout<<"Case #"<<tc<<": ";
		ans=0;
		for(j=0;j<s.length();j++) {
			ans+=dp[z][j];
			ans%=10000;
		}
		s="";
		while(ans>0) {
			s=char('0'+ans%10)+s;
			ans/=10;
		}
		while(s.size()<4) s="0"+s;
		cout<<s<<endl;
	}
	return 0;
}
