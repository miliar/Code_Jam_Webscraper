#include <iostream>
#include <istream>
#include <sstream>
using namespace std;
int main(){
    int numberofcases;
    cin>>numberofcases;
    int result[numberofcases];
    for(int k=0;k<numberofcases;k++)
    result[k]=4;
    for(int i =0;i<numberofcases;i++){
            char grid[4][4];
            for(int j =0;j<4;j++){
            cin>>grid[j][0]>>grid[j][1]>>grid[j][2]>>grid[j][3];}
            string flag;
            getline(cin,flag);
            string flag1;
            getline(cin,flag1);
            for(int j=0;j<4;j++){
                  if((grid[j][0]=='X'||grid[j][0]=='T')&&(grid[j][1]=='X'||grid[j][1]=='T')&&(grid[j][2]=='X'||grid[j][2]=='T')&&(grid[j][3]=='X'||grid[j][3]=='T'))
                  result[i]=1;
                  if((grid[0][j]=='X'||grid[0][j]=='T')&&(grid[1][j]=='X'||grid[1][j]=='T')&&(grid[2][j]=='X'||grid[2][j]=='T')&&(grid[3][j]=='X'||grid[3][j]=='T'))
                  result[i]=1;
                  if((grid[0][0]=='X'||grid[0][0]=='T')&&(grid[1][1]=='X'||grid[1][1]=='T')&&(grid[2][2]=='X'||grid[2][2]=='T')&&(grid[3][3]=='X'||grid[3][3]=='T'))
                  result[i]=1;
                  if((grid[3][0]=='X'||grid[3][0]=='T')&&(grid[2][1]=='X'||grid[2][1]=='T')&&(grid[1][2]=='X'||grid[1][2]=='T')&&(grid[0][3]=='X'||grid[0][3]=='T'))
                  result[i]=1;
                  if((grid[j][0]=='O'||grid[j][0]=='T')&&(grid[j][1]=='O'||grid[j][1]=='T')&&(grid[j][2]=='O'||grid[j][2]=='T')&&(grid[j][3]=='O'||grid[j][3]=='T'))
                  result[i]=2;
                  if((grid[0][j]=='O'||grid[0][j]=='T')&&(grid[1][j]=='O'||grid[1][j]=='T')&&(grid[2][j]=='O'||grid[2][j]=='T')&&(grid[3][j]=='O'||grid[3][j]=='T'))
                  result[i]=2;
                  if((grid[0][0]=='O'||grid[0][0]=='T')&&(grid[1][1]=='O'||grid[1][1]=='T')&&(grid[2][2]=='O'||grid[2][2]=='T')&&(grid[3][3]=='O'||grid[3][3]=='T'))
                  result[i]=2;
                  if((grid[3][0]=='O'||grid[3][0]=='T')&&(grid[2][1]=='O'||grid[2][1]=='T')&&(grid[1][2]=='O'||grid[1][2]=='T')&&(grid[0][3]=='O'||grid[0][3]=='T'))
                  result[i]=2;}
                  if (result[i]==4){
                             for(int p=0;p<4;p++){
                                     for(int y=0;y<4;y++){
                                             if(grid[p][y]=='.')
                                             result[i]=3;}
                                             
                                     }       
                                       
                    }    
            }
        
    for(int i=0;i<numberofcases;i++){
            if(result[i]==1)
            cout<<"Case #"<<i+1<<": X won"<<endl;
            else if (result[i]==2)
            cout<<"Case #"<<i+1<<": O won"<<endl;
            else if (result[i]==3)
            cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
            else if (result[i]==4)
            cout<<"Case #"<<i+1<<": Draw"<<endl;
            }

    
    return 0;}
