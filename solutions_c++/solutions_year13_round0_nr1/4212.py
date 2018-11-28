#include<iostream>
#include<cmath>
#include<cstdio>
#include<vector>

using namespace std;
int isWinner(char arr[][4])
{
    int status =-1,i,j,k,tx=-1,ty=-1 ;//incomplete
    //find T pos
    for(j=0;j<4;j++)
    {
        for(k=0;k<4;k++)
        {
           if(arr[j][k]=='.')
              status=0;
        }
    }               
for (i=0;i<4;i++)
{  
     if(((arr[i][0]=='X' || arr[i][0]=='T') &&
                        (arr[i][1]=='X' || arr[i][1]=='T') &&
                        (arr[i][2]=='X' || arr[i][2]=='T') &&
                        (arr[i][3]=='X' || arr[i][3]=='T')) ||
                        (arr[0][i]=='X' || arr[0][i]=='T') &&
                        (arr[1][i]=='X' || arr[1][i]=='T') &&
                        (arr[2][i]=='X' || arr[2][i]=='T') &&
                        (arr[3][i]=='X' || arr[3][i]=='T') )
                        {
                                        status=1;//X wins
                                        //break;
                        }
      if(((arr[i][0]=='O' || arr[i][0]=='T') &&
                        (arr[i][1]=='O' || arr[i][1]=='T') &&
                        (arr[i][2]=='O' || arr[i][2]=='T') &&
                        (arr[i][3]=='O' || arr[i][3]=='T')) ||
                        (arr[0][i]=='O' || arr[0][i]=='T') &&
                        (arr[1][i]=='O' || arr[1][i]=='T') &&
                        (arr[2][i]=='O' || arr[2][i]=='T') &&
                        (arr[3][i]=='O' || arr[3][i]=='T')  )
                        {
                                        status=2;//O wins
                        }
     
}
    if(((arr[0][0]=='X' || arr[0][0]=='T') &&
                        (arr[1][1]=='X' || arr[1][1]=='T') &&
                        (arr[2][2]=='X' || arr[2][2]=='T') &&
                        (arr[3][3]=='X' || arr[3][3]=='T'))||
                        ((arr[0][3]=='X' || arr[0][3]=='T') &&
                        (arr[1][2]=='X' || arr[1][2]=='T') &&
                        (arr[2][1]=='X' || arr[2][1]=='T') &&
                        (arr[3][0]=='X' || arr[3][0]=='T')))
                        {
                           status=1;//X wins
                        }
    if(((arr[0][0]=='O' || arr[0][0]=='T') &&
                        (arr[1][1]=='O' || arr[1][1]=='T') &&
                        (arr[2][2]=='O' || arr[2][2]=='T') &&
                        (arr[3][3]=='O' || arr[3][3]=='T'))||
                        ((arr[0][3]=='O' || arr[0][3]=='T') &&
                        (arr[1][2]=='O' || arr[1][2]=='T') &&
                        (arr[2][1]=='O' || arr[2][1]=='T') &&
                        (arr[3][0]=='O' || arr[3][0]=='T')))
                        {
                           status=2; //O WINS
                        }
return status;
}

int main()
{

char arr[4][4];
int t,i,j,status;
cin>>t;
for(i=0;i<t;i++)
{
  cin>>arr[0]>>arr[1]>>arr[2]>>arr[3];
  //cout <<"\n"<<arr[0]<<arr[1]<<arr[2]<<arr[3];
  status = isWinner(arr);
  if(status == -1)
            cout<<"Case #"<<i+1<<": Draw\n";
  else if(status == 0)
            cout<<"Case #"<<i+1<<": Game has not completed\n";
  else if(status == 1)
            cout<<"Case #"<<i+1<<": X won\n";
  else if(status == 2)
            cout<<"Case #"<<i+1<<": O won\n";
  else
      cout<<"Case #"<<i+1<<": Draw\n";
      
            
}

}
