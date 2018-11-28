#include<iostream>
#include<fstream>
using namespace std;

int check(char arr[][4],char ch)
{
  int flag=1;
  for(int i=0;i<4;i++)
  {
      flag=1;
      for(int j=0;j<4;j++)
      {
          if(arr[i][j]!=ch&&arr[i][j]!='T')
          {
            flag=0;
            break;
          }
      }
      if(flag)
      {
          return 1;
      }
  }
  for(int i=0;i<4;i++)
  {
      flag=1;
      for(int j=0;j<4;j++)
      {
          if(arr[j][i]!=ch&&arr[j][i]!='T')
          {
            flag=0;
            break;
          }
      }
      if(flag)
      {
          return 1;
      }
  }
  if((arr[0][0]==ch||arr[0][0]=='T')&&(arr[1][1]==ch||arr[1][1]=='T')&&(arr[2][2]==ch||arr[2][2]=='T')&&(arr[3][3]==ch||arr[3][3]=='T'))
    return 1;
   if((arr[0][3]==ch||arr[0][3]=='T')&&(arr[1][2]==ch||arr[1][2]=='T')&&(arr[2][1]==ch||arr[2][1]=='T')&&(arr[3][0]==ch||arr[3][0]=='T'))
    return 1;
    return 0;

}
int gamecomplete(char arr[][4])
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]=='.')
                return 1;
        }
    }
    return 0;
}
int main()
{
    int T,i=0,flag;
    char arr[4][4];
    ifstream infile("A-large.in");
    ofstream outfile("output.txt");
    infile>>T;
    infile.get();
    for(i=0;i<T;i++)
    {

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                arr[j][k]='a';

            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                infile.get(arr[j][k]);

            }
            infile.get();
        }

        infile.get();
        flag=0;
        flag=check(arr,'X');
        if(flag)
        {


            outfile<<"Case #"<<i+1<<": "<<"X won"<<endl;
            flag=0;
            continue;
        }
        flag=check(arr,'O');
        if(flag)
        {


            outfile<<"Case #"<<i+1<<": "<<"O won"<<endl;
            flag=0;
            continue;
        }
        flag=gamecomplete(arr);
        if(flag)
        {


            outfile<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
            flag=0;
            continue;
        }
        outfile<<"Case #"<<i+1<<": "<<"Draw"<<endl;

}
infile.close();
outfile.close();
return 0;
}
