#include<iostream>
#include<cstdio>
using namespace std;

int status(int f, int x, int y)
{
    if((x==4) || (x==3 && f==1))
    {
               cout<<"X won"<<endl;
               return 1;
    }else if((y==4) || (y==3 && f==1))
    {
               cout<<"O won"<<endl;
               return 1;
    }
    return 0;
}


int main(){
    
    int t,i,j;
    int z = 1, s =-1;
    cin>>t;
    while(t--)
    {    
        char ch[4][4];
        for(i=0;i<4;i++)
        scanf("%s",ch[i]);
        int x =0, y=0, f=0, c=0;
        
        cout<<"Case #"<<z<<": ";
        z++;
        
        s=-1;
        for(i=0;i<4;i++)
        {
            x = 0;
            y = 0;
            f = 0;
            for(j=0;j<4;j++)
            {
                if(ch[i][j] == 'X')
                    x++;
                else if(ch[i][j] == 'O')
                    y++;
                else if(ch[i][j]=='T')
                    f = 1;
                else if(ch[i][j]=='.')
                    c = -1;
            }
            s = status(f,x,y);
            if(s==1)
            break;
        }
        if(s==1)
        continue;
        for(j=0;j<4;j++)
        {
            x = 0;
            y = 0;
            f = 0;
            for(i=0;i<4;i++)
            {
                if(ch[i][j] == 'X')
                    x++;
                else if(ch[i][j] == 'O')
                    y++;
                else if(ch[i][j]=='T')
                    f = 1;
                else if(ch[i][j]=='.')
                    c = -1;
            }
            s = status(f,x,y);
            if(s==1)
            break;
        }                
        if(s==1)
            continue;
        x=0;
        y=0;
        f=0;    
        for(i=0;i<4;i++)
        {  
            if(ch[i][i] == 'X')
                    x++;
            else if(ch[i][i] == 'O')
                y++;
            else if(ch[i][i]=='T')
                f = 1;
            else if(ch[i][i]=='.')
                c = -1;
        }
        s = status(f,x,y);
        if(s==1)
            continue;
        x=0;
        y=0;
        f=0;    
        for(i=3;i>=0;i--)
        {  
            if(ch[3-i][i] == 'X')
                    x++;
            else if(ch[3-i][i] == 'O')
                y++;
            else if(ch[3-i][i]=='T')
                f = 1;
            else if(ch[3-i][i]=='.')
                c = -1;
        }
        s = status(f,x,y);
        if(s==1)
        continue;
        if(c==-1)
        cout<<"Game has not completed"<<endl;
        else
        cout<<"Draw"<<endl;
    }   
    return 0;
}
