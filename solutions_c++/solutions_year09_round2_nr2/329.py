#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;
char str[30] ;
int v,len ;
int list[10] ;
int L[10] ;
string ans ;
string Ans ;
int main()
{
	int T ;
	int i,j,k,l ;
	freopen("B-large.in","r",stdin);
	freopen("qq.out","w",stdout) ;
	while(1 == scanf("%d",&T))
	{
		int Case = 1 ;
		while(T --)
		{
			scanf("%s",str) ;
			len = strlen(str) ;
			memset(list,0,sizeof(list)) ;
			v = 0 ;
			for(i = 0 ; i < len ; i ++)
			{
				list[str[i]-'0'] ++ ;
			}
			Ans = "" ;
			for(i = 0 ; i < len ; i ++)
			{
				memcpy(L,list,sizeof(list)) ;
				int find = 0 ;
				ans = "" ;
				for(j = 0 ; j < len ; j ++)
				{
					if(j < i)
					{
						if(L[str[j]-'0'])
						{
							L[str[j]-'0'] -- ;
							ans += str[j] ;
						}
						else
							break ;
					}
					else if(j == i)
					{
						for(k = str[j]-'0'+1 ; k < 10 ; k ++)
						{
							if(L[k])
							{
								ans += k+'0' ;
								L[k] -- ;
								break ;
							}
						}
						if(k < 10)
						{
							for(l = 0 ; l < 10 ; l ++)
							{
								while(L[l])
								{
									ans += l+'0' ;
									L[l] -- ;
								}
							}
							find = 1 ;
							break ;
						}
					}
				}
				if(find && (Ans == "" || ans < Ans))
						Ans = ans ;
			}
			if(Ans == "")
			{
				for(i = 1 ; i < 10 ; i ++)
				{
					if(list[i])
					{
						Ans += i+'0' ;
						list[i] -- ;
						break ;
					}
				}
				Ans += '0' ;
				for(i = 0 ; i < 10 ; i ++)
				{
					while(list[i])
					{
						Ans += i+'0' ;
						list[i] -- ;
					}
				}
			}
			printf("Case #%d: %s\n",Case++,Ans.c_str()) ;
		}
	}
	return 0 ;
}