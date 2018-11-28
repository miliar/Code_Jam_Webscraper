#include<iostream>
using namespace std;

#define ROW 4
#define COL 5

char T[5][COL]={
					{"XXXT"},
					{"XXTX"},
					{"XTXX"},
					{"TXXX"},
					{"XXXX"}
				};
char O[5][COL]={
					{"OOOT"},
					{"OOTO"},
					{"OTOO"},
					{"TOOO"},
					{"OOOO"}
				};
int checkH(char *matrix)//, char ch)
{
	if(strstr(matrix,"X")!=NULL)
	{
		for(int j=0;j<5;j++)	// for hoirzontal
		{
			if(strcmp(matrix,T[j])==0)
			{
				cout<<"X won"<<endl;
				return 1;
			}
		}
	}
	else
	{
		for(int j=0;j<5;j++)	// for hoirzontal
		{
			if(strcmp(matrix,O[j])==0)
			{
				cout<<"O won"<<endl;
				return 1;
			}
		}
	}

	return 0;
}


void data()
{
	char matrix[ROW][COL]={0};
	bool empty=false;
	bool win=false;
	char diag[2][5]={0};
	char vert[ROW][COL]={0};

	for (int i=0; i<4;i++)
	{

		cin>>matrix[i];
		//cout<<"line: ["<<matrix[i]<<"]"<<endl;

		if(empty==false)
		if(strstr(matrix[i],".")!=NULL)
		{
			empty=true;
		}

		if(win==false)
		{
			if( checkH(matrix[i]) == 1)
			{
				win=true;
				continue;
			}
			else
				win=false;
		}
	}

	if(win==false)
	{
	/* Filling diag1 and diag2 */
	diag[0][0]=matrix[0][0];
	diag[0][1]=matrix[1][1];
	diag[0][2]=matrix[2][2];
	diag[0][3]=matrix[3][3];

	diag[1][0]=matrix[0][3];
	diag[1][1]=matrix[1][2];
	diag[1][2]=matrix[2][1];
	diag[1][3]=matrix[3][0];

	for(int i =0 ;i<2;i++)
	{
			if(checkH(diag[i]) == 1)
			{
				win=true;
				break;
			}
			else
				win=false;
	}

	}

	if(win==false)
	{
		for (int i=0;i<4;i++)
		{
			vert[i][0]=matrix[0][i];
			vert[i][1]=matrix[1][i];
			vert[i][2]=matrix[2][i];
			vert[i][3]=matrix[3][i];
			//vert[i][0]=matrix[0][i];

			if(checkH(vert[i]) == 1)
			{
				win=true;
				break;
			}
			else
				win=false;
		}

	}

	if(win==false && empty==false)
	{
		cout<<"Draw"<<endl;
	}
	else if (win == false && empty == true)
		cout<<"Game has not completed"<<endl;

//return 0;
}




int main()
{
int t=0;	// testcase

cin>>t;
//cout<<t<<endl;
for(int i=1;i<=t;i++)
{
	cout<<"Case #"<<i<<": ";
	data();
}

return 0;

}
