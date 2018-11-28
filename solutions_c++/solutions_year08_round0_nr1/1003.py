#include <iostream>
#include <cstdio>
#include <map>
#include <string>
using namespace std;

int n,s,q;
int query[1001];
int count[101];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,index,used,swi,count2;
	map<string,int> dic;
	string sname;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		dic.clear();
		index=0;
		cin>>s;
		getline(cin,sname);
		for(j=1;j<=s;j++)
		{
			getline(cin,sname);
			dic.insert(make_pair(sname,index));
			index++;
		}
		cin>>q;
		getline(cin,sname);
		for(j=1;j<=q;j++)
		{
			getline(cin,sname);
			query[j]=dic[sname];
		}
		swi=-1;
		for(j=1;j<=q;j++)
		{
			swi++;
			count2=0;
			memset(count,0,sizeof(count));
			used=0;
			for(k=j;k<=q;k++)
			{
				count[query[k]]++;
				if(count[query[k]]==1)
				{
					count2++;
					if(count2==s)
						break;
				}
			}
			k--;
			j=k;
		}
		if(swi==-1)swi=0;
		cout<<"Case #"<<i<<": "<<swi<<endl;
	}
	return 0;
}