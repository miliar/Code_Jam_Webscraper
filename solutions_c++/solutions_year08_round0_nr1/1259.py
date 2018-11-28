#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int i , count , ca = 1, n , s , q , ans;
	string str;
	map<string,int> sq;
	bool b[105];
	cin>>n;
	while(n--)
	{
		sq.clear();
		ans = 0;
		cin>>s;
		getchar();
		for( i = 0 ; i < s ; i++)
		{
			getline(cin,str);
			sq[str] = i;
		}
		cin>>q;
		getchar();
		memset( b , 0 , sizeof(b) );
		count = 0;
		while(q--)
		{
			getline(cin,str);
			i = sq[str];
			if(!b[i])
			{
				count++;
				b[i] = 1;
			}
			if( count == s )
			{
				ans++;
				count = 1;
				memset(b , 0 , sizeof(b));
				b[i] = 1;
			}
		}
		printf("Case #%d: %d\n" , ca , ans);
		ca++;
	}
}