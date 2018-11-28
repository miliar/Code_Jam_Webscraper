#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

map<char, string> mp;
string a[1000];
int ans[1000];
int b[1000][1000];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	mp['0'] = "0000";
	mp['1'] = "0001";
	mp['2'] = "0010";
	mp['3'] = "0011";
	mp['4'] = "0100";
	mp['5'] = "0101";
	mp['6'] = "0110";
	mp['7'] = "0111";
	mp['8'] = "1000";
	mp['9'] = "1001";
	mp['A'] = "1010";
	mp['B'] = "1011";
	mp['C'] = "1100";
	mp['D'] = "1101";
	mp['E'] = "1110";
	mp['F'] = "1111";
	int i,j,k,n,m,t,l,ii,jj;
	cin>>t;
	char c;
	int total,mn;
	for(l=1;l<=t;++l)
	{
		total = 0;
		for(i=0;i<1000;++i)
			ans[i] = 0;
		cin>>n>>m;
		k = m/4;
		for(i=0;i<n;++i)
		{
			a[i] = "";
			for(j=0;j<k;++j)
			{
				cin>>c;
				a[i]+=mp[c];
			}
		}
		while(total < n*m)
		{
			for(i=0;i<n;++i)
				for(j=0;j<m;++j)
				{
					if(a[i][j] == '2')
					{
						b[i][j] = 0;
						continue;
					}
					if(i == 0 || j == 0)
						b[i][j] = 1;
					else
						if(a[i-1][j] == '2' || a[i][j-1] == '2' || a[i-1][j-1] == '2')
							b[i][j] = 1;
						else
						{
							if(a[i-1][j] != a[i][j] && a[i][j-1] != a[i][j] && a[i-1][j-1] == a[i][j])
							{
								b[i][j] = min (b[i-1][j]+1, min(b[i][j-1]+1,b[i-1][j-1]+1));
							}
							else
								b[i][j] = 1;
						}
				}
			ii = 0;
			jj = 0;
			mn = 0;
			for(i=0;i<n;++i)
				for(j=0;j<m;++j)
					if(b[i][j] > mn)
					{
						ii = i;
						jj = j;
						mn = b[i][j];
					}
			total += mn*mn;
			ans[mn]++;
			for(i=ii-mn+1;i<=ii;++i)
				for(j = jj-mn+1;j<=jj;++j)
					a[i][j] = '2';
		}
		int dif = 0;
			for(i=0;i<1000;++i)
				if(ans[i]!=0)
					++dif;
		cout<<"Case #"<<l<<": "<<dif<<endl;
			for(i=999;i>0;--i)
				if(ans[i]>0)
					cout<<i<<' '<<ans[i]<<endl;
	}
	return 0;
}