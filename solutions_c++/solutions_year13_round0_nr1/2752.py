#include<iostream>
using namespace std;
typedef long long LL;
char arr[10][10];
int col(char o)
{
    bool flag=0;        
    for(int i=0;i<4;i++)
    {
       int co=0,ct=0;            
       for(int j=0;j<4;j++)
       {
            if(arr[i][j]==o) co++;
            else if(arr[i][j]=='T') ct++;   
       }     
       if(co==4) flag=1;
       if(co==3 && ct==1) flag=1;
       //cout<<o<<" "<<i<<" "<<co<<" "<<ct<<"\n";
    }
    return flag;
}

int row(char o)
{
    bool flag=0;
    for(int i=0;i<4;i++)
    {
       int co=0,ct=0;                
       for(int j=0;j<4;j++)
       {
            if(arr[j][i]==o) co++;
            else if(arr[j][i]=='T') ct++;   
       }     
       if(co==4) flag=1;
       if(co==3 && ct==1) flag=1;
       //cout<<o<<" "<<i<<" "<<co<<" "<<ct<<"\n";       
    }
    return flag;
}

int diag(char o)
{
    bool flag=0;
    int co=0,ct=0;                
    for(int i=0;i<4;i++)
    {           
       {
            if(arr[i][i]==o) co++;
            else if(arr[i][i]=='T') ct++;   
       }     
       if(co==4) flag=1;
       if(co==3 && ct==1) flag=1;
    }
    //cout<<o<<" diag1 "<<" "<<co<<" "<<ct<<"\n";
           
    co=0,ct=0;            
    for(int i=0;i<4;i++)
    {       
       {
            if(arr[3-i][i]==o) co++;
            else if(arr[3-i][i]=='T') ct++;   
       }     
       if(co==4) flag=1;
       if(co==3 && ct==1) flag=1;
    }
    //cout<<o<<" diag1 "<<" "<<co<<" "<<ct<<"\n";
    return flag;
}


int main()
{
    int t,a=1;
    cin>>t;
    while(t--)
    {
        int dot=0;
        for(int i=0;i<4;i++)      
            cin>>arr[i];      
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(arr[i][j]=='.') dot++;
        if(col('O') || row('O') || diag('O'))
        {
            printf("Case #%d: O won",a++);       
        } else if(col('X') || row('X') || diag('X')) 
        {
            printf("Case #%d: X won",a++);                      
        } else if(dot==0)
        {
              printf("Case #%d: Draw",a++); 
        } else
        {
              printf("Case #%d: Game has not completed",a++);
        }
        printf("\n");
    }
}
