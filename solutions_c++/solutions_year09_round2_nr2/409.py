# include <iostream>
# include <string>
# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <vector>
# include <queue>
# include <cstring>
# include <map>
# include <cmath>

using namespace std;

# define vi vector < int >
# define vvi vector < vi >
# define For(i,n) for((int)i = 0; (int)i < (int)n; ++i)

int main ()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("BoutputL.out", "w", stdout);

	int t,k;
	int i;
	string n,tmp;
	cin>>t;
	For(k,t)
	{
		cin>>n;
		For(i,n.size() - 1)
			if(n[i] < n[i+1])
				break;
		if(i !=  n.size() - 1)
			next_permutation(n.begin(),n.end());
		else
		{
			char min = 'a';
			int h = -1;
			For(i,n.size())
				if(n[i]!='0' && n[i]<min)
				{
					min = n[i];
					h = i;
				}
			swap(n[0],n[h]);
			sort(n.begin() + 1,n.end());
			tmp = n[0];
			tmp += '0';
			tmp += n.substr(1, n.size());
			n = tmp;
		}
		cout<<"Case #"<<k+1<<": "<<n<<endl;
	}	
	return 0;
}