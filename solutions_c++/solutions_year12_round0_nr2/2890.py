#include <iostream>
using namespace std ;

int person[11000] ;
int n,s,p ;


int getans()
{
	int ans = 0 ;
	int cs = 0 ;
	for(int i=0;i<n;i++)
	{
		if(person[i]>=p+p-1+p-1&&(p-1>=0||n*p<=person[i]))
		{
			ans ++ ;
		}
		else
		{
			if(person[i]>=p+p-2+p-2&&person[i]<=p+p-2+p-1+p&&(p-2>=0||n*p<=person[i]))
			{
				ans ++ ;
				cs ++ ;
			}
		}
	}
	if(cs>s)
		ans -= (cs-s) ;
	return ans ;
}


int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int cas ;
	cin >> cas ;
	for(int xx=1;xx<=cas;xx++)
	{
		cout << "Case #" << xx << ": " ;
		cin >> n >> s >> p ;
		for(int i=0;i<n;i++)
		{
			cin >> person[i] ;
		}
		cout << getans() << endl ;
	}
	
}
