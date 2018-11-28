#include <iostream>
#include <sstream>
#include<stdlib.h>
#include <string>

using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int num;
        cin>>num;
        string stats[num];
        float wp[num];
        float op[num];
        float oopf[num];
        for(int j=0;j<num;j++)
        {
                cin>>stats[j];
                float win=0;
                int draw=0;
                for(int k=0;k<num;k++)
                {
                      if(stats[j][k]=='1') win++;
                      if(stats[j][k]=='.') draw++;
                }
                wp[j]=win/(num-draw);
               
        }
       
       
        for(int j=0;j<num;j++)
        {       float f=0; int t=0;
                for(int k=0;k<num;k++)
                {
                       if(stats[j][k]!='.')
                       {
                              t++;
                              float win=0; float total=0;
                              for(int l=0;l<num;l++)
                              {   
                                   if(j==l) continue;
                                   if(stats[k][l]=='1'){ win++;}
                                   if(stats[k][l]!='.'){total++;}
                              }
                              f+= win/total;
                       }
                }
                op[j]=f/t;       }
       
       
        for(int j=0;j<num;j++)
        {       float f=0; int t=0;
                for(int k=0;k<num;k++)
                {
                       if(stats[j][k]!='.')
                       {
                              t++;
                              f+=op[k];
                       }
                }
                oopf[j]=f/t;
        }
        cout<<"Case #"<<i+1<<":"<<endl;
        for(int j=0;j<num;j++)
        {
        float answer= 0.25*wp[j]+0.5*op[j]+0.25*oopf[j];
        cout<<answer<<endl;
        }
    }
    return 0;
}
