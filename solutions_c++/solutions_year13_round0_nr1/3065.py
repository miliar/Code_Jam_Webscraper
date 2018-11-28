#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string check(int** s)
{
	
	string result;
	int i,j,sum;
	bool dotflag=false;
	
	
	//horizontal
	
	for (i=0;i<4;i++)
	{ 
		sum=0;	
		for (j=0;j<4;j++)
			sum+=s[i][j];

		if (sum>100)
			dotflag=true;
		else if (sum==0 ||sum==10)
			return "O won";
		else if (sum==4 ||sum==13)
			return "X won";
			
	}
		
	//vertical
	
	for (i=0;i<4;i++)
	{ 
		sum=0;		
		for (j=0;j<4;j++)
			sum+=s[j][i];

		if (sum>100)
			dotflag=true;
		else if (sum==0 ||sum==10)
			return "O won";
		else if (sum==4 ||sum==13)
			return "X won";
			
	}

		//diagonal
	sum=0;	
	for (i=0;i<4;i++)
	{ 
		
		
		sum+=s[i][i];
		
	}
		if (sum>100)
			dotflag=true;
		else if (sum==0 ||sum==10)
			return "O won";
		else if (sum==4 ||sum==13)
			return "X won";

	sum=0;		
	for (i=0;i<4;i++)
	{ 
		
			
		sum+=s[i][3-i];
		
	}
		if (sum>100)
			dotflag=true;
		else if (sum==0 ||sum==10)
			return "O won";
		else if (sum==4 ||sum==13)
			return "X won";
   
    if (dotflag)
		return "Game has not completed";
	else
		return "Draw";
	}

int main()
{
	//ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
	int T;
	fin>>T;

	//ofstream fout("A-small-attempt0.out");
	ofstream fout("A-large.out");	
		
	
	//char **s = new char*[4];
	string *s=new string[4];
	int **map = new int*[4];

	for(int i = 0; i < 4; ++i) 
	{
      
	   map[i] = new int[4];
	}

	
	

	string result;
	
	for (int t=0;t<T;t++)
	{
		
		for (int i=0;i<4;i++)
		{
			fin>>s[i];
				for (int j=0;j<4;j++)
				{
					
		         if (s[i][j]=='X')
					 map[i][j]=1;
				 else if (s[i][j]=='O')
					 map[i][j]=0;
				 else if (s[i][j]=='T')

                      map[i][j]=10;
				 else
                       map[i][j]=100;
		         }
			
		}

	
		result=check(map);
		fout<<"Case #"<<t+1<<": "<<result<<endl;
		
	}
	
	for(int i = 0; i < 4; ++i) 
	{
		
		delete [] map[i];
     }

	
	delete [] s;
	delete [] map;
	
	return 0;
}