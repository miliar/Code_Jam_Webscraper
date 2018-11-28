#include<iostream>
using namespace std;
char arr[6][6];

void input()
{
    for(int i=1;i<=4;i++)
    {
            for(int j=1;j<=4;j++)
                   cin >> arr[i][j];
    }
}

void chek()
{
     int cx=0,co=0;
    /////////////////////////// checking rows 
    for(int i=1;i<=4;i++)
    {
          cx=0;
          co=0;
          for(int j=1;j<=4;j++)
          {
                if(arr[i][j]=='X' || arr[i][j]=='T')
                      cx++;
                if(arr[i][j]=='O' || arr[i][j]=='T')
                      co++;
          }
          
          if(cx==4)
          {
                cout << "X won\n";
                return;
          }    
          if(co==4)
          {
                cout << "O won\n";
                return;
          }
    }
    //////////////////////// checking coloumns
    for(int j=1;j<=4;j++)
    {
          cx=0;
          co=0;
          for(int i=1;i<=4;i++)
          {
                if(arr[i][j]=='X' || arr[i][j]=='T')
                      cx++;
                if(arr[i][j]=='O' || arr[i][j]=='T')
                      co++;
          }
          if(cx==4)
          {
                cout << "X won\n";
                return;
          }    
          if(co==4)
          {
                cout << "O won\n";
                return;
          }
    }
    ///////////////////////////////// checking diagonal from left-top
    cx=0;
    co=0;
    for(int i=1;i<=4;i++)
    {    
        if(arr[i][i]=='O' || arr[i][i]=='T')
          	co++;
    	  else if(arr[i][i]=='X' || arr[i][i]=='T')
          	cx++;
     }
     if(cx==4)
     {
          cout << "X won\n";
          return;
     }    
     else if(co==4)
     {
          cout << "O won\n";
          return;
     }
    ///////////////////////////////// checking diagonal from right-top
    cx=0;
    co=0;
    if(arr[1][4]=='O' || arr[1][4]=='T')
          co++;
    else if(arr[1][4]=='X' || arr[1][4]=='T')
          cx++;
    if(arr[2][3]=='O' || arr[2][3]=='T')
          co++;
    else if(arr[2][3]=='X' || arr[2][3]=='T')
          cx++;
    if(arr[3][2]=='O' || arr[3][2]=='T')
          co++;
    else if(arr[3][2]=='X' || arr[3][2]=='T')
          cx++;
    if(arr[4][1]=='O' || arr[4][1]=='T')
          co++;
    else if(arr[4][1]=='X' || arr[4][1]=='T')
          cx++;
    if(cx==4)
    {
                cout << "X won\n";
                return;
          }    
          else if(co==4)
          {
                cout << "O won\n";
                return;
          }
    

  	
/*
    for(int i=1;i<=4;i++)
    {
          for(int j=1;j<=4;j++)
          {
                if(i+j==5)
                {  
                      if(arr[i][j]=='X' || arr[i][j]=='T')
                             cx++;
                      if(arr[i][j]=='O' || arr[i][j]=='T')
                             co++;
                }
          }
          if(cx==4)
          {
                cout << "X won\n";
                return;
          }    
          else if(co==4)
          {
                cout << "O won\n";
                return;
          }
    }
*/
    /////////////////////////// checking incomplete
    for(int i=1;i<=4;i++)
    {
          for(int j=1;j<=4;j++)
          {
                if(arr[i][j]=='.')
                 {
                       cout << "Game has not completed\n";
                       return;
                 }
          }
    }
    /////////////////////////// draw
    cout << "Draw\n";
}              
          
int main()
{
    int T=0,i=1;
    cin >> T;
    while(T--)
    {
         input();
         cout << "Case #" << i << ": ";
         chek(); 
         i++;        
    }
    //getch();
    return 0;
}
    
