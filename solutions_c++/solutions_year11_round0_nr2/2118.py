#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int cases;
int c,d,n;
char combine[30][30];
int opposed[30][30];
vector<char> list;

int main()
{
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		list.clear();
		memset(combine,0,sizeof combine);
		memset(opposed,0,sizeof opposed);
		scanf("%d ",&c);
		while(c--)
		{
			char x,y,z;
			scanf("%c%c%c ",&x,&y,&z);
			combine[x-'A'][y-'A']=z;
			combine[y-'A'][x-'A']=z;
		}
		scanf("%d ",&d);
		while(d--)
		{
			char x,y;
			scanf("%c%c ",&x,&y);
			opposed[x-'A'][y-'A']=1;
			opposed[y-'A'][x-'A']=1;
		}
		scanf("%d ",&n);
		while(n--)
		{
			char x;
			scanf("%c",&x);
			if(list.size()&&combine[list.back()-'A'][x-'A']!=0)
			{
				list.back()=combine[list.back()-'A'][x-'A'];
			}
			else
			{
				list.push_back(x);
				for(int i=0;i<list.size();++i)
				{
					if(opposed[list[i]-'A'][x-'A'])
					{
						list.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [",t);
		for(int i=0;i<list.size();++i)
		{
			if(i) printf(", ");
			printf("%c",list[i]);
		}
		puts("]");
	}
	return 0;
}
