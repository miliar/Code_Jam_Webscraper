#include <iostream>
#include <string>

using namespace std;

struct Score
{
	int s;
	bool sup;
}s[105];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,S,P,N;

	cin >>T;

	for (int c = 1;c <= T;++c)
	{
		cin >> N >> S >> P;

		int ans = 0;

		for (int i = 0;i < N;++i) 
		{
			cin >> s[i].s;
			if (s[i].s / 3 >= P || s[i].s % 3 != 0 && s[i].s/3 + 1 >= P)
			{
				ans++;
				s[i].sup = false;
			}
	
			else s[i].sup = true;
		}

		for (int i = 0;i < N;++i)
		{
			if (S == 0) break;
			
			if (s[i].s == 0) continue; 

			if (s[i].sup == true && (s[i].s % 3 == 0 && s[i].s / 3 + 1 >= P || s[i].s/3 + s[i].s % 3 >= P))
			{
				ans++;
				S--;
			}
		}

		cout <<"Case #"<<c<<": "<<ans<<endl;
	}

	return 0;
}
