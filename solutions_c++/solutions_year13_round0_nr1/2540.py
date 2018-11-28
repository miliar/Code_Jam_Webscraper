#include<iostream>
using namespace std;
int main()
{
  freopen("C:\\Users\\Dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\Dell\\Desktop\\output.txt","w",stdout);  
    int t1,t;
    cin>>t1;
    for(t=1;t<=t1;t++)
    {   char a[4][4],sign;int i,j,c=0,tt=0,d=0,row=0,col=0,win=0;
        for(i=0;i<4;i++)
        {
                        for(j=0;j<4;j++)
                        {cin>>a[i][j];
                        if(a[i][j]=='T')
                        {row=i;col=j;tt=1;}
                        if(a[i][j]=='.')
                        d=1;}
        }
        if(tt==1)
        {
                if(row==col)
                {
                            if(row>0)
                            sign=a[0][0];
                            else
                            sign=a[1][1];
                            if(sign!='.')
                            {
                            for(i=0;i<4;i++)
                            {
                                            if(i==row)
                                            continue;
                                            if(a[i][i]!=sign)
                                            {c=1;break;}
                            }
                            
                
                if(c==0){cout<<"Case #"<<t<<": "<<sign<<" won"<<endl;win=1;}}}  
                if(win==0)
                {
                if((row+col)==3)
                {c=0;
                              if(row>0)
                              sign=a[0][3];
                              else
                              sign=a[1][2];
                              if(sign!='.')
                              {
                              for(i=0;i<4;i++)
                              {
                                              if(i==row)
                                              continue;
                                              if(a[i][3-i]!=sign)
                                              {c=1;break;}
                              }
                              
                
                
                if(c==0){cout<<"Case #"<<t<<": "<<sign<<" won"<<endl;win=1;}} }} 
                if(win==0)
                {c=0;
                if(row>0)
                sign=a[0][col];
                else
                sign=a[1][col];
                if(sign!='.'){
                for(i=0;i<4;i++)
                {
                                if(i==row)
                                continue;
                                if(a[i][col]!=sign)
                                {c=1;break;}
                }
                
                if(c==0){cout<<"Case #"<<t<<": "<<sign<<" won"<<endl;win=1;}}} 
                if(win==0)
                {
                c=0;
                if(col>0)
                sign=a[row][0];
                else
                sign=a[row][1];
                if(sign!='.')
                {
                for(i=0;i<4;i++)
                {
                                if(i==col)
                                continue;
                                if(a[row][i]!=sign)
                                {c=1;break;}
                }
                
                if(c==0){cout<<"Case #"<<t<<": "<<sign<<" won"<<endl;win=1;}                                                                   
                }}}if(win==0){
                   for(i=0;i<4;i++)
                   {
                                   if(a[i][0]==a[i][1] && a[i][1]==a[i][2] && a[i][2]==a[i][3] && a[i][3]!='.')
                                   {cout<<"Case #"<<t<<": "<<a[i][0]<<" won"<<endl;               
                                     win=1;}
                                     
                                     
                                  else if(a[0][i]==a[1][i] && a[1][i]==a[2][i] && a[2][i]==a[3][i] && a[3][i]!='.')
                                   {cout<<"Case #"<<t<<": "<<a[0][i]<<" won"<<endl;               
                                     win=1;}
                                     }
                                    if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[0][0]!='.' && win==0)
                                   {cout<<"Case #"<<t<<": "<<a[0][0]<<" won"<<endl;               
                                     win=1;}
                                     if(a[0][3]==a[1][2] && a[1][2]==a[2][1] && a[3][0]==a[2][1] && a[0][3]!='.' && win==0)
                                    { cout<<"Case #"<<t<<": "<<a[0][3]<<" won"<<endl;               
                                     win=1;}
                                     
                                     
                                     if(win==0 && d==0)
                                     cout<<"Case #"<<t<<": "<<"Draw"<<endl;
                                     else if(win==0 && d==1)
                                     cout<<"Case #"<<t<<": "<<"Game has not completed"<<endl; 
                                     }}return 0;}                           
                                      