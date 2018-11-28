#include<iostream>
#include<fstream>
#include<conio.h>

using namespace std;

int main()
{
    ifstream ifile;
    ofstream ofile;
    int n;
    int o=0,x=0,t=0,dot; 
    ifile.open("A-large.IN");
    ofile.open("output.txt");
    char A[4][4],win;
    ifile>>n;
    for(int i=0;i<n;i++)
    {
     dot=0;
     win='D';
     for(int j=0;j<4;j++)
     {
      for(int k=0;k<4;k++)
      {
       ifile>>A[j][k];
      }
     }
             
     for(int i=0;i<4;i++)
     {
      o=0,x=0,t=0;
      for(int j=0;j<4;j++)
      {
      /*if(A[i][0]=='X'&&A[i][1]=='X'&&A[i][2]=='X'&&A[i][3]=='X')
      win='X';
      else if(A[i][0]=='O'&&A[i][1]=='O'&&A[i][2]=='O'&&A[i][3]=='O')
      win='O';
      */
      if(A[i][j]=='X')
                      x++;
      else if(A[i][j]=='O')
           o++;
      else if(A[i][j]=='T')
           t++;
      else if(A[i][j]=='.')
           dot++;
      }
      if((x==3&&t==1)||(x==4))
      win='X';
      else if((o==3&&t==1)||(o==4))
      win='O';
      
     }
     for(int j=0;j<4;j++)
     {
      o=0,x=0,t=0;
      for(int i=0;i<4;i++)
      {
      /*if(A[i][0]=='X'&&A[i][1]=='X'&&A[i][2]=='X'&&A[i][3]=='X')
      win='X';
      else if(A[i][0]=='O'&&A[i][1]=='O'&&A[i][2]=='O'&&A[i][3]=='O')
      win='O';
      */
      if(A[i][j]=='X')
                      x++;
      else if(A[i][j]=='O')
           o++;
      else if(A[i][j]=='T')
           t++;
      else if(A[i][j]=='.')
           dot++;
      }
      if((x==3&&t==1)||(x==4))
      win='X';
      else if((o==3&&t==1)||(o==4))
      win='O';
      
     }
     
     
     o=0,x=0,t=0;
     for(int i=0;i<4;i++)
     {
      for(int j=i;j<=i;j++)
      {
      /*if(A[i][0]=='X'&&A[i][1]=='X'&&A[i][2]=='X'&&A[i][3]=='X')
      win='X';
      else if(A[i][0]=='O'&&A[i][1]=='O'&&A[i][2]=='O'&&A[i][3]=='O')
      win='O';
      */
      
      if(A[i][j]=='X')
                      x++;
      else if(A[i][j]=='O')
           o++;
      else if(A[i][j]=='T')
           t++;
      else if(A[i][j]=='.')
           dot++;
      }
      if((x==3&&t==1)||(x==4))
      win='X';
      else if((o==3&&t==1)||(o==4))
      win='O';
      
     }
     o=0,x=0,t=0;
     for(int i=0;i<4;i++)
     {
      for(int j=3-i;j<=3-i;j++)
      {
      /*if(A[i][0]=='X'&&A[i][1]=='X'&&A[i][2]=='X'&&A[i][3]=='X')
      win='X';
      else if(A[i][0]=='O'&&A[i][1]=='O'&&A[i][2]=='O'&&A[i][3]=='O')
      win='O';
      */
      
      if(A[i][j]=='X')
                      x++;
      else if(A[i][j]=='O')
           o++;
      else if(A[i][j]=='T')
           t++;
      else if(A[i][j]=='.')
           dot++;
      }
      if((x==3&&t==1)||(x==4))
      win='X';
      else if((o==3&&t==1)||(o==4))
      win='O';
      
     }
          
     /*
     for(int i=0;i<4;i++)
     {
      if(A[i][0]=='X'&&A[i][1]=='X'&&A[i][2]=='X'&&A[i][3]=='X')
      win='X';
      else if(A[i][0]=='O'&&A[i][1]=='O'&&A[2][i]=='O'&&A[3][i]=='O')
      win='O';
     }
     
     
     for(int i=0;i<4;i++)
     {
      if(A[0][i]=='X'&&A[1][i]=='X'&&A[2][i]=='X'&&A[3][i]=='X')
      win='X';
      else if(A[0][i]=='O'&&A[1][i]=='O'&&A[2][i]=='O'&&A[3][i]=='O')
      win='O';
     }
     
     if(A[0][0]=='X'&&A[1][1]=='X'&&A[2][2]=='X'&&A[3][3]=='X')
     win='X';
     if(A[0][0]=='O'&&A[1][1]=='O'&&A[2][2]=='O'&&A[3][3]=='O')
     win='O';
     if(A[0][3]=='X'&&A[1][2]=='X'&&A[2][1]=='X'&&A[3][0]=='X')
     win='X';
     if(A[0][3]=='X'&&A[1][2]=='X'&&A[2][1]=='X'&&A[3][0]=='X')
     win='O';
     */
     ofile<<"Case #"<<i+1<<": ";
     if(win=='X')
     ofile<<"X won"<<endl;
     else if(win=='O')
     ofile<<"O won"<<endl;
     else if(dot)
     ofile<<"Game has not completed"<<endl;
     else if(win=='D')
     ofile<<"Draw"<<endl;
     
    }
    ofile<<endl;
    ifile.close();
    ofile.close();
    getch();
}
