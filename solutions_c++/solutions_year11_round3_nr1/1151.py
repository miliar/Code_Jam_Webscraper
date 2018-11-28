#include<iostream>
using namespace std;
int main()
{
    int T,R,C,flag,row,column;
    char grid[60][60];
    cin>>T;
    for(int i=0;i<T;i++)
    {
            cin>>R>>C;
            flag=1;
            row=0;
            for(int j=0;j<R;j++)
                    cin>>grid[j];
            column=-1;
            while(column<C)
            {
                    column++;
                    if(grid[row][column]=='#'&&(grid[row][column+1]!='#'||grid[row+1][column]!='#'||grid[row+1][column+1]!='#'))
                    {
                           
                           flag=-1;
                           break;
                    }
                    if(grid[row][column]=='#'&&grid[row][column+1]=='#'&&grid[row+1][column]=='#'&&grid[row+1][column+1]=='#')
                    {
                        grid[row][column]='/';
                        grid[row][column+1]='\\';
                        grid[row+1][column]='\\';
                        grid[row+1][column+1]='/';
                        
                    }
                    if(column==C-1&&row<R-1)
                    {
                                    
                                    row++;
                                    column=-1;
                    }
                    
            }
            cout<<"Case #"<<i+1<<":\n";
            if(flag==-1)
                        cout<<"Impossible\n";
            else
                for(int j=0;j<R;j++)
                        cout<<grid[j]<<"\n";
    }
    return 0;
}                       
                                            
