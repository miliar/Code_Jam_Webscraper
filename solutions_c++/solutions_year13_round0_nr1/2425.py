#include <stdlib.h>
#include <fstream>
using namespace std;

int main ()
{
	ifstream R("a1.in");
    ofstream W("a1.out");
    
    int t;
    R>>t;
    for (int ti=1;ti<=t;++ti)
    {
		char stat[4][4],space;
		int posx,posy;
		int winner=0;
    	for(int i=0;i<4;++i)
    	{
    		for(int j=0;j<4;++j)
    		{
    			R>>stat[i][j];
    			if(stat[i][j]=='T')
    			{
    				posx=i;
    				posy=j;
    				stat[i][j]='X';
    			}
    		}
    	}
    	//for(int i=0;i<4;++i)
    	//	for(int j=0;j<4;++j)
    	//		W<<stat[i][j];
    	//W<<endl;
    	
    	
    	
    	if(stat[0][0]==stat[0][1] && stat[0][0]==stat[0][2] && stat[0][0]==stat[0][3]&&stat[0][0]=='X'){winner=1;}
    	if(stat[1][0]==stat[1][1] && stat[1][0]==stat[1][2] && stat[1][0]==stat[1][3]&&stat[1][0]=='X'){winner=1;}
    	if(stat[2][0]==stat[2][1] && stat[2][0]==stat[2][2] && stat[2][0]==stat[2][3]&&stat[2][0]=='X'){winner=1;}
    	if(stat[3][0]==stat[3][1] && stat[3][0]==stat[3][2] && stat[3][0]==stat[3][3]&&stat[3][0]=='X'){winner=1;}
    	if(stat[0][0]==stat[1][0] && stat[0][0]==stat[2][0] && stat[0][0]==stat[3][0]&&stat[0][0]=='X'){winner=1;}
    	if(stat[0][1]==stat[1][1] && stat[0][1]==stat[2][1] && stat[0][1]==stat[3][1]&&stat[0][1]=='X'){winner=1;}
    	if(stat[0][2]==stat[1][2] && stat[0][2]==stat[2][2] && stat[0][2]==stat[3][2]&&stat[0][2]=='X'){winner=1;}
    	if(stat[0][3]==stat[1][3] && stat[0][3]==stat[2][3] && stat[0][3]==stat[3][3]&&stat[0][3]=='X'){winner=1;}
    	if(stat[0][0]==stat[1][1] && stat[0][0]==stat[2][2] && stat[0][0]==stat[3][3]&&stat[0][0]=='X'){winner=1;}
    	if(stat[0][3]==stat[1][2] && stat[0][3]==stat[2][1] && stat[0][3]==stat[3][0]&&stat[0][3]=='X'){winner=1;}
    	if(winner==1)
    	{
    		W<<"Case #"<<ti<<": X won"<<endl;
    		continue;
    	}
    	stat[posx][posy]='O';
    	if(stat[0][0]==stat[0][1] && stat[0][0]==stat[0][2] && stat[0][0]==stat[0][3]&&stat[0][0]=='O'){winner=2;}
    	if(stat[1][0]==stat[1][1] && stat[1][0]==stat[1][2] && stat[1][0]==stat[1][3]&&stat[1][0]=='O'){winner=2;}
    	if(stat[2][0]==stat[2][1] && stat[2][0]==stat[2][2] && stat[2][0]==stat[2][3]&&stat[2][0]=='O'){winner=2;}
    	if(stat[3][0]==stat[3][1] && stat[3][0]==stat[3][2] && stat[3][0]==stat[3][3]&&stat[3][0]=='O'){winner=2;}
    	if(stat[0][0]==stat[1][0] && stat[0][0]==stat[2][0] && stat[0][0]==stat[3][0]&&stat[0][0]=='O'){winner=2;}
    	if(stat[0][1]==stat[1][1] && stat[0][1]==stat[2][1] && stat[0][1]==stat[3][1]&&stat[0][1]=='O'){winner=2;}
    	if(stat[0][2]==stat[1][2] && stat[0][2]==stat[2][2] && stat[0][2]==stat[3][2]&&stat[0][2]=='O'){winner=2;}
    	if(stat[0][3]==stat[1][3] && stat[0][3]==stat[2][3] && stat[0][3]==stat[3][3]&&stat[0][3]=='O'){winner=2;}
    	if(stat[0][0]==stat[1][1] && stat[0][0]==stat[2][2] && stat[0][0]==stat[3][3]&&stat[0][0]=='O'){winner=2;}
    	if(stat[0][3]==stat[1][2] && stat[0][3]==stat[2][1] && stat[0][3]==stat[3][0]&&stat[0][3]=='O'){winner=2;}
    	if(winner==2)
    	{
    		W<<"Case #"<<ti<<": O won"<<endl;
    		continue;
    	}
    	for(int i=0;i<4;++i)
    		for(int j=0;j<4;++j)
    			if(stat[i][j]=='.')
    				winner=3;
    	if(winner==3)
       	{
    		W<<"Case #"<<ti<<": Game has not completed"<<endl;
    		continue;
    	}
    	W<<"Case #"<<ti<<": Draw"<<endl;
	}
}
