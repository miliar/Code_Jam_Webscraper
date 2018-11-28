using namespace std;
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<queue>

typedef long long int int64;

int main()
{
    int64 t,i,j,k,n,ans,mx,x,y,fill;
    
    
    //freopen("inl.txt","r",stdin);
    //freopen("outl.txt","w",stdout);
    
    scanf("%lld",&t);
    for(mx=1; mx<=t; mx++)
    {
     char st[11][11],bl[10],anss[20];         
     for(i=0; i<4; i++)         
      scanf("%s",st[i]); 
     
     fill=0; x=y=-1;      
     ans =0;
     
     for(i=0; i<4; i++) { for(j=0; j<4; j++) {if(st[i][j]=='T'){x=i; y=j;}if(st[i][j]=='.')fill++;}}
     
     st[x][y]='X';
     if((strcmp(("XXXX"),st[0])==0)||(strcmp(("XXXX"),st[1])==0)||(strcmp(("XXXX"),st[2])==0)||(strcmp(("XXXX"),st[3])==0))ans=1;
     //if(((strcmp("TXXX"),st[0])==0)||((strcmp("XTXX"),st[1])==0)||((strcmp("XXTX"),st[2])==0)||((strcmp("XXXT"),st[3])==0))ans=1;
     
     if((st[0][0]=='X')&&(st[1][0]=='X')&&(st[2][0]=='X')&&(st[3][0]=='X')) ans=1;
     if((st[0][1]=='X')&&(st[1][1]=='X')&&(st[2][1]=='X')&&(st[3][1]=='X')) ans=1;
     if((st[0][2]=='X')&&(st[1][2]=='X')&&(st[2][2]=='X')&&(st[3][2]=='X')) ans=1;
     if((st[0][3]=='X')&&(st[1][3]=='X')&&(st[2][3]=='X')&&(st[3][3]=='X')) ans=1;
      
     if((st[0][0]=='X')&&(st[1][1]=='X')&&(st[2][2]=='X')&&(st[3][3]=='X')) ans=1;
     if((st[0][3]=='X')&&(st[1][2]=='X')&&(st[2][1]=='X')&&(st[3][0]=='X')) ans=1;      
     
     
     if(ans==0)
     { 
     if(x>-1 && y>-1) st[x][y]='O';            
     if((strcmp(("OOOO"),st[0])==0)||(strcmp(("OOOO"),st[1])==0)||(strcmp(("OOOO"),st[2])==0)||(strcmp(("OOOO"),st[3])==0))ans=2;
     //if(((strcmp("TOOO"),st[0])==0)||((strcmp("OTOO"),st[1])==0)||((strcmp("OOTO"),st[2])==0)||((strcmp("OOOT"),st[3])==0))ans=2;    
     
     if((st[0][0]=='O')&&(st[1][0]=='O')&&(st[2][0]=='O')&&(st[3][0]=='O')) ans=2;
     if((st[0][1]=='O')&&(st[1][1]=='O')&&(st[2][1]=='O')&&(st[3][1]=='O')) ans=2;
     if((st[0][2]=='O')&&(st[1][2]=='O')&&(st[2][2]=='O')&&(st[3][2]=='O')) ans=2;
     if((st[0][3]=='O')&&(st[1][3]=='O')&&(st[2][3]=='O')&&(st[3][3]=='O')) ans=2;
     
     if((st[0][0]=='O')&&(st[1][1]=='O')&&(st[2][2]=='O')&&(st[3][3]=='O')) ans=2;
     if((st[0][3]=='O')&&(st[1][2]=='O')&&(st[2][1]=='O')&&(st[3][0]=='O')) ans=2;      
     
     }
     
     if(ans==0 && fill>0) ans=4;
     if(ans==0 && fill==0) ans=3;
     //cout<<"#"<<fill<<endl;
     if(ans==1) strcpy(anss,"X won");
     if(ans==2) strcpy(anss,"O won");
     if(ans==3) strcpy(anss,"Draw");
     if(ans==4) strcpy(anss,"Game has not completed");
     printf("Case #%lld: %s\n",mx,anss);
     //scanf("%s",bl);
    }
    
    return 0;
}
