#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

float dis(int x1,int y1,int x2,int y2)
      {
      return  sqrt( (x2-x1)*(x2-x1) + (y1-y2)*(y1-y2) ); 
      }
      
int area1(int x1,int y1,int x2,int y2,int x3,int y3)
      {
              /*
      float S=0;
      float A=dis(x1,y1,x2,y2);
      float B=dis(x3,y3,x2,y2);
      float C=dis(x1,y1,x3,y3); 
      S=(A+B+C)/2;
      
      return (int)(4*( S*(S-A)*(S-B)*(S-C) ));
      */
      int ans;
      ans = ( (x1-x2)*(y2-y3) - (x2-x3)*(y1-y2) );
      return ans;
      }

int main()
{
    
    int N,M;
    //float 
    long long A;
    int c;
//    int x2,y2,x3,y3;
    long long area; 
    
    cin>>c;
    for(int i=1;i<=c;i++)
            {
            cin>>N>>M>>A;             
            //cout<<N<<" "<<M<<" "<<A<<endl;
            int x1=0,y1=0;
      for(int x2=0;x2<=N;x2++)
              for(int y2=0;y2<=M;y2++)
                          for(int x3=0;x3<=N;x3++)
                             for(int y3=0;y3<=M;y3++)
                                     if( area1(x1,y1,x2,y2,x3,y3) == A )
                                                {
                                     printf("Case #%d: %d %d %d %d %d %d\n",i,0,0,x2,y2,x3,y3);
                                     goto end;                                
                                                }                     
              printf("Case #%d: IMPOSSIBLE\n",i);
              end: ;
              }
return 0;
}
