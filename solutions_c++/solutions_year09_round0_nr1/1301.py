#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	vector<string> dic;
	int L,D,N,i;
	cin>>L>>D>>N;
	for(i=0;i<D;++i)
	{
		string ts;
		cin>>ts;
		dic.push_back(ts);
	}
	int m[15][26];
	for(i=1;i<=N;++i)
	{
		memset(m,0,15*26*sizeof(int));
		string ts;
		cin>>ts;
		int k=0;
		int st=0;
		int j;
		for(j=0;j<ts.size();++j)
		{
			switch(st)
			{
			case 0:
				if(ts[j]=='(')
					st=1;
				else
				{
					m[k][(int)(ts[j]-'a')]=1;
					++k;
				}
				break;
			case 1:
				if(ts[j]==')')
				{
					st=0;
					++k;
				}
				else
					m[k][(int)(ts[j]-'a')]=1;
				break;
			}
		}
		int ans=0;
		int l;
		for(j=0;j<D;++j)
		{
			for(l=0;l<L;++l)
				if(m[l][(int)(dic[j][l]-'a')]==0)
					break;
			if(l==L)
				++ans;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}