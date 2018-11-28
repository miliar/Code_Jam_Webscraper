#include<iostream>
#include<cstdio>
#include<cmath>
#include<cctype>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<fstream>

using namespace std;

int main()
{
	int L,D,N;
	ifstream fin("source");
	fin>>L>>D>>N;
	vector <string> st;
	st.resize(D);
	for(int i=0;i<D;i++)
		fin>>st[i];
	fin.get();
	int K=N;
	ofstream f("out.txt");
	f.close();
	while(N--)
	{
		string s="",p;
		getline(fin,p);
		for(int i=0;i<p.size();i++)
			if(p[i]!=' ')
				s+=p[i];
		//cout<<s<<endl;
		vector < vector <int> > allow;
		allow.resize(L);
		for(int i=0;i<L;i++)
			allow[i].resize(26,0);
		int counter=0;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]>='a'&&s[i]<='z')
				allow[counter++][int(s[i]-'a')]=1;
			else
			{
				i++;
				while(s[i]!=')')
				{
					allow[counter][int(s[i]-'a')]=1;
					i++;
				}	 	 	 
				counter++;	  	  
			}
		}
		/*for(int i=0;i<allow.size();i++)
		{
			for(int j=0;j<allow[i].size();j++)
				cout<<allow[i][j]<<" ";
			cout<<endl;
		}*/
		int ans=0;
		for(int i=0;i<D;i++)
		{
			int counting=1;
			for(int j=0;j<L&&counting;j++)
				if(allow[j][int(st[i][j]-'a')]==0)
					counting=0;
			if(counting)
				ans++;
		}
		ofstream fout("out.txt",ios::app);
		fout<<"Case #"<<K-N<<": "<<ans<<endl;
	}
	return 0;
}

