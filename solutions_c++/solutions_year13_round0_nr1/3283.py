#include<cstdio>

int state[4][4];

void init()
{
	char tmp[5];
	for(int i=0;i<4;i++)
	{
		scanf("%s",tmp);
		for(int j=0;j<4;j++)
		{
			if(tmp[j]=='.') state[i][j]=0;
			else if(tmp[j]=='X') state[i][j]=1;
			else if(tmp[j]=='O') state[i][j]=2;
			else state[i][j]=3;
		}
	}
}

int judge()
{
	int cnt[4];
	for(int i=0;i<4;i++)
	{
		//row
		for(int j=0;j<4;j++) cnt[j]=0;
		for(int j=0;j<4;j++) cnt[state[i][j]]++;
		if(cnt[1]==4 || cnt[1]==3 && cnt[3]==1) return 1;
		if(cnt[2]==4 || cnt[2]==3 && cnt[3]==1) return 2;
		//column
		for(int j=0;j<4;j++) cnt[j]=0;
		for(int j=0;j<4;j++) cnt[state[j][i]]++;
		if(cnt[1]==4 || cnt[1]==3 && cnt[3]==1) return 1;
		if(cnt[2]==4 || cnt[2]==3 && cnt[3]==1) return 2;
	}
	//diagonal
	for(int j=0;j<4;j++) cnt[j]=0;
	for(int j=0;j<4;j++) cnt[state[j][j]]++;
	if(cnt[1]==4 || cnt[1]==3 && cnt[3]==1) return 1;
	if(cnt[2]==4 || cnt[2]==3 && cnt[3]==1) return 2;
	
	for(int j=0;j<4;j++) cnt[j]=0;
	for(int j=0;j<4;j++) cnt[state[j][3-j]]++;
	if(cnt[1]==4 || cnt[1]==3 && cnt[3]==1) return 1;
	if(cnt[2]==4 || cnt[2]==3 && cnt[3]==1) return 2;
	
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++) if(state[i][j]==0) return 0;
	return 3;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		init();
		printf("Case #%d: ",i+1);
		int ans = judge();
		if(ans==1) printf("X won\n");
		else if(ans==2) printf("O won\n");
		else if(ans==3) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
