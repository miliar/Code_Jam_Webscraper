#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
char str[10000] ;
vector<int> list ;
void Read()
{
	int i,v;
	list.clear() ;
	i = 0 ;
	while(1)
	{
		if(str[i] >= '0' && str[i] <= '9')
		{
			v = 0 ;
			while(str[i] >= '0' && str[i] <= '9')
			{
				v = v * 10 + str[i]-'0' ;
				i ++ ;
			}
			list.push_back(v) ;
		}
		else
		{
			if(str[i] == '\0') break ;
			i ++ ;
		}
	}
	return ;
}
set<int> S ;
bool happy(int v,int r)
{
	int t ;
	S.clear() ;
	while(v != 1)
	{
		S.insert(v) ;
		t = 0 ;
		while(v > 0)
		{
			t += (v%r)*(v%r) ;
			v /= r ;
		}	
		v = t ;
		if(S.find(v) != S.end()) break ;
	}
	if(v == 1) return 1 ;
	return 0 ;
}
bool check(int v)
{
	int i ;
	for(i = 0 ; i < list.size() ; i ++)
	{
		if(happy(v,list[i])) {}
		else break ;
	}
	if(i == list.size()) return 1 ;
	return 0 ;
} 
int main()
{
	int Case,T ;
	int ans ;
	freopen("A-small-attempt0(1).in","r",stdin);
	freopen("A.out","w",stdout) ;
	while(1 == scanf("%d",&T))
	{
		Case = 1 ;
		gets(str) ;
		while(T --)
		{
			gets(str) ;
			Read() ;
			for(ans = 2 ; ; ans ++)
			{
				if(check(ans)) break ;
			}
			printf("Case #%d: %d\n",Case++,ans) ;
		}
	}
	return 0 ;
}