#include <iostream>
#include <memory.h>
using namespace std ;


int a,b;

int jiecheng(int num)
{
	int sum = 1 ;
	for(int i=1;i<=num;i++)
		sum *= i ;
}

int getw(int num)
{
	if(num<10)
		return 1 ;
	if(num>=10&&num<=99)
		return 2 ;
	if(num>=100&&num<=999)
		return 3 ;
	if(num>=1000&&num<=9999)
		return 4 ;
	if(num>=10000&&num<=99999)
		return 5 ;
	if(num>=100000&&num<=999999)
		return 6 ;
	if(num>=1000000&&num<=9999999)
		return 7 ;	
}

int getans()
{
	int ans = 0 ;
	for(int i=a;i<=b;i++)
	{
		int d = 1 ;
		int w = getw(i);
	

		int tem = i ;
		for(int j=1;j<w;j++)
			d *= 10 ;
		for(int j=1;j<w;j++)
		{
			int ge = tem%10 ;
			tem /= 10 ;
			ge *= d ;
			tem += ge ;

			if(tem>=a&&tem<=b)
			{
				if(i<tem)
				{
					//cout << i << " " << tem << " " << ans << endl ;
					ans ++ ;
				}
			}			
			
		}					
	}
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
		cin >> a >> b ;		
		cout << getans() << endl ;
	}
}
