#include <iostream>
#include <set>
#include <string>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int N,n,s,q,i,ans;
	set<string> a,b;
	string str;
	cin>>N;
	for(n=1;n<=N;n++)
	{
		cin>>s;
		getline(cin,str);
		for(i=0;i<s;i++)
		{
			getline(cin,str);
			a.insert(str);
		}
		cin>>q;
		getline(cin,str);
		ans=0;
		for(i=0;i<q;i++)
		{
			getline(cin,str);
			b.insert(str);
			if(b.size()==s)
			{
				ans++;
				b.clear();
				b.insert(str);
			}
		}
		b.clear();
		cout<<"Case #"<<n<<": "<<ans<<endl;
	}
	return 0;
}