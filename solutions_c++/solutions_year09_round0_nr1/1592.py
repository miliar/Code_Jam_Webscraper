#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<cctype>
#include<cassert>
#include<iostream>

using namespace std;

#define D 5005
#define L 20
char dict[D][L];


vector<string> split(char *a)
{
	int i=0;
	vector<string> ans;
	while(a[i]!=0)
	{
		//cout<<"i= "<<i<<endl;
		if(a[i]=='(')
		{
			string s;
			++i;
			while(a[i]!=')')
			{
				s+=a[i];
				++i;
			}
			++i;
			ans.push_back(s);
		}
		else
		{
			string s;
			s+=a[i];
			ans.push_back(s);
			++i;
		}
	}
	return ans;
}

bool fun(vector<string> &tokens,int x)
{
	int i,j;
	for(i=0;i<tokens.size();++i)
	{
		bool ok=false;
		for(j=0;j<tokens[i].size();++j)
			if(tokens[i][j]==dict[x][i])
			{
				ok=true;
				break;
			}
		if(!ok)
			return false;
	}
	return true;
}

int main()
{
	int l,d,n;
	scanf("%d %d %d",&l,&d,&n);
	int i;
	for(i=0;i<d;++i)
		scanf("%s",dict[i]);
	
	//cout<<"here"<<endl;
	int t;
	char buf[26*D];
	for(t=1;t<=n;++t)
	{
		scanf("%s",buf);
		vector<string> tokens=split(buf);
		assert(tokens.size()==l);
		//cout<<"hrer"<<endl;
		int ans=0;
		for(i=0;i<d;++i)
			ans+=fun(tokens,i);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}

