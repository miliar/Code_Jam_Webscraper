#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int T,casee=1;
    fstream file1;
    file1.open("A-small-attempt0.in");
    fstream file2;
    file2.open("A-small.out");
    file1>>T;
    while(T>0)
    {
    int N,M;
    file1>>N>>M;
    string exist[100];
    //exist=new string [N];
    string *neww=0;
    neww=new string [M];
    for(int i=0; i<N; i++)
            file1>>exist[i];
    for(int i=0; i<M; i++)
            file1>>neww[i];   
    int existing=N, newdir=M;
    int steps=0;
    int ct=0;
    while(newdir>0)
    {                  
              bool flag=true;     
              string help=neww[ct];     
              if(neww[ct].size()>0)
              {
                  for(int i=0; i<existing; i++)
                          if(exist[i].compare(help)==0)  flag=false;
                  if(flag==true) 
                  {
                           steps++;
                           existing++;
                           exist[existing-1]=neww[ct];
                           int n=help.size();
                           int i=n-1;
                           int count=n-1;
                           while(help[i]!='/')
                           {
                                   count--;
                                   i--;                               
                           }
                           string daily = help.substr(0, count);
                           neww[ct]=daily;
    
                  }              
                  else
                  {
                      ct++;
                      newdir--; 
                  }         
              }    
              else
              {
                  ct++;
                  newdir--;
              }
    }  
    file2<<"Case #"<<casee<<": "<<steps<<endl;
    T--;
    casee++;
    }     
    file1.close();
    file2.close();
    system("PAUSE");
    return 0;
}
