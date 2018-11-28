#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>

using namespace std;


int main()
{
    int num;
	cin>>num;
	
	char a[4][4];
	
	for(int p=0;p<num;p++)
	{
				
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
                cin>>a[i][j];
			}
		}
		
		int fw=1,k=0,i,j;
				
		while(fw&&k<4)
		{
			if(a[k][k]=='X'||a[k][k]=='T'){}
			else fw=0;
			k++;
		}
		
		if(fw){cout<<"Case #"<<p+1<<": "<<"X won"<<endl;continue;}
        
        fw=1;i=0;j=3;
        while(fw&&i<4)
        {
            if(a[i][j]=='X'||a[i][j]=='T'){}
            else fw=0;
            i++;j--;
        }
		
    	if(fw){cout<<"Case #"<<p+1<<": "<<"X won"<<endl;continue;}
        
        k=0;fw=1;
		while(fw&&k<4)
		{
			if(a[k][k]=='O'||a[k][k]=='T'){}
			else fw=0;
			k++;
		}
		
		if(fw){cout<<"Case #"<<p+1<<": "<<"O won"<<endl;continue;}
        
        fw=1;i=0;j=3;
        while(fw&&i<4)
        {
            if(a[i][j]=='O'||a[i][j]=='T'){}
            else fw=0;
            i++;j--;
        }
    	
    	if(fw){cout<<"Case #"<<p+1<<": "<<"O won"<<endl;continue;}
		
		int flagX=0,flagO=0,flagD=0;
		
		for(i=0;i<4;i++)
		{	
			for(j=0;j<4;j++)
			{
				if(a[i][j]=='X'||a[i][j]=='T')flagX++;
						
				if(a[i][j]=='O'||a[i][j]=='T')flagO++;
						
				if(a[i][j]=='.')flagD=1;
			}
			
			if(flagX==4)break;
			if(flagO==4)break;
			flagX=0;flagO=0;
		}
				
		if(flagX==4){cout<<"Case #"<<p+1<<": "<<"X won"<<endl;continue;}
		else if(flagO==4){cout<<"Case #"<<p+1<<": "<<"O won"<<endl;continue;}
				
		flagX=0;flagO=0;
		
        
        
		for(j=0;j<4;j++){
		for(i=0;i<4;i++)
		{
            
            if(a[i][j]=='X'||a[i][j]=='T')flagX++;
						
			if(a[i][j]=='O'||a[i][j]=='T')flagO++;
		}
            if(flagX==4)break;
			if(flagO==4)break;
			flagX=0;flagO=0;
		}
			
		if(flagX==4){cout<<"Case #"<<p+1<<": "<<"X won"<<endl;continue;}
		else if(flagO==4){cout<<"Case #"<<p+1<<": "<<"O won"<<endl;continue;}	
			
		else if(flagD){cout<<"Case #"<<p+1<<": "<<"Game has not completed"<<endl;continue;}
		else {cout<<"Case #"<<p+1<<": "<<"Draw"<<endl;continue;}		
		
	}
}
			
