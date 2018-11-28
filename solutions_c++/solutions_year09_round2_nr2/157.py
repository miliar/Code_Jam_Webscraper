#include<iostream>
#include<string>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		string s;
		int p,q;
		cin>>s;
		p=s.size()-1;
		while(p>0 && s[p]<=s[p-1])p--;
		if(p==0)s="0"+s;else p--;
		q=p;
		while(q+1!=s.size() && s[q+1]>s[p])q++;

		int k;
		k=s[p];s[p]=s[q];s[q]=k;
		for(int i=0;i<=p;i++)cout<<s[i];
		for(int i=s.size()-1;i>p;i--)cout<<s[i];
		cout<<endl;

	}
	return 0;
}