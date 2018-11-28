#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<cstdio>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
int main()
{
	int t, t1=1;
	cin>>t;
    vector<vector<long long int> >v(2000001);
	for(long long int i =1;i<=2000000;i++)
	{
		vector<long long int>tt;
		stringstream s1;
		s1<<i;
		string s;
		s = s1.str();
		int sSZ = s.size();
		for(int j=0;j<s.size()-1;j++)
		{
			string newStr = s.substr(j+1,sSZ-j-1) + s.substr(0,j+1);
			if(newStr[0]=='0' || s.compare(newStr)==0)continue;
			stringstream s2;
			s2<<newStr;
			long long int t12;
			s2>>t12;
			if(find(tt.begin(),tt.end(),t12)==tt.end())
				tt.push_back(t12);
		}
		v[i]=tt;
	}
	while(t1<=t)
	{
		int a,b,count=0;
		cin>>a>>b;
		for(long long int i=a;i<=b;i++)
		{
			vector<long long int>ty = v[i];
			for(int kk=0;kk<ty.size();kk++)
			{
				long long int t11 = ty[kk];
 				if(t11>=a && t11<=b)
				{
					if(i<t11){
						//cout<<i<<" "<<t11<<endl;
						count++;
					}
				}
			}
		}
		cout<<"Case #"<<t1++<<": "<<count<<endl;
	}
	return 0;
}
