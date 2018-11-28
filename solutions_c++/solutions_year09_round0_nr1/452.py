#include <iostream>
#include <vector>
#include <string>
using namespace std;

int l,d,n;
vector<string> strings;
bool match[20][1000];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	string tmp;
	for(int i = 0;i < d;i++)
	{
		cin >> tmp;
		strings.push_back(tmp);
	}
	for(int i = 0;i < n;i++)
	{
		cin >> tmp;
		memset(match,0,sizeof match);
		int j = 0;
		int k = 0;
		while(tmp[j] != '\0')
		{
			if(tmp[j] == '(')
			{
				while(tmp[j] != ')')
					match[k][tmp[j++]] = 1;
				j ++;
				k++;
			}
			else match[k++][tmp[j++]] = 1;
		}
		int cnt = 0;
		for( j = 0;j < strings.size();j++)
		{
			bool flg = true;
			for(k = 0;k < strings[j].size();k++)
			{
				if(!flg) break;
				if(!match[k][strings[j][k]])
					flg = false;
			}
			cnt += flg;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
	//system("pause");
	return 0;
}
