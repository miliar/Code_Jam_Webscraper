#include <iostream>
#include <algorithm>
using namespace std;

const int C = 258, L = 100;
int main()
{
	int map[C];
	char s[L];
	int i,j,k,t,len;

	int ca;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>ca;
	for(t=1;t<=ca;++t)
	{
		cin >> s;
		len = strlen(s);
		memset(map,-1,sizeof(map));
		bool first = false;
		map[s[0]] = 1;
		int top=0;
		for(i=1;i<len;++i)
		{
			if(map[s[i]]==-1)
			{
				map[s[i]] = top++;
				if(top==1)top++;
			}
			
		}
		long long radix = (long long)max(top, 2);
		
		/*
		cout << radix << endl;
		cout << s << endl;
		for(i=0;i<len;++i)
		{
			cout << map[s[i]] << ' ' ;
		}
		cout << endl;
		*/
		
		long long ans=0;
		for(i=0;i<len;++i)
		{
			ans *= radix;
			if(map[s[i]]==-1)exit(1);
			ans += (long long)map[s[i]];
			
		}

		cout << "Case #" << t << ": " << ans << endl;

	}
	return 0;
}