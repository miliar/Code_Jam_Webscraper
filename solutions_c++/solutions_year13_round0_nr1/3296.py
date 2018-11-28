#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

char map[4][5];

bool win(char k)
{
	for(int i=0;i<4;++i)
	{
		int sum=0;
		for(int j=0;j<4;++j)
			if(map[i][j]==k || map[i][j]=='T')
				++sum;
		if(sum==4)
			return true;
		sum=0;
		for(int j=0;j<4;++j)
			if(map[j][i]==k || map[j][i]=='T')
				++sum;
		if(sum==4)
			return true;
	}
	int sum=0;
	for(int i=0;i<4;++i)
		if(map[i][i]==k || map[i][i]=='T')
			++sum;
	if(sum==4)
		return true;
	sum=0;
	for(int i=0;i<4;++i)
		if(map[i][3-i]==k || map[i][3-i]=='T')
			++sum;
	if(sum==4)
		return true;
	return false;
}

int work()
{
	if(win('X'))
		return 1;
	if(win('O'))
		return 2;
	return 0;
}

int main ()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;++ii)
	{
		for(int i=0;i<4;++i)
			scanf("%s",map[i]);
		printf("Case #%d: ",ii);
		int key=work();
		if(key==1)
			puts("X won");
		else if(key==2)
			puts("O won");
		else
		{
			int sum=0;
			for(int i=0;i<4;++i)
				for(int j=0;j<4;++j)
					if(map[i][j]=='.')
						++sum;
			if(sum)
				puts("Game has not completed");
			else
				puts("Draw");
		}
	}
	return 0;
}
