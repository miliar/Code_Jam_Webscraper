#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <memory.h>

using namespace std;

string ss[5050];
bool is[5050][30];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,D,n;
	char c;
	cin>>l>>D>>n;
	for (int i=0;i<D;i++)
		cin>>ss[i];
	for (int k=0;k<n;k++)
	{
		string t;
		memset(is,0,sizeof(is));
		cin>>t;
		int d=0;
		int rr=0;
		for (int i=0;i<t.size();i++)
		{
			
			if (t[i]=='(')
			{
				while(t[++i]!=')')
					is[d][t[i]-'a']=true;
				d++;
			}
			else
			{
				is[d][t[i]-'a']=true;
				d++;
			}
		}
		int res=0;
		for (int i=0;i<D;i++)
		{
			bool suc=true;
			for (int j=0;j<l;j++)
			{
				if (is[j][ss[i][j]-'a']==false)
				{
					suc=false;
					break;
				}
			}
			if (suc)
				res++;
		}
		cout<<"Case #"<<k+1<<": "<<res<<endl;
	}
	return 0;
}