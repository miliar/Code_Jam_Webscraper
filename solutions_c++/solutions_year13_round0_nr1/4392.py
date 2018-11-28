#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#define MAXSIZE 100002
#define MODVALUE 1000000007
#define MAX(a,b) \
({ __typeof__ (a) _a = (a); \
__typeof__ (b) _b = (b); \
_a > _b ? _a : _b; })
 
#define MIN(a,b) \
({ __typeof__ (a) _a = (a); \
__typeof__ (b) _b = (b); \
_a < _b ? _a : _b; })
 
#define FOR(a,b,c) for(long a=b;a<c;a++)
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        char output[100];
         sprintf(output,"Case #%d: ",(i+1));
        char board[4][4];
        char input[4];
        FOR(i,0,4)
        {
        	scanf("%s",input);
        	board[i][0]=input[0];
         	board[i][1]=input[1];
         	board[i][2]=input[2];
         	board[i][3]=input[3];
         }
                //scanf("%c%c%c%c\n",&board[i][0],&board[i][1],&board[i][2],&board[i][3]);
        
        bool  hasXWon=false,hasOWon=false,isComplete=true;
        int i=0;
        for(i;i<4;i++)
        {
            char headForRow=board[i][0];
            char headForColumn=board[0][i];
            bool haveWinnerForRow=true,haveWinnerForColumn=true;
            FOR(j,0,4)
            {
                //printf("headForrow:%c\n",headForRow);
                if(headForRow!='.')
                {
                //printf("board[%d][%d]:%c\n",i,j,board[i][j]);
                    if(headForRow=='T')
                        headForRow=board[i][j];
                    
                    if(board[i][j]=='.')
                    {
                        isComplete=false;
                        haveWinnerForRow=false;
                     }
                    else if(board[i][j]!='T' && headForRow!=board[i][j] )
                       haveWinnerForRow=false;
                }
                else
                {
                    isComplete=false;
                    haveWinnerForRow=false;
                }
                //printf("headForColumn:%c\n",headForColumn);
                // handle for ith column
                if(headForColumn!='.')
                {
                    if(headForColumn=='T')
                        headForColumn=board[j][i];
                    
                    if(board[j][i]=='.')
                    {
                        isComplete=false;
                        haveWinnerForColumn=false;
                    }
                    else if(board[j][i]!='T' && headForColumn!=board[j][i] )
                       haveWinnerForColumn=false;
                }
                else
                {
                    isComplete=false;
                    haveWinnerForColumn=false;
                }
                
            }
            
            //printf("complte status :%d after i:%d\n",isComplete,i);
                if(haveWinnerForRow)
                {
                    //printf("haveWinnerForRow:%d",i);
                    if(headForRow=='X')
                        hasXWon=true;
                    else if(headForRow=='O')
                        hasOWon=true;
                }
                
                if(haveWinnerForColumn)
                {
                	
                		
                //printf("haveWinnerForColumn:%d--->%c",i,headForColumn);
                    if(headForColumn=='X')
                        hasXWon=true;
                    else if(headForColumn=='O')
                        hasOWon=true;
                }
            if(hasXWon||hasOWon)
            	{
            		//printf("%d-->%d\n",hasXWon,hasOWon);
                	break;
                }
            }
            
            if(i>3) // don't already have a winner
            {
                //printf("no winner till now\n");
                char head=board[0][0];
                bool haveWinner=true;
                FOR(i,0,4)
                {
                    
                    if(head!='.')
                    {
                        if(head=='T')
                            head=board[i][i];
                    
                        if(board[i][i]=='.')
                        {
                            isComplete=false;
                            haveWinner=false;
                         }
                         else if(board[i][i]!='T' && head!=board[i][i] )
                            haveWinner=false;
                    }
                    else
                    {
                        isComplete=false;
                        haveWinner=false;
                    }
                }
                
                if(haveWinner)
                {
                    if(head=='X')
                        hasXWon=true;
                    else if(head=='O')
                        hasOWon=true;
                }
                else // check the other diaogonal
                {
                    head=board[0][3];
                    bool haveWinner=true;
                    for(int i=3;i>=0;i--)
                    {
                    
                        if(head!='.')
                        {
                            if(head=='T')
                                head=board[3-i][i];
                    
                            if(board[3-i][i]=='.')
                            {
                                isComplete=false;
                                haveWinner=false;
                            }
                        else if(board[3-i][i]!='T' && head!=board[3-i][i] )
                                haveWinner=false;
                    }
                    else
                    {
                        isComplete=false;
                        haveWinner=false;
                    }
                }
                
                if(haveWinner)
                {
                    if(head=='X')
                        hasXWon=true;
                    else if(head=='O')
                        hasOWon=true;
                }    
            } // end of other diagonal else
                
        }
        //printf("%d-->%d -->%d",hasXWon,hasOWon,isComplete);
        if(hasXWon)
        {
            strcat(output,"X won");
        }
        else if(hasOWon)
        {
            strcat(output,"O won");
        }
        else
        {
        	if(isComplete)
        	 	strcat(output,"Draw");
        	else
        		strcat(output,"Game has not completed");
        }
        printf("%s\n",output);
    }
            
}        
/*    }
    
}
            
            if((board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T')&&(board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T'))
                hasXWon=true;
            if((board[0][i]=='X' || board[1][i]=='T') && (board[0][i]=='X' || board[i][1]=='T')&&(board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T'))
                hasXWon=true;    
            FOR(j,0,4)
            {
                if(board[i][j]=='.')
                    isComplete=false;
            } 
        }
    
    }
    }
}*/
