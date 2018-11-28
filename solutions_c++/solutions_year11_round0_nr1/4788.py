#include<iostream>
#include<conio.h>
#include<fstream>

using namespace std;

int main()
{
     int test;
     ofstream outputFile;
     outputFile.open("bot_out.txt");
     scanf("%d",&test);
     
     char bot[101];
     int pos[101];
     
     int count=0,t=1,n=0,poso=1,posb=1,time=0,movo,movb,mov;
     bot[0]=pos[0]=-1;
     
     
     while(t<=test)
     {
                  poso=1;posb=1;
                  time=0;
                  scanf("%d",&n);
                  for (int i=1; i<=n; i++)
                  {
                      cin>>bot[i];
                      cin>>pos[i];
                  }
                  //Read 1 line till here
                  for (int i=1; i<=n; i++)
                  {
                      if(bot[i]=='B')
                      {
                                     mov=pos[i]-posb;
                                     mov=abs(mov);
                                     mov=mov+1;
                                     time += mov;cout<<"time here="<<time<<endl;
                                     posb=pos[i];
                                     for(int j=i+1; j<=n; j++)
                                     {
                                             if (bot[j]=='O')
                                             {
                                                             if(poso < pos[j])
                                                             {      
                                                                    poso=poso+mov;
                                                                    if(poso>pos[j])
                                                                                   poso=pos[j];
                                                             } 
                                                             else
                                                             {      
                                                                    poso=poso-mov;
                                                                    if(poso<pos[j])
                                                                                   poso=pos[j];
                                                             }    
                                                             break;                
                                             }
                                             
                                     }
                      }//end of if part
                      
                      else
                      {
                                     mov=pos[i]-poso;
                                     mov=abs(mov);
                                     mov=mov+1;
                                     time += mov;cout<<"time="<<time<<endl;
                                     poso=pos[i];
                                     for(int j=i+1; j<=n; j++)
                                     {
                                             if (bot[j]=='B')
                                             {
                                                             if(posb < pos[j])
                                                             {      
                                                                    
                                                                    posb=posb+mov;
                                                                    if(posb>pos[j])
                                                                                   posb=pos[j];
                                                             } 
                                                             else
                                                             {      
                                                                    
                                                                    posb=posb-mov;
                                                                    if(posb<pos[j])
                                                                                   posb=pos[j];
                                                             }    
                                                             break;                
                                             }
                                             
                                     }
                      }//end of else
                    
                    
                    }
                    //cout<<"Case #"<<t<<":"<<time;
                    outputFile << "Case #"<<t<<": "<<time<<endl;
                    cout<<endl;
                    

     t++;                 
     }
     outputFile.close();
     system("PAUSE");
     return 0;
}
