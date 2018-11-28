#include<iostream>
//#include<cstdio>
//#include<sstream>
//#include<cstring>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T;
    cin>>T;
    cin.ignore();
    
    int isGameComplete=1,i,j;
    char board[4][4];
    
    // 0 means YES, 1 means NO :P
    int xWinPossible[10]; //rows:0-3, cols:4-7, left diagonal:8, right diagonal: 9
    int oWinPossible[10];   
    
    string outputs[4]={"X won","O won","Draw","Game has not completed"};
    
    int result;
    
    int t=1;
    while(T--)
    {
        memset (xWinPossible,0,10 *sizeof(int)); 
        memset (oWinPossible,0,10 * sizeof(int));
        result=5;
        isGameComplete=1;
        
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>board[i][j];
            }
        }
        
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //cin>>board[i][j];
                if(board[i][j]=='.'){
                    isGameComplete=0;  //Game not complete, So draw not possible
                    xWinPossible[i]=1;
                    xWinPossible[4+j]=1;
                    oWinPossible[i]=1;
                    oWinPossible[4+j]=1;
                    if(i==j){
                        xWinPossible[8]=1;
                        oWinPossible[8]=1;
                    }else if(i==3-j){
                        xWinPossible[9]=1;
                        oWinPossible[9]=1;
                    }
                }
                else if(board[i][j]=='X'){
                    oWinPossible[i]=1;
                    oWinPossible[4+j]=1;
                    if(i==j)
                        oWinPossible[8]=1;
                    else if(i==3-j)
                        oWinPossible[9]=1;
                }
                else if(board[i][j]=='O'){
                    xWinPossible[i]=1;
                    xWinPossible[4+j]=1;
                    if(i==j)
                        xWinPossible[8]=1;
                    else if(i==3-j)
                        xWinPossible[9]=1;
                }

            }
            if(xWinPossible[i]==0){
                result=0;
                break;
            }else if(oWinPossible[i]==0){
                result=1;
                break;
            }
        }
        if(result==5)  // CHECK for columns and diagonals only if no ones wins through rows
            for(i=4;i<10;i++){
                if(xWinPossible[i]==0){
                    result=0;
                    break;
                }else if(oWinPossible[i]==0){
                    result=1;
                    break;
                }
            }
        
        if(result!=0&&result!=1){
            result=isGameComplete?2:3;
        }
        
        cout<<"Case #"<<t++<<": "<<outputs[result]<<endl;
        cin.ignore();
    }
    
    return 0;
}