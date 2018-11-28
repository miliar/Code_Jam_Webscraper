// Sai
#include<iostream>
#include<vector>
#include<map>
using namespace std;

main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
	int n;
	cin>>n;
	vector<pair<char,int> > s(n);
	vector<int> o,b;
	for(int i=0;i<n;i++)
		cin>>s[i].first>>s[i].second;
	int op=1,bp=1,otime=0,btime=0;
	int time=0;char p;
	for(int i=0;i<n;i++)
	{
		if(s[i].first=='O'){
			int t=max(s[i].second-op,op-s[i].second);
			op=s[i].second;
			if(p=='O')
				otime+=t+1;
			else
				otime=max(btime+1,otime+t+1);
			p='O';
			}
		else {
			int t=max(s[i].second-bp,bp-s[i].second);
			bp=s[i].second;
			if(p=='B')
				btime=btime+t+1;
			else
				btime=max(otime+1,btime+t+1);
			p='B';
			}
//		cout<<otime<<" "<<btime<<endl;
	}
	cout<<"Case #"<<t<<": "<<max(otime,btime)<<endl;
	}
}
