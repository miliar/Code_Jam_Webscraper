#include <iostream>
#include<cstring>
#include<algorithm>
using namespace std;
char str[2000] ;
int p[505] ;
int list[2000] ;

int main()
{
    //freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T,i,j ;
	while(1 == scanf("%d",&T))
	{
		int Case = 1 ;
		while(T --)
		{
			scanf("%s",str) ;
			memset(p,-1,sizeof(p)) ;
			i = 0 ;
			p[str[0]] = 1 ;
			while(str[i] != '\0')
			{
				if(str[i] == str[0]) i ++ ;
				else
					break ;
			}
			int ID = 2 ;
			if(str[i] != '\0')
			{
				p[str[i]] = 0 ;
			}
			i = 0 ;
			while(str[i] != '\0')
			{
				if(p[str[i]] != -1)
				{
					list[i] = p[str[i]] ;
				}
				else
				{
					p[str[i]] = ID ++ ;
					list[i] = p[str[i]] ;
				}
				i ++ ;
			}
			int len = i ;
			long long ans = 0 ;
			for(i = 0 ; i < len ; i ++)
			{
				ans = ans * ID + list[i] ;
			}
			printf("Case #%d: ",Case++) ;
			cout << ans << endl ;
		}
	}
	return 0 ;
}