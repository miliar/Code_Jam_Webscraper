#include<iostream>
using namespace std;
char map[5][5],s;
int T,Case;
int main()
{
  //freopen("A-small-attempt0.in","r",stdin);
  //freopen("1111.out","w",stdout); 
   cin>>T;
   getchar();
   Case=0;
   while(T--)
   {
     int end=1,i,j,k,f=0;//ÊÇ·ñ½áÊø 
     for(i=1;i<=4;i++)
      gets(map[i]);
    if(T) getchar();
    // for(int i=1;i<=4;i++)
//       for(int j=0;j<=3;j++)
//       {
//         if(j<3) cout<<map[i][j];
//         else cout<<map[i][j]<<endl;        
//       }
    for(i=1;i<=4;i++)
      for(j=0;j<=3;j++)
       if(map[i][j]=='.') {end=0;break;}
       //ºáÏòÉ¨Ãè 
    for(i=1;i<=4;i++)
    {  
      int flag=1;
      for(k=0;k<=3;k++)
      {
         s=map[i][k];
         if(s=='.') {flag=0;break;}
         else if(s=='T') continue;
         else break;     
      }
      if(!flag) continue;
       for(j=0;j<=3;j++)
        { 
          if(map[i][j]=='.') break;
          if(map[i][j]=='T') continue;
          if(map[i][j]!=s) break;      
        } 
       if(j==4) 
       {
         f=1;cout<<"Case #"<<++Case<<": "<<s<<" won"<<endl;break;      
       }      
    } 
    if(f) continue;  
    //ÊúÏòÉ¨Ãè
    for(i=0;i<=3;i++)
    {
      int flag=1;
      for(k=1;k<=4;k++)
      {
         s=map[k][i];
         if(s=='.') {flag=0;break;}
         else if(s=='T') continue;
         else break;     
      }
      if(!flag) continue;
      for(j=1;j<=4;j++)
      {
        if(map[j][i]=='.') break;
        if(map[j][i]=='T') continue;
        if(map[j][i]!=s) break;              
      } 
      if(j==5)
      { f=1;cout<<"Case #"<<++Case<<": "<<s<<" won"<<endl;break;}                     
    }
    if(f) continue;
    //Ğ±×ÅÉ¨Ãè
    int flag=1;
    for(k=1;k<=3;k++)
    { 
      s=map[k][k-1];
      if(s=='.') {flag=0;break;}
      else if(s=='T') continue; 
      else break;               
    }
    if(flag)
    {
    for(i=1;i<=4;i++)
     {
       if(map[i][i-1]=='T') continue;
       if(map[i][i-1]=='.') break;
       if(map[i][i-1]!=s) break;       
     }
     if(i==5)
     {
       f=1;cout<<"Case #"<<++Case<<": "<<s<<" won"<<endl;        
     }
     }
     if(f) continue;
     flag=1;
    for(k=0;k<=3;k++)
    { 
      s=map[4-k][k];
      if(s=='.') {flag=0;break;}
      else if(s=='T') continue; 
      else break;               
    }
    if(flag)
    {
     int n=4;
     for(i=0;i<=3;i++)
     {
       if(map[n-i][i]=='T')continue;
       if(map[n-i][i]=='.') break;
       if(map[n-i][i]!=s) break;               
     }
     if(i==4)
     {
       f=1;cout<<"Case #"<<++Case<<": "<<s<<" won"<<endl;       
     }
     }
     if(f) continue;
     if(end) cout<<"Case #"<<++Case<<": "<<"Draw"<<endl;
     else cout<<"Case #"<<++Case<<": "<<"Game has not completed"<<endl;
   } 
   //system("pause");
   return 0;
}
