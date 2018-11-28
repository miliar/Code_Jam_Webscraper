#include <iostream>
#include <fstream>
using namespace std;

void print(char mat[4][4])
{
    for(int i=0;i<4;++i)
    {
        for(int j=0;j<4;++j)
    {
        cout<<mat[i][j];
    }
    cout<<endl;
    }
    cout<<endl;
}

int main()
{
    fstream file,file1;
    file.open("input.txt");
    file1.open("output.o");
    int testcase;
    file>>testcase;
    char mat[4][4];
    int Xwin[4],Owin[4];
    bool detect;
    for(int i=0;i<testcase;++i)
    {
     detect=0;
     for(int m=0;m<4;++m)
     {
         for(int n=0;n<4;++n)
         {
             file>>mat[m][n];
             if(mat[m][n]=='.')
             detect=1;
         }
     }
     Xwin[2]=0;Owin[2]=0;
     Xwin[3]=0;Owin[3]=0;
     for(int j=0;j<4;++j)
     {
         Xwin[0]=0;
         Owin[0]=0;
         Xwin[1]=0;
         Owin[1]=0;
         if(mat[j][j]=='T'||mat[j][j]=='X')
         ++Xwin[2];
         if(mat[j][j]=='T'||mat[j][j]=='O')
         ++Owin[2];
         if(mat[j][3-j]=='T'||mat[j][3-j]=='X')
         ++Xwin[3];
         if(mat[j][3-j]=='T'||mat[j][3-j]=='O')
         ++Owin[3];
         for(int k=0;k<4;++k)
         {
             if(mat[j][k]=='T'||mat[j][k]=='X')
             ++Xwin[0];
             if(mat[j][k]=='T'||mat[j][k]=='O')
             ++Owin[0];
             if(mat[k][j]=='T'||mat[k][j]=='X')
             ++Xwin[1];
             if(mat[k][j]=='T'||mat[k][j]=='O')
             ++Owin[1];
             if((Xwin[0]!=k+1)&&(Owin[0]!=k+1)&&(Xwin[1]!=k+1)&&(Owin[1]!=k+1))
             break;
         }
         if(Xwin[0]==4||Xwin[1]==4||Owin[0]==4||Owin[1]==4)
         break;
     }
    if((Xwin[0]==4)||(Xwin[1]==4)||(Xwin[2]==4)||(Xwin[3]==4))
    file1<<"Case #"<<i+1<<":"<<" X won"<<endl;
    else if((Owin[0]==4)||(Owin[1]==4)||(Owin[2]==4)||(Owin[3]==4))
    file1<<"Case #"<<i+1<<":"<<" O won"<<endl;
    else if(detect==true)
    file1<<"Case #"<<i+1<<":"<<" Game has not completed"<<endl;
    else
    file1<<"Case #"<<i+1<<":"<<" Draw"<<endl;
    }
    return 0;
    file.close();
    file1.close();
}
