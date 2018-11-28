#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
#define RANGE 150
char comb[RANGE][3];
char oppo[RANGE][2];
char str[4];
int C,D,N;

bool Combine(vector<char>& String,char c)
{
	bool combined = false;
	char endc = String[String.size()-1];
	for(int i = 0;i<C;++i)
	{
		if((comb[i][0]==endc&&comb[i][1]==c)||(comb[i][0]==c&&comb[i][1]==endc))
		{
			String[String.size()-1] = comb[i][2];
			combined = true;
			break;
		}
	}
	return combined;
}

bool Erase(vector<char>& String,char c)
{
	bool erased = false;
	for(int i = 0;i<String.size();++i)
	{
		for(int j = 0;j<D;++j)
		{
			if((oppo[j][0]==String[i]&&oppo[j][1]==c)||(oppo[j][0]==c&&oppo[j][1]==String[i]))
			{
				String.clear();
				erased = true;
				break;
			}
		}
	}
	return erased;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,cnt = 1;;
	scanf("%d",&t);
	while(t--)
	{
		vector<char> String;
		memset(comb,0,sizeof(comb));
		memset(oppo,0,sizeof(oppo));
		scanf("%d",&C);
		for(int i = 0;i<C;++i)
		{
			scanf("%s",str);
			comb[i][0] = str[0];
			comb[i][1] = str[1];
			comb[i][2] = str[2];
		}
		scanf("%d",&D);
		for(int i = 0;i<D;++i)
		{
			scanf("%s",str);
			oppo[i][0] = str[0];
			oppo[i][1] = str[1];
		}
		scanf("%d",&N);getchar();
		for(int i = 0;i<N;++i)
		{
			char c = getchar();
			if(String.empty())
			{
				String.push_back(c);continue;
			}

			if(Combine(String,c))
				continue;
			else
			{
				if(Erase(String,c))
					continue;
				else
					String.push_back(c);
			}
		}
		printf("Case #%d: [",cnt++);
		if(String.size() > 1)
		{
			for(int i = 0;i<String.size() - 1;++i)
				printf("%c, ",String[i]);
		}
		if(String.size() > 0)
			printf("%c",String[String.size()-1]);
		printf("]\n");
	}
	return 0;
}