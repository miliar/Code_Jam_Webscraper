#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>n;
		int loc_o = 1;
		int loc_b = 1;
		int res = 0, time = 0;
		char ch = 0;
		for(int i = 0; i < n; i++)
		{
			char r;
			int p;
			cin>>r>>p;
			int need,tmp;

			if(r=='B') 
			{
				tmp = abs(loc_b-p)+1;
				loc_b = p;
			}
			else 
			{
				tmp = abs(loc_o-p)+1;
				loc_o = p;
			}

			if(r==ch)
			{
				res += tmp;
				time += tmp;
			}
			else
			{
				if(tmp > time) need = tmp -time;
				else need = 1;
				res += need;
				time = need;
				ch = r;
			}
		}
		cout<<"Case #"<<cas<<": "<<res<<'\n';
	}
	return 0;
}