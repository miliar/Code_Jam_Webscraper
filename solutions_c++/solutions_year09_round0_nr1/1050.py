#include<stdio.h>
#include<math.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;

bool found(string a,char key)
{
	int l,h,mid;
	l=0;
	h=a.size()-1;
	while(l<=h)
	{
		mid=(l+h)/2;
		if(a[mid]==key)
		{
			return true;
		}
		if(a[mid]>key)
		{
			h=mid-1;
		}
		else
		{
			l=mid+1;
		}
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-l.out","w",stdout);
	int l,d,n,t=1,i,j,k,flag,cnt;
	string s;
	while(cin>>l>>d>>n)
	{
		vector <string> dic;
		for(i=0;i<d;i++)
		{
			cin>>s;
			dic.push_back(s);
		}
		while(n--)
		{
			cin>>s;
			vector <string> a;
			k=0;
			for(i=0;i<s.size();i++)
			{
				if(s[i]=='(')
				{
					a.push_back("");
					for(i++;;i++)
					{
						if(s[i]==')')
							break;
						a[k]+=s[i];
					}
					k++;
				}
				else
				{
					a.push_back("");
					a[k]+=s[i];
					k++;
				}
			}
			for(i=0;i<l;i++)
			{
				sort(a[i].begin(),a[i].end());
			}
			cnt=0;
			for(i=0;i<dic.size();i++)
			{
				flag=0;
				for(j=0;j<l;j++)
				{
					if(!found(a[j],dic[i][j]))
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
					cnt++;
			}
			cout<<"Case #"<<t++<<": "<<cnt<<endl;
		}
	}
	return 0;
}