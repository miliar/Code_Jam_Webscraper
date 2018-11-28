#include <iostream>
using namespace std;

int Judge(int m[4][4],bool full)
{
	for(int i=0;i<4;i++)
	{
		int row=m[i][0]+m[i][1]+m[i][2]+m[i][3];
		if(row==4||row==103) return 1;
		if(row==32||row==124) return 2;
		row=m[0][i]+m[1][i]+m[2][i]+m[3][i];
		if(row==4||row==103) return 1;
		if(row==32||row==124) return 2;
	}
	int row=m[0][0]+m[1][1]+m[2][2]+m[3][3];
	if(row==4||row==103) return 1;
	if(row==32||row==124) return 2;
	row=m[0][3]+m[1][2]+m[2][1]+m[3][0];
	if(row==4||row==103) return 1;
	if(row==32||row==124) return 2;
	if(full) return 3;
	
	return 0;
}


int main()
{	
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	int map[4][4];
	int ans;
	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		memset(map,0,sizeof(int)*16);
		printf("Case #%d: ",case_id);
		bool isfull=true;
		for (int i=0;i<4;i++) 
		{
			
			for(int j=0;j<4;j++)
			{
				char tmp='.';
				cin>>tmp;
				if(tmp=='X') map[i][j]=1;
				if(tmp=='O') map[i][j]=8;
				if(tmp=='T') map[i][j]=100;
				if(tmp=='.') isfull=false;
			}
		}
		ans=Judge(map,isfull);
		if(ans==1)
			printf("%s","X won");
		else if(ans==2)
			printf("%s","O won");
		else if(ans==3)
			printf("%s","Draw");
		else
			printf("%s","Game has not completed");
		printf("\n");
	}

	return 0;
}

