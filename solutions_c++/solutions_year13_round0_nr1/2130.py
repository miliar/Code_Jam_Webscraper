#include <fstream>
#include <math.h>
#include <vector>
using namespace std;
int main()
{
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  int n;
  fin>>n;
  char arr[4][4];
  int nx,ny;
  int status;
  for (int i=0;i<n;i++)
  {
    status=3;
    for (int j=0;j<4;j++)
      for (int k=0;k<4;k++)
	{
           fin>>arr[j][k];
	}

    for (int j=0;j<4;j++)
      {
        nx=ny=0;
        for (int k=0;k<4;k++)
        {
          if (arr[j][k]=='X')
            nx++;
          if (arr[j][k]=='O')
            ny++;
          if (arr[j][k]=='T')
            {ny++; nx++;}          
        }
        if (nx==4)
          status=1;
        if (ny==4)
          status=2;
      }

    for (int j=0;j<4;j++)
      {
        nx=ny=0;
        for (int k=0;k<4;k++)
        {
          if (arr[k][j]=='X')
            nx++;
          if (arr[k][j]=='O')
            ny++;
          if (arr[k][j]=='T')
            {ny++; nx++;}          
        }
        if (nx==4)
          status=1;
        if (ny==4)
          status=2;
      }
   nx=ny=0;
   for (int j=0;j<4;j++)
     {
          if (arr[j][j]=='X')
            nx++;
          if (arr[j][j]=='O')
            ny++;
          if (arr[j][j]=='T')
            {ny++; nx++;}          
     }
        if (nx==4)
          status=1;
        if (ny==4)
          status=2;

   nx=ny=0;
   for (int j=0;j<4;j++)
     {
          if (arr[j][3-j]=='X')
            nx++;
          if (arr[j][3-j]=='O')
            ny++;
          if (arr[j][3-j]=='T')
            {ny++; nx++;}          
     }
        if (nx==4)
          status=1;
        if (ny==4)
          status=2;

     if (status==3)
      for (int j=0;j<4;j++)
        for (int k=0;k<4;k++)
          if (arr[j][k]=='.')
            status=4;
     switch (status) {
      
       case 1:
       fout<<"Case #"<<i+1<<": "<<"X won"<<endl;
       break;
       case 2:
       fout<<"Case #"<<i+1<<": "<<"O won"<<endl;
       break;
       case 3:
       fout<<"Case #"<<i+1<<": "<<"Draw"<<endl;
       break;
       case 4:
       fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
       break;
    }
  }
  return 0;
}
