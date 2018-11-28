#include <iostream>
using namespace std;
int cnt[10];
int main()
{
	int tc;
	cin>>tc;int cs=0;
	while(tc--) {
		++cs;
		string s;
		cin>>s;string org=s;
		next_permutation(s.begin(),s.end());
		cout<<"Case #"<<cs<<": ";
		if (s>org) cout<<s<<endl;
		else {
			/*
			memset(cnt,0,sizeof(cnt));
			for(int i=0;i<s.size();i++) cnt[s[i]-'0']++;
			string ans="";
			bool extraUsed=0;
			for(int i=0;i<=s.size();i++) {
				for(int j=0;j<10;j++) {
					if (i==0 && j==0) continue;
					bool inString=0;
					if (s.find(j+'0')!=string::npos) inString=1;
					if (inString) {if (cnt[j]==0) continue; else cnt[j]--;}
					if (!inString) {if (extraUsed || j!=0) continue; else extraUsed=1;}
					ans+='0'+j;
					break;
				}
			}
			*/
			sort(s.begin(),s.end());
			if (s[0]=='0')
			for(int i=0;i<s.size();i++) if (s[i]!='0') {swap(s[0],s[i]);break;}
			cout<<s[0]<<0<<s.substr(1)<<endl;
		}
	}
	return 0;
}