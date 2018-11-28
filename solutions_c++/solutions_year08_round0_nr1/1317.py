#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	map<string, int> m;
	int n;
	cin >> n;

	for(int test=0; test<n; test++)
	{
		m.clear();
		int s,q;
		int ans=0;
		string tmp;
		cin >> s;
		getline(cin, tmp);
		for(int i=0; i<s; i++)
		{			
			getline(cin, tmp);
			m[tmp]=i;
		}


		cin >> q;
		getline(cin, tmp);

		int cnt=0;
		int shn[100];
		memset(shn, 0, sizeof(shn));
		for(int i=0; i<q; i++)
		{			
			getline(cin, tmp);
			if(!shn[m[tmp]])
			{
				cnt++;
				shn[m[tmp]]=1;
			}				
			if(cnt==s)
			{
				ans++;
				memset(shn, 0, sizeof(shn));
				cnt=1;
				shn[m[tmp]]=1;
			}
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
				
	}
	return 0;
}
