#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <conio.h>
using namespace std;

int formnumber(string number)
{
    int len = number.size(); 
    //cout<<"\nthe length is "<<len;   
    int num=0;
    for(int i=0;i<len;i++)
    {
            num*=10;
            num+=number[i]-48;
    }
    //cout<<"inside the form number part.. return ing "<<num;
    return num;            
}

string formstring(fstream& inp)
{
    string number;
    while(1)
    {
           char e;
           inp.get(e);
           if(e=='\n' || inp.eof())
                      break;
           number=number+e;     
    }
    return number;
}

int main(void)
{
    /*** Taking in the total number of test cases ***/   
    int N;
    fstream inp("A-large.in",ios::in|ios::binary);
    string number;
    number=formstring(inp);  
    //cout<<"\n the string form of the number is "      <<number;
    N=formnumber(number);    
    //cout<<"\n The no of test case is "<<N;
    
    /************************************************/
    
    /***** Scanning in the inputs for each test case and processing them *****/
    for(int i=1;i<=N;i++)
    {            
            /*** forming the number of search engines ***/
            int S;
            {
            string number;            
            number=formstring(inp);            
            S=formnumber(number);            
            }
            /********************************************/
            
            /*** forming the search engine vector ***/
            vector<string> engine;
            for(int j=1;j<=S;j++)
            {
                    string eng;                    
                    eng=formstring(inp);                    
                    engine.push_back(eng);                                        
            }
            /****************************************/
            
            /*** forming the number of querries ***/
            int Q;
            number=formstring(inp);            
            Q=formnumber(number);
            /**************************************/
            
            /*** forming the querry vector ***/
            vector<string> querry;
            for(int j=1;j<=Q;j++)
            {
                    string qer;
                    qer=formstring(inp);
            
                    querry.push_back(qer);
            }
            /*********************************/
            
            /*************** Processing ***************/
            //cout<<"\nInto the processing arena";
            unsigned int switches=0;
            int count=0,criticalsize=engine.size();            
            map<string,int> enginemap;            
            for(int j=0;j<engine.size();j++)
            enginemap.insert(std::pair<string,int>(engine[j],0));            
            for(int j=0;j<querry.size();j++)
            {
                    
                  if(enginemap[querry[j]]==0)
                  {                
                      count++;                    
                      enginemap[querry[j]]=1;                          
                  }                        
                  if(count==criticalsize)
                  {
                           switches++;
                           enginemap.erase(enginemap.begin(),enginemap.end());
                           for(int k=0;k<engine.size();k++)
                              enginemap.insert(std::pair<string,int>(engine[k],0));
                           if(criticalsize == engine.size())
                                           criticalsize--;
                           enginemap[querry[j]]=1;
                           //cout<<"\n\n enginemap at "<<querry[j]<<" = "<<enginemap[querry[j]];
                           count=0;
                  }      
                  //cout<<"\nquerr is "<<querry[j]<<"\n and count is "<<count;
                    
            }
            //cout<<"\n querry list  is over. ";
            /******************************************/
            
            cout<<"\nCase #"<<i<<": "<<switches;            
    }
    /*************************************************************************/
    inp.close();
    getch();
    return 0;
}




