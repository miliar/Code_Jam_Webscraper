#include<iostream>
#include<vector>
#include<string>

using namespace std;

vector<string> dic;
vector<char> my[20];

int main(void)
{
	freopen("E:\\A-small.in","r",stdin);
	freopen("E:\\A-small.txt","w",stdout);
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	int i,k,j;
	dic.resize(d);
	for(i=0;i<d;i++)
	{
		cin>> dic[i];
	}
	for(i=0;i<n;i++)
	{
		string temp;
		cin >> temp;
		int num = 0;
		for(j=0;j<20;j++)
			my[j].clear();
		for(j=0;j<temp.length();j++)
		{
			if(temp[j]=='(')
			{
				for(k=j+1;k<temp.length();k++)
				{
					my[num].push_back(temp[k]);
					if(temp[k] == ')')
						break;
				}
				j = k;
				num++;
			}
			else
			{
				my[num++].push_back(temp[j]);
			}
		}
		int result = 0;
		for(k=0;k<d;k++)
		{
			for(j=0;j<l;j++)
			{
				int q;
				bool flag = false;
				for(q=0;q<my[j].size();q++)
				{
					if(my[j][q] == dic[k][j])
					{
						flag = true;
						break;
					}
				}
				if(!flag)
					break;
			}
			if(j == l)
				result++;
		}
		printf("Case #%d: %d\n",i+1,result);
	}
	return 0;
}
				
