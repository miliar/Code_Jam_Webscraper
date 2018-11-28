#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main()
	{
	int L,D,N;
	cin>>L>>D>>N;
	int i,j;
	vector<string> s(D);
	for(i=0;i<D;i++)
		cin>>s[i];
	for(i=1;i<=N;i++)
		{
		string t;
		vector<string> m(L);
		cin>>t;
		int k,z=0;
		for(k=0;k<t.size();k++)
			{
			
			if(t[k]=='(')
				{
				k++;
				while(t[k]!=')')
					{
					m[z]+=t[k];
					k++;
					}
				
				z++;
				}
			else
				{
				m[z] = t[k];
				
				z++;
				}
				
			}
		
		long long int ans=0;
		for(int x=0;x<D;x++)
			{
			bool con;
			for(j=0;j<L;j++)
				{
				con = false;
				for(k=0;k<m[j].size();k++)
					{
					if(m[j][k] == s[x][j])
						{
						con = true;
						break;
						}
					}
				if(!con)break;			
				}
			if(con) ans++;
			}
		cout<<"Case #"<<i<<": "<<ans<<endl;
		}

	return 0;
	}
