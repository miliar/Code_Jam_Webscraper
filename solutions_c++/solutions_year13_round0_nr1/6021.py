#include <iostream>
#include<cstdio>
using namespace std;
int main() 
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        bool draw=true;
        char a[4][4];           //input
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                    cin>>a[i][j];
                    if(a[i][j]=='.')
                        draw=false;
                    
                }
        char win;
        bool found=true;
        for(int i=0;i<4;i++)    //chking for horizontal win
            {
                found=true;
                win=a[i][0];
                if(win=='T')
                    win=a[i][1];
                for(int j=0;j<4;j++)
                    {
                     
                     if(a[i][j]=='T')
                            {
                                continue;
                            }
                        if(a[i][j]!=win)
                            {
                                found=false;    
                                break;
                            }
                    }
                if(found&&win!='.')
                    break;
            }
        if(found&&win!='.')
            {
                cout<<"Case #"<<w<<": "<<win<<" won"<<endl;
                continue;
            }
        for(int j=0;j<4;j++)    //chking for vertical win
            {
                found=true;
                win=a[0][j];
                if(win=='T')
                    win=a[1][j];
                for(int i=0;i<4;i++)
                    {
    
                     if(a[i][j]=='T')
                            {
                                continue;
                            }
                        if(a[i][j]!=win)
                            {
                                found=false;    
                                break;
                            }
                    }
                if(found&&win!='.')
                    break;
            }
        if(found&&win!='.')
            {
            cout<<"Case #"<<w<<": "<<win<<" won"<<endl;
            continue;
            }
        found=true;
        win=a[0][3];
        if(win=='T')
            win=a[1][2];
        for(int i=0;i<4;i++)
            {        
            if(a[i][3-i]=='T')
                {
                continue;
                }
                if(a[i][3-i]!=win)
                {
                    found=false;    
                    break;
                }
            }
        if(found&&win!='.')
            {cout<<"Case #"<<w<<": "<<win<<" won"<<endl;
            continue;
            }
        found=true;
        win=a[0][0];
        if(win=='T')
            win=a[1][1];
        for(int i=0;i<4;i++)
            {        
            if(a[i][i]=='T')
                {
                continue;
                }
                if(a[i][i]!=win)
                {
                    found=false;    
                    break;
                }
            }
        if(found&&win!='.')
            {cout<<"Case #"<<w<<": "<<win<<" won"<<endl;
            continue;
            }
        if(draw)
            cout<<"Case #"<<w<<": "<<"Draw"<<endl;
        else
            cout<<"Case #"<<w<<": "<<"Game has not completed"<<endl;
            
    }
    return 0;
}
