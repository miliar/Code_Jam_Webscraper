#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;


int l,d,n,yu[15][26];
string ss[5005],s;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,k,te,ans;
	cin>>l>>d>>n;
	for (i = 0 ; i < d ; i++)cin>>ss[i];
	for (te = 1 ; te <= n ; te++)
	{
		cin>>s;
		memset(yu,0, sizeof yu);
		for (i = k = 0 ; i < s.length() ; i++,k++)
		{
			if(s[i]=='(')
			{
				for (i=i+1 ; s[i] != ')' ; i++)yu[k][s[i]-'a'] = 1;
			}
			else
				yu[k][s[i]-'a'] = 1;
		}
		for (i = ans = 0 ; i < d ; i++)
		{
			for (k = 0 ; k < l ; k++)
				if(!yu[k][ss[i][k]-'a']) break;
			if(k == l) ans++;
		}
		cout<<"Case #"<<te<<": "<<ans<<endl;
	}
	return 0;
}
