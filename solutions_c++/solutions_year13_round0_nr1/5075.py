//gmw.sjtu@gmail.com

#include <iostream>
#include <fstream>
using namespace std;

bool checkX(char A)
{
    if ((A=='X')||(A=='T')) return true;
    else return false;

}

bool checkO(char A)
{
    if ((A=='O')||(A=='T')) return true;
    else return false;

}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");

    int N;
    char field[4][4];
    fin>>N;
    for(int n=0;n<N;n++)
    {
        int i,j;
        int state=1;
        bool Xflag=false;
        bool Oflag=false;
        for(i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                fin>>field[i][j];
                if (field[i][j]=='.') state=0;
            }
        }

     while (true)
     {
      //line check
      for (j=0;j<4;j++)
      {
          Xflag=(checkX(field[0][j])&&checkX(field[1][j])&&checkX(field[2][j])&&checkX(field[3][j]));
          Oflag=(checkO(field[0][j])&&checkO(field[1][j])&&checkO(field[2][j])&&checkO(field[3][j]));
          if (Xflag||Oflag) break;
      }
      if (Xflag||Oflag) break;
      //column check
      for (i=0;i<4;i++)
      {
          Xflag=(checkX(field[i][0])&&checkX(field[i][1])&&checkX(field[i][2])&&checkX(field[i][3]));
          Oflag=(checkO(field[i][0])&&checkO(field[i][1])&&checkO(field[i][2])&&checkO(field[i][3]));
          if (Xflag||Oflag) break;
      }
      if (Xflag||Oflag) break;
      //diagonse check
     Xflag=(checkX(field[0][0])&&checkX(field[1][1])&&checkX(field[2][2])&&checkX(field[3][3]));
     Oflag=(checkO(field[0][0])&&checkO(field[1][1])&&checkO(field[2][2])&&checkO(field[3][3]));
     if (Xflag||Oflag) break;
     Xflag=(checkX(field[0][3])&&checkX(field[1][2])&&checkX(field[2][1])&&checkX(field[3][0]));
     Oflag=(checkO(field[0][3])&&checkO(field[1][2])&&checkO(field[2][1])&&checkO(field[3][0]));
     break;
    }

    fout<<"Case #"<<n+1<<": ";
    if (Xflag) fout<<"X won"<<endl;
    else if (Oflag) fout<<"O won"<<endl;
    else if (state==0) fout<<"Game has not completed"<<endl;
    else if (state==1) fout<<"Draw"<<endl;
}
}
