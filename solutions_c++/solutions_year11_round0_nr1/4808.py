#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    
    ofstream outputFile;
    outputFile.open("bot_out.txt");
    int test;
    char bot[200];
    int pos[200];
    scanf("%d",&test);
    
    for(int i=0;i<test;i++)
      {
         int n;   
         scanf("%d",&n);
         getchar();
         for(int j=0;j<n;j++)
           {
              cin>>bot[j];  
              //cout<<bot[j];
              cin>>pos[j]; 
             //  cout<<pos[j];
           }
         int  time=0,posb=1,poso=1;  
         for(int j=0;j<n;j++)
           {
              
              if(bot[j]=='B')
                {
                             
                    int k=0;         
                   if(posb<pos[j])
                     {
                      
                        k=pos[j]-posb+1;
                       // cout<<k<<" ";
                        time+=pos[j]-posb+1;
                        posb=pos[j];
                     }
                   else if(posb>pos[j])
                     {
                        
                        k=posb-pos[j]+1;
                       //  cout<<k<<" ";
                        time+=posb-pos[j]+1;
                        posb=pos[j];
                     }
                   else if(posb==pos[j])
                     {
                       time++;
                       k=1;
                     }
                for(int m=j+1;m<n;m++)
                  {  
                     if(bot[m]=='O')
                       {
                         if(poso>pos[m])
                           {
                              int t=poso-pos[m];
                              if(k>t)
                                poso=pos[m]; 
                              else
                                poso-=k;
                           }
                         else if(poso<pos[m])
                           {
                              int t=pos[m]-poso;
                              if(k>t)
                                poso=pos[m]; 
                              else
                                poso+=k;
                           }
                           break;
                 
                         }                            
                    }  
                 }
                 
               
               
              else if(bot[j]=='O')
                {
                             
                    int k=0;         
                   if(poso<pos[j])
                     {
                       
                        k=pos[j]-poso+1;
                      //   cout<<k<<" ";
                        time+=pos[j]-poso+1;
                        poso=pos[j];
                     }
                   else if(poso>pos[j])
                     {
                       
                        k=poso-pos[j]+1;
                      //   cout<<k<<" ";
                        time+=poso-pos[j]+1;
                        poso=pos[j];
                     }
                   else if(poso==pos[j])
                     {
                       time++;
                       k=1;
                     }
                     
                 for(int m=j+1;m<n;m++)
                   {    
                   if(bot[m]=='B')
                     {
                         if(posb>pos[m])
                           {
                              int t=posb-pos[m];
                              if(k>t)
                                posb=pos[m]; 
                              else
                                posb-=k;
                           }
                         else if(posb<pos[m])
                           {
                              int t=pos[m]-posb;
                              if(k>t)
                                posb=pos[m]; 
                              else
                                posb+=k;
                           }
                         break;  
                        } 
                                                   
                     } 
                 }
                 
            } 
            
         outputFile << "Case #"<<i+1<<": "<<time<<endl;
      }
       outputFile.close();
 // system("pause");

return 0;
}       
                     
                     
                     
                     
                   
                   
                   
                   
                   
                                           
            
