#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	
	string line;
  	ifstream myfile ("input.txt");
  	ofstream myOutfile;
  	myOutfile.open ("output.txt");
  	
  	int totalCases = 0;
  	
  	myfile>>totalCases;
  	
  	for(int loop=0; loop<totalCases; loop++)
  	{
  		char myData[4][4];
  		
  		for(int i=0; i<4; i++)
  		{
  			for(int j=0; j<4; j++)
  			{
  				myfile>>myData[i][j];
  				//cout<<myData[i][j];
  			}
  			//cout<<"\n";
	 	}  
  		bool matchInProgress = 0;
  		bool xWon = 0;
  		bool oWon = 0;
  		
  		for(int i=0; i<4; i++)
  		{
  			char firstCharInRow = myData[i][0];
  			
  			if(firstCharInRow == '.')
  			{
  				matchInProgress = 1;
  			}
  			else
  			{
  				for(int j=1; j<4; j++)
  				{
  					if(myData[i][j]== '.')
  					{
  						matchInProgress = 1;
  						break;
  					}
  					
  					if(firstCharInRow == 'T')
  					{
  						firstCharInRow = myData[i][j];
  					}  					
  					else if(myData[i][j]==firstCharInRow || myData[i][j]== 'T')
  					{
  						if(j==3)
  						{
  							if(firstCharInRow=='O')
  							{
  								oWon = 1;
  							}
  							if(firstCharInRow=='X')
  							{
  								xWon = 1;
  							}	
  						}
  					}
  					else if(myData[i][j]!=firstCharInRow)
  					{
  						break;
  					}
  				}
  				
  				if(!xWon && !oWon)
  				{
  					if(i==0)
  					{
  						firstCharInRow = myData[i][0];
  						
  						for(int j=1; j<4; j++)
	  					{
		  					if(myData[j][j]== '.')
		  					{
		  						matchInProgress = 1;
		  						break;
		  					}
		  					
		  					if(firstCharInRow == 'T')
		  					{
		  						firstCharInRow = myData[j][j];
		  					}  					
		  					else if(myData[j][j]==firstCharInRow || myData[j][j]== 'T')
		  					{
		  						if(j==3)
		  						{
		  							if(firstCharInRow=='O')
		  							{
		  								oWon = 1;
		  							}
		  							if(firstCharInRow=='X')
		  							{
		  								xWon = 1;
		  							}	
		  						}
		  					}
		  					else if(myData[j][j]!=firstCharInRow)
		  					{
		  						break;
		  					}
		  				}
		  				
		  				if(!xWon && !oWon)
		  				{
		  					firstCharInRow = myData[i][3];
		  					
		  					for(int j=3; j>=0; j--)
		  					{
		  						int ii= 3-j;
		  						
			  					if(myData[ii][j]== '.')
			  					{
			  						matchInProgress = 1;
			  						break;
			  					}
			  					
			  					if(firstCharInRow == 'T')
			  					{
			  						firstCharInRow = myData[ii][j];
			  					}  					
			  					else if(myData[ii][j]==firstCharInRow || myData[ii][j]== 'T')
			  					{
			  						if(j==0)
			  						{
			  							if(firstCharInRow=='O')
			  							{
			  								oWon = 1;
			  							}
			  							if(firstCharInRow=='X')
			  							{
			  								xWon = 1;
			  							}	
			  						}
			  					}
			  					else if(myData[ii][j]!=firstCharInRow)
			  					{
			  						break;
			  					}
			  				}
		  					
		  				}
		  				
		  				if(!xWon && !oWon)
		  				{
		  					for(int j=0; j<4; j++)
		  					{
		  						firstCharInRow = myData[i][j];
  						
		  						for(int ii=1; ii<4; ii++)
			  					{
				  					if(myData[ii][j]== '.')
				  					{
				  						matchInProgress = 1;
				  						break;
				  					}
				  					
				  					if(firstCharInRow == 'T')
				  					{
				  						firstCharInRow = myData[ii][j];
				  					}  					
				  					else if(myData[ii][j]==firstCharInRow || myData[ii][j]== 'T')
				  					{
				  						if(ii==3)
				  						{
				  							if(firstCharInRow=='O')
				  							{
				  								oWon = 1;
				  							}
				  							if(firstCharInRow=='X')
				  							{
				  								xWon = 1;
				  							}	
				  						}
				  					}
				  					else if(myData[ii][j]!=firstCharInRow)
				  					{
				  						break;
				  					}
				  				}
		  					}
		  					
		  				}
		  				
  					}
  					
  					
  				}
  				
  				
  				
  			}
  			
  			if(xWon || oWon)
  			{
  				break;
  			}
  		}
  		
  		if(xWon)
  		{
  			myOutfile << "Case #"<<loop+1<<": X won"<<endl;
  		}
  		else if(oWon)
  		{
  			myOutfile << "Case #"<<loop+1<<": O won"<<endl;
  		}
  		else if(matchInProgress)
	  	{
	  		myOutfile << "Case #"<<loop+1<<": Game has not completed"<<endl;
	  	}
	  	else
		{
	  		myOutfile << "Case #"<<loop+1<<": Draw"<<endl;
	  	}  		
  		
  	}
  	
  	myOutfile.close();
  	myfile.close();
/*  	while ( myfile.good() )
    {
   		getline (myfile,line);
   		cout << line << endl;
   	}
   	myfile.close();
	
	ofstream myfile;
  	myfile.open ("input.txt");
  	myfile << "Writing this to a file.\n";
  	myfile.close();*/
	return 0;
}
