// Sai
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>

using namespace std;


main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
	int C,D,N;
	string inp;
	cin>>C;
	vector<pair<string,char> > c(C);
	for(int i=0;i<C;i++)
	{
		string temp,x;
		cin>>temp;
		x=temp.substr(0,2);if(x[1]<x[0]){char t=x[1];x[1]=x[0];x[0]=t;}
		c[i].first=x;
		c[i].second=temp[2];
	}
	cin>>D;
	vector<string> d(D);
	for(int i=0;i<D;i++)
		{
		string x;
		cin>>x;if(x[1]<x[0]){char t=x[1];x[1]=x[0];x[0]=t;}
		d[i]=x;
		}
	cin>>N;
	cin>>inp;
	string out;
	for(int i=0;i<inp.size();i++)
	{
		out+=inp[i];
		int change=1;
		while(change==1 && out.size()>=2)
		{
			change=0;
			string x=out.substr(out.size()-2,2);
			if(x[1]<x[0]){char t=x[1];x[1]=x[0];x[0]=t;}
			for(int i=0;i<c.size();i++)
			{
				if(c[i].first==x)
					{
					change=1;
//					cout<<out<<"\t";
					out=out.substr(0,out.size()-2)+c[i].second;
//					cout<<out<<endl;
					}
			}
		}
		for(int i=0;i<d.size();i++)
		{
			size_t a=out.find(d[i][0]);
			size_t b=out.find(d[i][1]);
			if(a!=string::npos && b!=string::npos)
			{
			out="";
//				cout<<a<<b<<endl;
//				if(a>b)	{size_t t=a;a=b;b=t;}
//				cout<<out<<"\t";
//				out=out.erase(a,b-a+1);
//				cout<<out<<endl;
			}
		}
	}
	cout<<"Case #"<<t<<": [";
	for(int i=0;i+1<out.size();i++)
		cout<<out[i]<<", ";
	if(out.size()!=0)
		cout<<out[out.size()-1];
	cout<<"]\n";
	}
}
