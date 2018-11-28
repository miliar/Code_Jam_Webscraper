#include<iostream>
#include<stdio.h>
using namespace std;
char a[4][4];
int xwin()
{
    for(int i=0;i<4;i++)
    {
    	if((a[i][0]=='T' || a[i][0]=='X') && (a[i][1]=='T' || a[i][1]=='X') && (a[i][2]=='T' || a[i][2]=='X') && (a[i][3]=='T' || a[i][3]=='X'))
        return 2;
    }
    for(int i=0;i<4;i++)
    {
    	if((a[0][i]=='T' || a[0][i]=='X') && (a[1][i]=='T' || a[1][i]=='X') && (a[2][i]=='T' || a[2][i]=='X') && (a[3][i]=='T' || a[3][i]=='X'))
        {return 2;}
    }
    if((a[0][0]=='T' || a[0][0]=='X') && (a[1][1]=='T' || a[1][1]=='X') && (a[2][2]=='T' || a[2][2]=='X') && (a[3][3]=='T' || a[3][3]=='X'))
   		return 2;
    if((a[3][0]=='T' || a[3][0]=='X') && (a[2][1]=='T' || a[2][1]=='X') && (a[1][2]=='T' || a[1][2]=='X') && (a[0][3]=='T' || a[0][3]=='X'))
		return 2;
    
	return 0;        
}
int owin()
{
    for(int i=0;i<4;i++)
    {
    	if((a[i][0]=='T' || a[i][0]=='O') && (a[i][1]=='T' || a[i][1]=='O') && (a[i][2]=='T' || a[i][2]=='O') && (a[i][3]=='T' || a[i][3]=='O'))
        	return 3;
    }
    for(int i=0;i<4;i++)
    {
    	if((a[0][i]=='T' || a[0][i]=='O') && (a[1][i]=='T' || a[1][i]=='O') && (a[2][i]=='T' || a[2][i]=='O') && (a[3][i]=='T' || a[3][i]=='O'))
        	return 3;
    }
    if((a[0][0]=='T' || a[0][0]=='O') && (a[1][1]=='T' || a[1][1]=='O') && (a[2][2]=='T' || a[2][2]=='O') && (a[3][3]=='T' || a[3][3]=='O'))
    	return 3;
    if((a[3][0]=='T' || a[3][0]=='O') && (a[2][1]=='T' || a[2][1]=='O') && (a[1][2]=='T' || a[1][2]=='O') && (a[0][3]=='T' || a[0][3]=='O'))
    	return 3;
    
	return 0;        
}
int main()
{
    int t,count;
    cin>>t;
	count=1;
    while(t--)
    {
                 int w=0;
                 cin>>a[0];
                 cin>>a[1];
                 cin>>a[2];
                 cin>>a[3];
                 if(w==0)
				 	 w=xwin();
                 if(w==0)
				 	 w=owin();
                 if(w==0)
                 {
                    for(int i=0;i<4;i++)
                 		for(int j=0;j<4;j++)
                 			if(a[i][j]=='.') 
							{
								w=1;break;
							}
                 }
                 if(w==1) 
				 	printf("Case #%d: Game has not completed\n",count);
                 if(w==2) 
				 	printf("Case #%d: X won\n",count);
                 if(w==3) 
				 	printf("Case #%d: O won\n",count);
                 if(w==0) 
				 	printf("Case #%d: Draw\n",count); 
                 count++;
    }
    return 0;
}
 
