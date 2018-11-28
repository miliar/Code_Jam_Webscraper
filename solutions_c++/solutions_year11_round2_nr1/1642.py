#include<iostream>
#include<vector>
#include<string>
using namespace std;
main()
{
   int tt,t;
   cin>>tt;
   for(t=1;t<=tt;t++)
   {
	cout<<"Case #"<<t<<":"<<endl;
	int n;
	cin>>n;
	vector<string> in;
	vector<float> wp_w,wp_t,owp,oowp;
	vector<vector <int> > op (n, vector<int>());
	string str;
	for(int i=0;i<n;i++)
	{
		cin>>str;
		in.push_back(str);
		int w=0,l=0;
		for(int j=0;j<n;j++)
			if(str[j]=='1')
			{   w++;  op[i].push_back(j);}
			else if(str[j]=='0')
			{   l++;  op[i].push_back(j);}
		wp_w.push_back(float(w));
		wp_t.push_back(float(w+l));
	}
	for(int i=0;i<n;i++)
	{
		float sum=0.0;
		for(int j=0;j<op[i].size();j++)
			if(in[i][op[i][j]]=='0')
				sum+=(wp_w[op[i][j]]-1)/(wp_t[op[i][j]]-1);
			else
				sum+=(wp_w[op[i][j]])/(wp_t[op[i][j]]-1);
		owp.push_back(sum/float(op[i].size()));
	}
	for(int i=0;i<n;i++)
	{
		float sum=0.0;
		for(int j=0;j<op[i].size();j++)
			sum+=owp[op[i][j]];
		oowp.push_back(sum/float(op[i].size()));
	}
	for(int i=0;i<n;i++)
		cout<<0.25*wp_w[i]/wp_t[i]+0.50*owp[i]+0.25*oowp[i]<<endl;
   }
}
