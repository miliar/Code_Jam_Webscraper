#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

#define vi vector <int>
#define pb(a) push_back(a)
#define ppb(a) pop_back(a)


int func(vi alp)
{
	for(int i =0;i<alp.size();i++)if(alp[i]==999999999)return 1;
	return 0;
}
int main()
{
	int n,cases=0;
	cin>>n;
	while(n--)
	{
		int s;
		cin>>s;
		char c;
		vector< string > eng,que;
		char str[101];
		map<string,int>mm;
		for(int i =0;i<s;i++){c=getchar();scanf("%[^\n]",str);string pp(str);eng.pb(pp);mm[pp]=i;}
		int q;
		cin>>q;
		for(int j =0;j<q;j++){c=getchar();scanf("%[^\n]",str);string pp(str);que.pb(pp);}
		int temp=0;
		vi alp(s,999999999);
		vi hi=alp;
		for(int k =0;k<que.size();k++)
		{
			if(alp[mm[que[k]]]==999999999)alp[mm[que[k]]]=i;		
			if(func(alp))continue;
			else
			{
				temp++;
				alp=hi;
				k--;
			}
		}
		cout<<"Case #"<<++cases<<": "<<temp<<endl;
		
	}
return 0;
}

