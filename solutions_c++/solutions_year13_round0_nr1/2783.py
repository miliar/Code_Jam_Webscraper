#include<cstdio>
#include<vector>
#include<set>
#include<utility>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

int game[4][4];
int complete;

int check()
{
	int i,j;
	//For Diagonal 1
	if(game[0][0]==1||game[0][0] == 3)
		   if(game[1][1]==1||game[1][1] == 3)
		      if(game[2][2]==1||game[2][2] == 3)
			     if(game[3][3]==1||game[3][3] == 3)
				    return 1;

	if(game[0][0]==2||game[0][0] == 3)
		   if(game[1][1]==2||game[1][1] == 3)
		      if(game[2][2]==2||game[2][2] == 3)
			     if(game[3][3]==2||game[3][3] == 3)
				    return 2;

	//For Diagonal 2
	if(game[0][3]==1||game[0][3] == 3)
		   if(game[1][2]==1||game[1][2] == 3)
		      if(game[2][1]==1||game[2][1] == 3)
			     if(game[3][0]==1||game[3][0] == 3)
				    return 1;

	if(game[0][3]==2||game[0][3] == 3)
		   if(game[1][2]==2||game[1][2] == 3)
		      if(game[2][1]==2||game[2][1] == 3)
			     if(game[3][0]==2||game[3][0] == 3)
				    return 2;

	//For Rows
	for(i=0; i<4; i++)
	{
		if(game[i][0]==1||game[i][0] == 3)
		   if(game[i][1]==1||game[i][1] == 3)
		      if(game[i][2]==1||game[i][2] == 3)
			     if(game[i][3]==1||game[i][3] == 3)
				    return 1;

		if(game[i][0]==2||game[i][0] == 3)
		   if(game[i][1]==2||game[i][1] == 3)
		      if(game[i][2]==2||game[i][2] == 3)
			     if(game[i][3]==2||game[i][3] == 3)
				    return 2;

	}

	//For columns
	for(j=0;j<4;j++)
	{
		if(game[0][j]==1||game[0][j] == 3)
		   if(game[1][j]==1||game[1][j] == 3)
		      if(game[2][j]==1||game[2][j] == 3)
			     if(game[3][j]==1||game[3][j] == 3)
				    return 1;

		if(game[0][j]==2||game[0][j] == 3)
		   if(game[1][j]==2||game[1][j] == 3)
		      if(game[2][j]==2||game[2][j] == 3)
			     if(game[3][j]==2||game[3][j] == 3)
				    return 2;
	}

	//If there is a Draw or Not Complete case
	if(complete == 0)
		return 0;
	else
		return -1;
}

int main()
{
	int t,i,j,res,m;
	char ch,cr;
	FILE *ifp, *ofp;
    char outputFilename[] = "output.txt";

    ifp = fopen("input.in", "r");
	ofp = fopen(outputFilename, "w");

	fscanf(ifp, "%d", &t);

    m=1;
	while(t--)
	{
		memset(game,0,sizeof(game));
		complete=0;
        fscanf(ifp, "%c", &cr);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fscanf(ifp, "%c", &ch);
				if(ch=='O')
				   game[i][j] = 1;
				else if(ch == 'X')
				   game[i][j] = 2;
				else if(ch == '.')
				{   game[i][j]=0;
					complete = 1;
				}
				else if(ch == 'T')
				   game[i][j]=3;
			}
            fscanf(ifp,"%c", &cr);

		}
        res = check();
        fprintf(ofp, "Case #%d: ", m);
        m++;
        /* printf("\n");
        for(i=0; i<4; i++)
        {
            for(j=0; j<4;j++)
            {
                printf("%d ",game[i][j]);
            }
            printf("\n");
        } */

    		if(res == 1)
			   fprintf(ofp, "O won\n");
			else if(res==2)
				fprintf(ofp, "X won\n");
			else if(res == 0)
				fprintf(ofp, "Draw\n");
			else if( res== -1)
				fprintf(ofp, "Game has not completed\n");
	}

	return 0;
}
