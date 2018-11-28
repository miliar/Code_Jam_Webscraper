#include <iostream>
#include <fstream>
using namespace std;
char Matrix[4][4];
int X,O,Dot,Draw;
unsigned int Test_Cases;

void read_test_cases(void);
void Check(unsigned int);
void Explore_Rows(void);
void Explore_Columns(void);
void Explore_D(void);

main()
{
	read_test_cases();



}

void read_test_cases(void)
{
	ifstream fin("A.in");
	fin >> Test_Cases ;
	unsigned int Number_of_iterations;
	int i,j;
	for(Number_of_iterations=0;Number_of_iterations<Test_Cases;Number_of_iterations++)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fin >>Matrix[i][j];
			}
		}
		Check(Number_of_iterations+1);
	}
}

void Check(unsigned int Case)
{
		X=0;
		O=0;
		Dot=0;
		Draw=0;
		Explore_Rows();
		if(X==1)
		{
			cout<<"Case #"<<Case<<": X won\n";
			return;
		}
		if(O==1)
		{
			cout<<"Case #"<<Case<<": O won\n";
			return;
		}
		Explore_Columns();
		if(X==1)
		{
			cout<<"Case #"<<Case<<": X won\n";
			return;
		}
		if(O==1)
		{
			cout<<"Case #"<<Case<<": O won\n";
			return;
		}
		Explore_D();
		if(X==1)
		{
			cout<<"Case #"<<Case<<": X won\n";
			return;
		}
		if(O==1)
		{
			cout<<"Case #"<<Case<<": O won\n";
			return;
		}
				
		

		if(Dot==1)
		{
			cout<<"Case #"<<Case<<": Game has not completed\n";
			return;
		}
		if(Dot==0)
		{
			cout<<"Case #"<<Case<<": Draw\n";
			return;
		}
		
}

void Explore_D(void)
{
	int i,j;
	int fail;
	char First;
		fail=1;
		First=Matrix[0][0];
		if(First=='.')
		{
			Dot=1;
		}
		else
		{
			if(First=='T')
			{
				First=Matrix[1][1];
				for(j=2;j<4;j++)
				{
					
					if(Matrix[j][j]!=First && Matrix[j][j]!='T')
						fail=0;
				}
				
			}
			else
			{
				for(j=1;j<4;j++)
				{
					if(Matrix[j][j]!=First && Matrix[j][j]!='T')
						fail=0;
				}
			}
			if(fail==1)
			{
				if(First=='X')
					X=1;
				if(First=='O')
					O=1;
				return;
			}
		}	
		


		fail=1;
		First=Matrix[0][3];
		if(First=='.')
		{
			Dot=1;
		}
		else
		{
			if(First=='T')
			{
				First=Matrix[1][2];
				for(j=2;j<4;j++)
				{
					if(Matrix[j][3-j]!=First && Matrix[j][3-j]!='T')
						fail=0;
				}
				
			}
			else
			{
				for(j=1;j<4;j++)
				{
					if(Matrix[j][3-j]!=First && Matrix[j][3-j]!='T')
						fail=0;
				}
			}
			if(fail==1)
			{
				if(First=='X')
					X=1;
				if(First=='O')
					O=1;
				return;
			}
		}	
		
}


void Explore_Columns(void)
{
	int i,j;
	int fail;
	char First;
	for(i=0;i<4;i++)
	{
		fail=1;
		First=Matrix[0][i];
		if(First=='.')
		{
			Dot=1;
		}
		else
		{
			if(First=='T')
			{
				First=Matrix[1][i];
				for(j=2;j<4;j++)
				{
					if(Matrix[j][i]=='.') Dot=1;
					if(Matrix[j][i]!=First && Matrix[j][i]!='T')
						fail=0;
				}
				
			}
			else
			{
				for(j=1;j<4;j++)
				{
					if(Matrix[j][i]=='.') Dot=1;
					if(Matrix[j][i]!=First && Matrix[j][i]!='T')
						fail=0;
				}
			}
			if(fail==1)
			{
				if(First=='X')
					X=1;
				if(First=='O')
					O=1;
				return;
			}
		}	
	}
}


void Explore_Rows(void)
{
	int i,j;
	int fail;
	char First;
	for(i=0;i<4;i++)
	{
		fail=1;
		First=Matrix[i][0];
		if(First=='.')
		{
			Dot=1;
		}
		else
		{
			if(First=='T')
			{
				First=Matrix[i][1];
				for(j=2;j<4;j++)
				{
					if(Matrix[i][j]=='.') Dot=1;
					if(Matrix[i][j]!=First && Matrix[i][j]!='T')
						fail=0;
				}
				
			}
			else
			{
				for(j=1;j<4;j++)
				{
					if(Matrix[i][j]=='.') Dot=1;
					if(Matrix[i][j]!=First && Matrix[i][j]!='T')
						fail=0;
				}
			}
			if(fail==1)
			{
				if(First=='X')
					X=1;
				if(First=='O')
					O=1;
				return;
			}
		}	
	}
}
