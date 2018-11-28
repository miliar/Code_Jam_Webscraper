#include <stdio.h>
#include <string>
#include <map>
#include <iostream>
using namespace std;

int main()
{
	freopen("D://in.txt","r",stdin);
	freopen("D://out.txt","w",stdout);

	int T,cas,N,M,i,j,k,cnt,res;
	string a[105],b[105];
	map <string,int> m;
	map <string,int>::iterator itor;

	cin>>T;
	for (cas=1;cas<=T;cas++)
	{
		cin>>N>>M;
		for (i=0;i<N;i++) cin>>a[i];
		for (i=0;i<M;i++) cin>>b[i];
	    m.clear();
		cnt=0;
		m[""]=cnt++;
		for (i=0;i<N;i++)
		{
			while (a[i]!="")
			{
				if (m.find(a[i])==m.end()) m[a[i]]=cnt++;
				while (a[i][a[i].length()-1]!='/') a[i].erase(a[i].length()-1,1);a[i].erase(a[i].length()-1,1);
			}
		}
		res=0;
		for (i=0;i<M;i++)
		{
			while (m.find(b[i])==m.end())
			{
				res++;
				m[b[i]]=cnt++;
				while (b[i][b[i].length()-1]!='/') b[i].erase(b[i].length()-1,1);b[i].erase(b[i].length()-1,1);
			}
		}
		cout<<"Case #"<<cas<<": "<<res<<endl;
	}
	return 0;
}