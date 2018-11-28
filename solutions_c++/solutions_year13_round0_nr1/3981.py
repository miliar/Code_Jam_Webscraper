#include <iostream>
#define L 4
using namespace std;
char map[L+2][L+2];
bool check(char x)
{
	int i,j;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
			if (map[i][j]!=x&&map[i][j]!='T') break;
		if (j==4) return true;
		for (j=0;j<4;j++)
			if (map[j][i]!=x&&map[j][i]!='T') break;
		if (j==4) return true;
	}
	for (i=0;i<4;i++)
		if (map[i][i]!=x&&map[i][i]!='T') break;
	if (i==4) return true;
	for (i=0;i<4;i++)
		if (map[i][L-i-1]!=x&&map[i][L-i-1]!='T') break;
	if (i==4) return true;
	return false;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int N,i,j,k;
	bool visit[4][4],ans1=false,ans2=false;
	cin>>N;
	for (i=0;i<N;i++)
	{
		for (j=0;j<4;j++) cin>>map[j];
		ans1=check('X');
		ans2=check('O');
		cout<<"Case #"<<i+1<<": ";
		if (ans1&&!ans2)
		{
			cout<<"X won"<<endl;
			continue;
		}
		if (!ans1&&ans2)
		{
			cout<<"O won"<<endl;
			continue;
		}
		for (j=0;j<16;j++)
			if (map[j/4][j%4]=='.') break;
		if (j==16) cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}