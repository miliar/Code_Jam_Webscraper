#include <fstream>
#include<iostream>
#include<conio.h>
using namespace std;

int max1(int p[3])
{
    int t1=(p[1]>=p[2])?p[1]:p[2];        
    return (p[0]>=t1)?p[0]:t1;
}
int check(int total, int p[3], int goal)
{
     //3 types of score possible :    x x x    or    x x x+1   or   x x+1 x+1
     int m=max1(p),s=0;
     if(p[2]==0)//no surprise possible :(                  
          return 0;
     if((p[1]==0) && (p[2]==1))//no surprise possible :(
          return 0;     
     if(goal==m+1 && p[1]==p[2])  //surprise possible if score is form x x x   or    x x+1 x+1 
          return 1;//achievable 
     else 
          return 0;    
}
int main()
{
     int T,N,S,P,max,temp,normal=0,surprise=0,h=0;
     int total; //total score
     int num[3]={10,10,10};
     char ch;
     ifstream fi("qualify2large.in");     
     ofstream fo("qualify2large.out");     
     fi>>T;       
     for(int i=0;i<T;i++)//for every test case
     {
         fi>>N>>S>>P;         
         normal=0;
         surprise=0;
         fo<<"Case #"<<i+1<<": ";
         for(int j=0;j<N;j++)//for every googler
         {
             fi>>total;    
             num[0]=num[1]=num[2]=10;
             max=30;
             h=0; 
             do
             {
                  temp=num[0]+num[1]+num[2];                
                  if(temp>total)
                  num[h]--;  
                  else if(temp==total)       
                  {
                       if(max1(num)>=P) 
//if max score is greater than or equal to required score(P), this googler is a contender for normal score as well as surprising score
                       {
                           normal++;
                           break;
                       }
                       //otherwise check if googler can get required score, atleast with the help of surprised score.
                       if(check(total,num,P))
                           surprise++;
                       break;
                  }
                  else break;
                  h=(h+1)%3; //decrementing each score in round robin fashion, only normal scores possible this way                                                 
             }while(num[0]>=0);
         }
          if(S>=surprise)            
                 fo<<(normal+surprise)<<endl; // all surprised googlers plus the normal googlers which may compensate for extra 'S'
             else
                 fo<<(normal+S)<<endl;         //all normal googlers plus only 'S' of the surprised googlers
     }
     fi.close();  
     fo.close();     
     cout<<"completed";
     getch();
}
