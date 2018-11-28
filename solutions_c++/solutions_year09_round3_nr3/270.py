#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<fstream>

using namespace std;

int check(vector <int> st, vector <int> rm)
{
	int ans=0;
	for(int i=0;i<rm.size();i++)
	{
		st[rm[i]]=0;
		for(int j=rm[i]-1;j>0&&st[j]!=0;ans++,j--);
		for(int j=rm[i]+1;j<st.size()&&st[j]!=0;j++,ans++);
	}
	return ans;
}
		


int calc(vector <int> st, vector <int> rm)
{
	int ans=check(st,rm);
	while(next_permutation(rm.begin(),rm.end()))
	{
		int n=check(st,rm);
		if(ans>n)
			ans=n;
		/*for(int i=0;i<rm.size();i++)
			cout<<rm[i]<<" ";
		cout<<n<<endl;*/
	}
	return ans;
}

int main()
{
	int T;
	cin>>T;
	int K=T;
	ofstream fout("out.txt");
	while(T--)
	{
		int P, Q;
		cin>>P>>Q;
		vector <int> st;
		st.resize(P+1,1);
		vector <int> rm;
		rm.resize(Q);
		for(int i=0;i<rm.size();i++)
			cin>>rm[i];
		//	  cout<<"@";
		int ans=calc(st,rm);
		//cout<<"!";
		fout<<"Case #"<<K-T<<": "<<ans<<endl;
	}
	return 0;
}

