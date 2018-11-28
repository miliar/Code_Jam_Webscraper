#include <iostream>
#include <string>

using namespace std;

char c[300][300];
char d[300][300];

int i, j, k, p;
int T, C, D, N;
string tmp, s, ans;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for( k = 1; k <= T; k ++ )
	{
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		ans.clear();

		cin>>C;
		for( i = 0; i < C; i ++ )
		{
			cin>>tmp;
			c[ tmp[ 0 ] ][ tmp[ 1 ] ] = c[ tmp[ 1 ] ][ tmp[ 0 ] ] = tmp[ 2 ];
		}
		cin>>D;
		for( i = 0; i < D; i ++ )
		{
			cin>>tmp;
			d[ tmp[ 0 ] ][ tmp[ 1 ] ] = d[ tmp[ 1 ] ][tmp [ 0 ] ] = 1;
		}
		cin>>N;
		cin>>s;

		ans.insert(ans.end(), s[0]);
		p = 0;
		
		for( i = 1; i < N; i ++ )
		{
			if(ans.size() == 0)
			{
				ans.insert(ans.end(), s[i]);
				p = 0;
				continue;
			}
			//printf("%d\n",c[ s[i]][ans[p]]);
			if(c[ s[i]][ans[p]] != 0)
			{
				ans[p] = c[s[i]][ans[p]];
				
			}
			else
			{
				for(j = 'A' ; j <= 'Z'; j++)
					if(d[j][s[i]] != 0)
					{
						if(ans.find_first_of((char)j) == string::npos) continue;
						ans.clear();
						//cout<<ans.size()<<endl;
						break;
					}
					if(ans.size() == 0) { continue;}
				ans.insert(ans.end(), s[i]);
				p ++;
			}
		}
		//cout<<ans<<endl;
		//cout<<ans[0]<<endl<<ans[1]<<endl<<ans[2]<<endl;

		cout<<"Case #"<<k<<": [";
		if(ans.size() > 0) cout<<ans[0];
		for( i = 1; i < ans.size(); i ++)
			cout<<", "<<ans[i];
		cout<<"]"<<endl;
		
	}
	return 0;
}