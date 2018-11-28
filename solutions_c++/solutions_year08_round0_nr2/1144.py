#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<stdio.h>
using namespace std;
void trainTimetable(vector <int> aStart,vector <int> bEnd,vector <int> bStart,vector <int> aEnd)
{
     int totala=0, totalb=0, noa=0,nob=0;
     for(int time=0;time<7440;time++)
     {
             for(int j=0;j<aEnd.size();j++)
             {
                     if(aEnd[j]==time)
                            noa++;        
             }  
             for(int i=0;i<aStart.size();i++)
             {
                     if(aStart[i]==time && noa>0)
                           noa--;
                     else if(aStart[i]==time && noa==0)
                          totala++;     
             }  
             for(int j=0;j<bEnd.size();j++)
             {
                     if(bEnd[j]==time)
                            nob++;        
             }    
             for(int i=0;i<bStart.size();i++)
             {
                     if(bStart[i]==time && nob>0)
                              nob--;
                     else if(bStart[i]==time && nob==0)
                              totalb++;        
             }    
     }
     cout<<totala<<" "<<totalb;
}
int main()
{
    int k;
    cin>>k;
    int tt,a,b;
    for(int i=0;i<k;i++)
    {
           int t, na,nb;
           cin>>tt;
           cin>>a>>b; 
           vector <int> naa; 
           vector <int> nab;
           for(int j=0;j<a;j++)
           {
                    string s;
                    cin>>s;
                    int hh,mm;
                    sscanf(s.c_str(),"%d:%d",&hh,&mm);  
                    naa.push_back(hh*60+mm);  
                    cin>>s;
                    sscanf(s.c_str(),"%d:%d",&hh,&mm); 
                    nab.push_back(hh*60+mm+tt);    
                    //cout<<naa[j]<<"\t"<<nab[j];
           }
           vector <int> nba; 
           vector <int> nbb;
           for(int j=0;j<b;j++)
           {
                    string s;
                    cin>>s;
                    int hh,mm;
                    sscanf(s.c_str(),"%d:%d",&hh,&mm);  
                    nba.push_back(hh*60+mm);  
                    cin>>s;
                    sscanf(s.c_str(),"%d:%d",&hh,&mm); 
                    nbb.push_back(hh*60+mm+tt);  
                  //  cout<<nba[j]<<"\t"<<nbb[j];  
           }
           cout<<"Case #"<<(i+1)<<": ";
           trainTimetable(naa,nab,nba,nbb);
           
           if(i!=(k-1))
                       cout<<endl;
    }
    getchar();
    getchar();
    return 0;    
}
