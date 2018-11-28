#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int temp,T;
        //freopen("A-large.in","r",stdin);
  //freopen("key.txt","w",stdout);
    cin>>T;
    getchar();
    char test[5][5];
    for(int i=0;i<T;i++)
    {
         for(int j=0;j<4;j++)
         {
             for(int k=0;k<4;k++)
             {
                     test[j][k]=getchar();
             }   
             getchar();
         }     

    
          getchar();
          int WinOfO=0;
          int WinOfX=0;
          int numberOfDot=0;
          int WinOfPotential=0;
          for(int j=0;j<4;j++)
          {
          int numberOfT=0;
          int numberOfO=0;
          int numberOfX=0;
     
             for(int k=0;k<4;k++)
             {
                if(test[j][k]=='O')
                        numberOfO+=1;
                else
                if(test[j][k]=='X')
                        numberOfX+=1;
                 else
                 if(test[j][k]=='T')
                        numberOfT+=1;  
                 else
                        numberOfDot+=1;     
             }
             if(numberOfO>=3&&numberOfT+numberOfO==4)
                          WinOfO+=1;
             else
             if(numberOfX>=3&&numberOfT+numberOfX==4)
                          WinOfX+=1;
             else
             if(numberOfT<=1&&(numberOfX+numberOfDot+numberOfT==4||numberOfO+numberOfDot+numberOfT==4))
                         WinOfPotential+=1;   
         }     
         //cout<<numberOfDot<<endl;
          for(int j=0;j<4;j++)
          {
          int numberOfT=0;
          int numberOfO=0;
          int numberOfX=0;
     
             for(int k=0;k<4;k++)
             {
                if(test[k][j]=='O')
                        numberOfO+=1;
                else
                if(test[k][j]=='X')
                        numberOfX+=1;
                 else
                 if(test[k][j]=='T')
                        numberOfT+=1;
                 else
                        numberOfDot+=1;                                    
             }
             if(numberOfO>=3&&numberOfT+numberOfO==4)
                          WinOfO+=1;
             else
             if(numberOfX>=3&&numberOfT+numberOfX==4)
                          WinOfX+=1;
             else
             if(numberOfT<=1&&(numberOfX+numberOfDot+numberOfT==4||numberOfO+numberOfDot+numberOfT==4))
                         WinOfPotential+=1;                  
         }
         //cout<<numberOfDot<<endl;
           int numberOfT=0;
          int numberOfO=0;
          int numberOfX=0;
          for(int j=0;j<4;j++)
          {
        
            if(test[j][j]=='O')
                     numberOfO+=1;
            else
            if(test[j][j]=='T')
                     numberOfT+=1;
            else
            if(test[j][j]=='X')
                     numberOfX+=1;
            else
                      numberOfDot+=1;         
          }
             if(numberOfO>=3&&numberOfT+numberOfO==4)
                          WinOfO+=1;
             else
             if(numberOfX>=3&&numberOfT+numberOfX==4)
                          WinOfX+=1; 
             else
                  if(numberOfT<=1&&(numberOfX+numberOfDot+numberOfT==4||numberOfO+numberOfDot+numberOfT==4))
                         WinOfPotential+=1;                        
          numberOfT=0;
          numberOfO=0;
          numberOfX=0;
//cout<<numberOfDot<<endl;
          for(int j=0;j<4;j++)
          {
        
            if(test[3-j][j]=='O')
                     numberOfO+=1;
            else
            if(test[3-j][j]=='T')
                     numberOfT+=1;
            else
            if(test[3-j][j]=='X')
                     numberOfX+=1;
            else
                        numberOfDot+=1;     
          }
             if(numberOfO>=3&&numberOfT+numberOfO==4)
                          WinOfO+=1;
             else
             if(numberOfX>=3&&numberOfT+numberOfX==4)
                          WinOfX+=1;
             else
             if(numberOfT<=1&&(numberOfX+numberOfDot+numberOfT==4||numberOfO+numberOfDot+numberOfT==4))
                         WinOfPotential+=1;                            
         //cout<<numberOfDot<<endl;
                          
         if(WinOfO>WinOfX)
         cout<<"Case #"<<i+1<<": O won"<<endl;
         else
            if(WinOfX>WinOfO)
         cout<<"Case #"<<i+1<<": X won"<<endl;
         else 
             if(WinOfX==WinOfO&&numberOfDot==0)
             cout<<"Case #"<<i+1<<": Draw"<<endl;
         else      
                    cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
    }
    //cin>>N;
    return 0;
}
