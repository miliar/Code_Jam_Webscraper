#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main () {
	string line;
	int noOfCase,array[4][4];
	char tempChar;
	  
	ifstream myfile ("A-large.in");
	if (myfile.is_open())
	{   
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{
			int count=0;
			for(int i=0;i<4;i++){
				getline(myfile,line);
				for(int j=0;j<4;j++)
				{
					tempChar=line[j];
					
					// tempChar=toupper(tempChar);
					if (tempChar=='.')
					{
						array[i][j]=0;
						count++;
					}
					if (tempChar=='X')
						array[i][j]=2;
					if (tempChar=='T')
						array[i][j]=1;
					if (tempChar=='O')
						array[i][j]=-2;
				}
			}

			// check diagonal
			int sumdig1=0,sumdig2=0;
			bool gameEnded=false;
			for (int r=0;r<4;r++)
			{
				sumdig1+=array[r][r];
				sumdig2+=array[3-r][r];				
			}
			
			if((sumdig1>6)||(sumdig1<-6)||(sumdig1==-5))
			{	
				if (sumdig1	> 0)
				{
					cout<<"Case #"<<k+1<<": "<<"X won"<<endl;			
					myfileOut<<"Case #"<<k+1<<": "<<"X won"<<endl;
					gameEnded=true;
				}
				else
				{
					cout<<"Case #"<<k+1<<": "<<"O won"<<endl;			
					myfileOut<<"Case #"<<k+1<<": "<<"O won"<<endl;
					gameEnded=true;
				}
			}
			else{
				if((sumdig2>6)||(sumdig2<-6)||(sumdig2==-5))
				{	
					if (sumdig2	> 0)
					{
						cout<<"Case #"<<k+1<<": "<<"X won"<<endl;			
						myfileOut<<"Case #"<<k+1<<": "<<"X won"<<endl;
						gameEnded=true;
					}
					else
					{
						cout<<"Case #"<<k+1<<": "<<"O won"<<endl;			
						myfileOut<<"Case #"<<k+1<<": "<<"O won"<<endl;
						gameEnded=true;
					}
				}
			}
			
			if (!gameEnded)
			{
				// check vertical and horizontal
				for(int p=0;p<4;p++)
				{
					int sumver=0,sumhor=0;
					for(int q=0;q<4;q++)
					{
						sumver+=array[p][q];
						sumhor+=array[q][p];
					}
					if((sumver>6)||(sumver<-6)||(sumver==-5))
					{	
						if (sumver	> 0)
						{
							cout<<"Case #"<<k+1<<": "<<"X won"<<endl;			
							myfileOut<<"Case #"<<k+1<<": "<<"X won"<<endl;
							gameEnded=true;
							break;
						}
						else
						{
							cout<<"Case #"<<k+1<<": "<<"O won"<<endl;			
							myfileOut<<"Case #"<<k+1<<": "<<"O won"<<endl;
							gameEnded=true;
							break;
						}
					}
					else 
					{
						if((sumhor>6)||(sumhor<-6)||(sumhor==-5))
						{
							if (sumhor	> 0)
							{
								cout<<"Case #"<<k+1<<": "<<"X won"<<endl;			
								myfileOut<<"Case #"<<k+1<<": "<<"X won"<<endl;
								gameEnded=true;
								break;
							}
							else
							{
								cout<<"Case #"<<k+1<<": "<<"O won"<<endl;			
								myfileOut<<"Case #"<<k+1<<": "<<"O won"<<endl;
								gameEnded=true;
								break;
							}
						}
					}
				}
				if (!gameEnded)
				{
					if (count==0)
					{
						cout<<"Case #"<<k+1<<": "<<"Draw"<<endl;			
						myfileOut<<"Case #"<<k+1<<": "<<"Draw"<<endl;
					}
					else
					{
						cout<<"Case #"<<k+1<<": "<<"Game has not completed"<<endl;			
						myfileOut<<"Case #"<<k+1<<": "<<"Game has not completed"<<endl;
					}
				}
			}
			getline(myfile,line);
		}
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}