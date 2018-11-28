#include<stdio.h>
#include<fstream>
#include<iostream>
#include<string>
#include<vector>
#include<iterator>
#include<map>
#include<cmath>
#include<deque>

#include<sstream>
using namespace std;

//ostream cout("large.out");
//ofstream cout("small.out");


void proccess();

map<string,bool>searchE;
deque<string>querys;
 
int main()
{
   // ifstream cin("sample.in");
    ifstream cin("A-small.in");
    //ifstream cin("A-large.in");
    
    int testCases,i,numSE,numQ,j;
    char aux[102];
    
    
    cin>>testCases;
    
    for(i=0;i<testCases;i++)
    {
        querys.clear();
        searchE.clear();
        
        cin>>numSE; 
        cin.get();
        
        for(j=0;j<numSE;j++)
        {
           
            cin.getline(aux,101);
            
            searchE[aux]=false;
            
        }
        
        cin>>numQ;
        cin.get();
       
        for(j=0;j<numQ;j++)
        {
            cin.getline(aux,101);
            querys.push_back(aux);
           
        }
        
        cout<<"Case #"<<(i+1)<<": ";
        proccess();
        cout<<endl;
        //break;
    }
    
    
    system("pause");
    
}



void proccess()
{
     int remainds,switchs=0,i;
     
    // copy(searchE.begin(),searchE.end(),ostream_iterator<bool>(cout,", "));
      
    map<string,bool>auxS=searchE;
        
    remainds=searchE.size();
      for(i=0;i<querys.size();i++)
     {
            if(searchE.count(querys[i])>0&&searchE[querys[i]]==false)
            {
                remainds--;    
                searchE[querys[i]]=true;
                
                if(remainds==0)
                {
                    switchs++;  
                   remainds=searchE.size()-1; 
                    searchE=auxS; 
                    searchE[querys[i]]=true;
                    
                }
                
            }
            
            
      }
    
    cout<<switchs;
    
}


