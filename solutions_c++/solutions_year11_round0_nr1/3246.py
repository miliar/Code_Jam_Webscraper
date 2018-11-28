#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    
    int i;
    ifstream  in(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;
    
    int cases=0;
    while(cases<t)
          {      int bot[2][2];
                     bot[0][0]=0;//orange time
                     bot[0][1]=1;//orange pos
                     bot[1][0]=0;//blue
                     bot[1][1]=1;
                 int n;
                 int time=0;
                 in>>n;
                 int prs=0;
              //   cout<<"\n---------"<<endl;
                 while(prs<n)
                   {         
                             string str;
                             int pos;
                             in>>str;//cout<<str;
                             if(str=="O")i=0;
                             else i=1;
                             in>>pos;//cout<<pos;
                             int temp;
                             temp=pos-bot[i][1];
                             if(temp<0)temp=temp*(-1);
                             if((time-bot[i][0])<temp)
                                 {
                                  time=time + (temp-(time-bot[i][0]));
                                  time++;
                                  bot[i][0]=time;
                                  bot[i][1]=pos;
                                 } 
                              else{
                                   time++;
                                   bot[i][0]=time;
                                   bot[i][1]=pos;
                                   }
                             
                             
                   prs++;
                   }
                   
                  
                  cases++;
                  out<<"Case #"<<cases<<": "<<time<<endl;
          }

    
    return 1;
    
}
