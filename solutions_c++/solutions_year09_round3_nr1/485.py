#include<iostream>
#include<string>
#include<map>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	string s;map<char,int>mp;
	int t;cin>>t;int cas=1;
	while(t--){
	     cin>>s;mp.clear();
		 int ind=0,i,m=s.length();
		 for(i=0;i<m;i++)
		 {
		    if(mp.find(s[i])==mp.end())
			    mp[s[i]]=ind++;			
		 }
		 int b=mp.size();
		 if(b==1)b++;long long sum=0;
		 for(i=0;i<m;i++)
		 {
		     if(mp[s[i]]==0)
			 sum=sum*b+1;
			 else if(mp[s[i]]==1)
			 sum*=b;
			 else sum=sum*b+mp[s[i]];		
		 }
		 cout<<"Case #"<<cas++<<": "<<sum<<endl;
	}
	
}
