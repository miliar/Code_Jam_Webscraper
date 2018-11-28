#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;
string str ;
int T,L,A ;
char S[5000] ;
void change()
{
	int i ;
	string temp = "" ;
	for(i = 0 ; i < str.size() ; i ++)
	{
		if(str[i] != ' ')
			temp += str[i] ;
	}
	str = temp ;
}
double Ans ;
void get(string &now,string& name,double& v,string& Left,string& Right)
{
	int i ;
	string temp ;
	v = 0 ;
	Left = Right = "" ;
	name = "" ;
	for(i = 0 ; i < now.size() ; i ++)
	{
		if(now[i] >= '0' && now[i] <= '9')
		{
			break ;
		}
	}
	temp = "" ;
	while(now[i] >= '0' && now[i] <= '9' || now[i] == '.')
	{
		temp += now[i++] ;
	}
	double ret ;
	sscanf(temp.c_str(),"%lf",&v) ;
	while(now[i] >= 'a' && now[i] <= 'z')
	{
		name += now[i++] ;
	}
	if(name != "")
	{
		int cnt = 0 ;
		while(1)
		{
			if(now[i] == '(')
				cnt ++ ;
			else if(now[i] == ')')
				cnt -- ;
			Left += now[i++] ;
			if(cnt == 0)
				break ;
		}
		cnt = 0 ;
		while(1)
		{
			if(now[i] == '(')
				cnt ++ ;
			else if(now[i] == ')')
				cnt -- ;
			Right += now[i++] ;
			if(cnt == 0)
				break ;
		}
	}
	return  ;
}
set<string> Q ;
void dfs(string now)
{
	int i ;
	if(now == "") return ;
	double v ;
	string Left,Right ;
	string name ;
	get(now,name,v,Left,Right) ;
	Ans *= v ;
	if(Q.find(name) != Q.end())
	{
		dfs(Left) ;
	}
	else
	{
		dfs(Right);
	}
}
void solve()
{
	Ans = 1.0 ;
	change() ;
	dfs(str) ;
	printf("%.7lf\n",Ans) ;
}
int main()
{
	int i ;
	freopen("A-large.in","r",stdin);
	freopen("AA.out","w",stdout) ;
	while(1 == scanf("%d",&T))
	{
		int Case = 1 ;
		while(T --)
		{
			scanf("%d",&L) ;
			gets(S) ;
			str = "" ;
			for(i = 0 ; i < L ; i ++)
			{
				gets(S) ;
				str += S ;
			}
			scanf("%d",&A) ;
			Q.clear() ;
			string name ;
			printf("Case #%d:\n",Case++) ;
			for(i = 0 ; i < A ; i ++)
			{
				cin >> name ;
				Q.clear() ;
				int B ;
				scanf("%d",&B) ;
				int j ;
				for(j = 0 ; j < B ; j ++)
				{
					cin >> name ;
					Q.insert(name) ;
				}
				solve() ;
			}
		}
	}
	return 0 ;
}