#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;

const int MAX_LEN = 50 ;
void SquareTiles(int line ,ifstream& input, ofstream& output);
int main()
{
	long start = GetTickCount();
	ifstream input("A-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("A-large.out",ios::out);
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	for (i=0;i<lines;i++)
	{
		SquareTiles(i,input,output);
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}
void SquareTiles(int line ,ifstream& input, ofstream& output)
{
	int rows ,cols  , i ,j ;
	input>>rows >>cols;
	char tiles[MAX_LEN][MAX_LEN];
	for(i=0;i <rows ;i++)
	{
		for(j=0; j< cols ; j++)
		{
			input>>tiles[i][j];		
		}	
	}

	bool possible = true ;
	for(i=0;i <rows ;i++)
	{
		if(!possible)
			break ;
		for(j=0; j< cols ; j++)
		{
			if(tiles[i][j] =='#')
			{
				if( (i ==rows-1)||(j==cols-1 ))
				{
					possible = false ;
					break ;
				}
				else if( tiles[i][j+1]=='.' || tiles[i+1][j]=='.' ||  tiles[i+1][j+1]=='.')
				{
							possible = false ;
							break ;
				}
				else 
				{
					tiles[i][j] = tiles[i+1][j+1] ='/' ;
					tiles[i+1][j] = tiles[i][j+1]= '\\'  ;
				}
			}//end of if(tiles[i][j] =='#')
		}// end of for j
	}// end of for i
	
	output<<"Case #"<<line+1<<":\n";
	if(!possible)
		output<<"Impossible\n";
	else
	for(i=0;i <rows ;i++)
	{
		for(j=0; j< cols ; j++)
		{
			output<<tiles[i][j];		
		}	
		output<<"\n" ;
	}


}
