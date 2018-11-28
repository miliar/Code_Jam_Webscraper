#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

int calc(int n)
{
	int p=n;
	vector <int> st;
	while(n)
	{
		st.push_back(n%10);
		n/=10;
	}
	sort(st.begin(),st.end());
	int minim=1000000000;
	while(next_permutation(st.begin(),st.end()))
	{
		int k=0;
		for(int i=0;i<st.size();i++)
			k=k*10+st[i];
		if(k-p>0&&k-p<minim)
			minim=k-p;
	}
	if(minim==1000000000)
	{
		st.push_back(0);
	}	 
	sort(st.begin(),st.end());
	while(next_permutation(st.begin(),st.end()))
	{
		int k=0;
		for(int i=0;i<st.size();i++)
			k=k*10+st[i];
		if(k-p>0&&k-p<minim)
			minim=k-p;
	}
	return minim+p;
} 	  	  

int main()
{
		int T;
		cin>>T;
		//cout<<T;
		int K=T;
		ofstream fout("out.txt");
		while(T--)
		{
			int N;
			cin>>N;
			int ans=calc(N);
			//cout<<"!";
			fout<<"Case #"<<K-T<<": "<<ans<<endl;
		}
		fout.close();
		return 0;
}

