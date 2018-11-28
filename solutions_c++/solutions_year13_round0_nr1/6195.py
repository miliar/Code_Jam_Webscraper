#include <iostream>
#include <fstream>
#include <sstream>


using namespace std;

int main()
{
	int cases;
	char grid[4][4],won,over,first_r,first_c,first_d;
	bool check,empty;
	string line;
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int i=0; i < cases ; i++)
	{
		int count_r=0,count_c=0,count_d_f=0,count_d_r=0,frwd_d=0,rev_d=0;
		check=false,empty=false;
		won='n',over='n';
		for(int j=0; j<5;j++)
		{
			getline(cin,line);
			if (j<4)
			{
				for (int k = 0; k < 4; k++)
				{
					grid[j][k]=line[k];
				}
			}
		}
		/*for (int c = 0; c < 10 && !check; c++)
		{
		bool t=false;*/
		for (int a = 0; a < 4 && !check; a++)
		{
			int count_r=0,count_c=0,count_d=0;

			for (int b = 0; b < 4 && !check; b++)
			{
				if(grid[a][0]!='T')
				{
					first_r=grid[a][0];
				}
				else
				{
					first_r=grid[a][1];
				}

				if ((grid[a][b]==first_r || grid[a][b]=='T') && (grid[a][b]!='.'))
				{
					//printf("a=%d b=%d count=%d ",a,b,count_r);
					count_r++;
				}
				if (count_r==4 )
				{
					won=first_r;
					over='y';
					check=true;

				}
				if(grid[a][b]=='.')
				{	
					empty=true;
				}
				/*if (a==3 && b==3)
				{
				if (won!= )
				{

				}
				}*/
			}
			for (int b = 0; b < 4 && !check; b++)
			{
				if(grid[0][a]!='T')
				{

					first_c=grid[0][a];
				}
				else
				{	
					first_c=grid[1][a];
				}
				if ((grid[b][a]==first_c || grid[b][a]=='T') && (grid[b][a]!='.'))
				{
					count_c++;
				}
				if (count_c==4 )
				{

					won=first_c;
					over='y';
					check=true;

				}
				if(grid[b][a]=='.')
				{	
					empty=true;
				}
			}
			for (int b=0; b < 4 && !check; b++)
			{
				if (a-b==0)
				{
					if(grid[0][0]!='T')
					{
						frwd_d=grid[0][0];
					}
					else
					{
						frwd_d=grid[1][1];
					}
					if ((grid[a][a]==frwd_d || grid[a][a]=='T') && (grid[a][a]!='.'))
					{
						//printf("a=%d b=%d count=%d ",a,b,count_r);
						count_d_f++;
					}
					if (count_d_f==4 )
					{
						won=frwd_d;
						over='y';
						check=true;

					}
					if(grid[a][a]=='.')
					{	
						empty=true;
					}
				}
				if (a+b==3)
				{
					if(grid[0][3]!='T')
					{
						rev_d=grid[0][3];
					}
					else
					{
						rev_d=grid[1][2];
					}

					if ((grid[a][b]==rev_d || grid[a][b]=='T') && (grid[a][b]!='.'))
					{
						//printf("a=%d b=%d count=%d ",a,b,count_r);
						count_d_r++;
					}
					if (count_d_r==4 )
					{
						won=rev_d;
						over='y';
						check=true;

					}
					if(grid[a][a]=='.')
					{	
						empty=true;
					}
				}
			}

		}

		cout<<"Case #"<<i+1<<": ";

		if (won == 'X' || won == 'O')
		{
			if (won=='X')
			{
				cout<<"X won\n";
			}
			if (won=='O')
			{
				cout<<"O won\n";
			}
		}
		else if (empty)
		{
			cout<<"Game has not completed\n";
		}
		else
		{
			cout<<"Draw\n";
		}

	}
	return 0;
}