#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
using namespace std;
int t,na,nb;
int resa,resb;
int flag1[10001],flag2[10001];
vector < int > ta[10001],tb[10001];
char pal1[100],pal2[100];
string s1,s2,s3,s4;
bool searchA( int a )
{
    for(int r=0;r<=a;r++)
      if(flag1[r])
       {
           flag1[r]--;
           return true;     
       }   
     return false;
}
bool searchB( int a )
{
    for(int r=0;r<=a;r++)
      if(flag2[r])
       {
           flag2[r]--;
           return true;     
       }   
     return false;
}
int main()
{
    int N;
    scanf("%d",&N);
    for(int H=0;H<N;H++)
    {
        memset(flag1,0,sizeof(flag1));
        memset(flag2,0,sizeof(flag2));
        for(int r=0;r<2000;r++)
          ta[r].clear(),tb[r].clear();        
          resa=resb=0;
    scanf("%d",&t);
    scanf("%d%d",&na,&nb);
    for(int r=0;r<na;r++)
     {
       scanf("%s %s",pal1,pal2); 
       string S1=pal1,S2=pal2; 
       string s1,s2,s3,s4;
       s1+=S1.substr(0,2);
       s2+=S1.substr(3,2);
       s3+=S2.substr(0,2);
       s4+=S2.substr(3,2);  
       int t1=atoi( s1.c_str() )*60+atoi( s2.c_str() );
       int t2=atoi( s3.c_str() )*60+atoi( s4.c_str() );  
       ta[t1].push_back( t2+t );
     }   
    for(int r=0;r<nb;r++)
     {
       scanf("%s %s",pal1,pal2);    
       string S1=pal1,S2=pal2; 
       string s1,s2,s3,s4;
       s1+=S1.substr(0,2);
       s2+=S1.substr(3,2);
       s3+=S2.substr(0,2);
       s4+=S2.substr(3,2);
       int t1=atoi( s1.c_str() )*60+atoi( s2.c_str() );
       int t2=atoi( s3.c_str() )*60+atoi( s4.c_str() ); 
       tb[t1].push_back( t2+t );
     }   
     for(int r=0;r<24*60;r++)
     {
           if(ta[r].size())
              for(int c=0;c<ta[r].size();c++)              
              {
                if(!searchA(r))
                  resa++;
                    flag2[ta[r][c]]++;      
              }      
           if(tb[r].size())
              for(int c=0;c<tb[r].size();c++)
              {
                if(!searchB(r))
                  resb++;
                    flag1[tb[r][c]]++;       
              }     
     }
    printf("Case #%d: %d %d\n",H+1,resa,resb);
   }
    return 0;
}
/*
5
2 2
10:30 10:35
10:35 10:41
10:40 11:30
10:45 12:00


*/
