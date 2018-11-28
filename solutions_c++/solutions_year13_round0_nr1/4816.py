#include "cstdio"
#include "cstring"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    
    for(int test=1;test<=t;test++)
    {
        char board[5][5];
        bool o,x,full;
        
        full=true;
        o=false;
        x=false;
        
        for(int i=0;i<4;i++)scanf("%s",board[i]);
        
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(board[i][j]=='.')
                {
                    full=false;
                    break;
                }
        }
        
        for(int i=0;i<4;i++)
        {
            int to,tx,tt;
            
            to=tx=tt=0;
            
            for(int j=0;j<4;j++)
            {
                if(board[i][j]=='X')tx++;
                if(board[i][j]=='T')tt++;
                if(board[i][j]=='O')to++;
            }
            
            if(to==3 && tt==1)o=true;
            if(tx==3 && tt==1)x=true;
            if(to==4)o=true;
            if(tx==4)x=true;
        }
        
        for(int j=0;j<4;j++)
        {
            int to,tx,tt;
            
            to=tx=tt=0;
            
            for(int i=0;i<4;i++)
            {
                if(board[i][j]=='X')tx++;
                if(board[i][j]=='T')tt++;
                if(board[i][j]=='O')to++;
            }
            
            if(to==3 && tt==1)o=true;
            if(tx==3 && tt==1)x=true;
            if(to==4)o=true;
            if(tx==4)x=true;
        }
        
        int to,tx,tt;
            
        to=tx=tt=0;
            
        for(int i=0;i<4;i++)
        {
            if(board[i][i]=='X')tx++;
            if(board[i][i]=='T')tt++;
            if(board[i][i]=='O')to++;
        }
        
        if(to==3 && tt==1)o=true;
        if(tx==3 && tt==1)x=true;
        if(to==4)o=true;
        if(tx==4)x=true;
        
        to=tx=tt=0;
            
        for(int i=0;i<4;i++)
        {
            if(board[i][3-i]=='X')tx++;
            if(board[i][3-i]=='T')tt++;
            if(board[i][3-i]=='O')to++;
        }
        
        if(to==3 && tt==1)o=true;
        if(tx==3 && tt==1)x=true;
        if(to==4)o=true;
        if(tx==4)x=true;
        
        printf("Case #%d: ",test);
        
        if(x==true)printf("X won\n");
        else if(o==true)printf("O won\n");
        else if(full==true)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    
    return 0;
}
