#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

void checknonbase(vector<char> &v,string &str);
void checkoppose(vector<char> &v, string &str);

int main()
{
    int T;
    int C;
    int D;
    int N;
    vector<string> strvec;
    ifstream in("B-large.in");
    in>>T;
    for(int i=0; i<T; i++)
    {
         vector<char> base;
         base.push_back('Q');
         base.push_back('W'); 
         base.push_back('E'); 
         base.push_back('R'); 
         base.push_back('A'); 
         base.push_back('S'); 
         base.push_back('D'); 
         base.push_back('F'); 
         vector<char> nonbase;
         vector<char> oppose;
         string series;   
         in>>C;
         for(int j=0; j<C; j++)
         {
             char c,d,e;    
             in>>c;
             in>>d;
             in>>e;
             nonbase.push_back(c);
             nonbase.push_back(d);
             nonbase.push_back(e);           
         }
         in>>D;
         for(int j=0; j<D; j++)
         {
             char c,d;
             in>>c;
             in>>d;
             oppose.push_back(c);
             oppose.push_back(d);        
         }  
         in>>N;
         for(int j=0; j<N; j++)
         {
             char c;
             in>>c;    
             series.push_back(c);
             checknonbase(nonbase,series);
             checkoppose(oppose,series);
         }
        
         strvec.push_back(series);
          
    }
    in.close();
    int count=1;
    ofstream out("output.txt");
    while(!strvec.empty())
    {
        string str = strvec.front();
        strvec.erase(strvec.begin());
        out<<"Case #"<<count<<": "<<"[";
        string::iterator it;
        for(it=str.begin();it<str.end();it++)
        {
            if((it+1)==str.end())
            {
                out<<*it;                         
            }
            else
            {
                out<<*it<<", ";
            }
            
        }
        out<<"]"<<endl;
        count++;                          
    }
    out.close();
    
    
    return 0;    
}



void checknonbase(vector<char> &v,string &str)
{
     vector<char>::iterator it;
     for(it=v.begin(); it<v.end();)
     {
             char c,d,e;
             c = *it;
             it++;
             d = *it;
             it++;
             e = *it;
             it++;
             string::iterator s;
             s=str.end();
             if(c==*(s-1)&&d==*(s-2) || d==*(s-1)&&c==*(s-2))
             {
                 str.erase(s-1);
                 str.erase(s-2);
                 str.push_back(e);                        
             }
             
     }      
}
void checkoppose(vector<char> &v, string &str)
{
     string::iterator s,t;
     s=str.end();
     char c = *(s-1);
     //cout<<c<<endl;
     vector<char>::iterator it;
     for(it=v.begin(); it<v.end();)
     {
         char d,e;
         d=*it;
         it++;
         e=*it;
         it++;
         //cout<<"d="<<d<<" e="<<e<<endl;
         if(c==d)
         {
             for(t=str.begin(); t<str.end(); t++)
             {
                 if(*t == e)
                 {
                     //cout<<"check1 "<<str<<endl;
                     //str.erase(t,str.end());
                     str.clear();
                     break;      
                 }                   
             }    
         }
         if(c==e)
         {
             for(t=str.begin(); t<str.end(); t++)
             {
                 if(*t == d)
                 {
                     //cout<<"check2 "<<str<<endl;
                     //str.erase(t,str.end());
                     str.clear();
                     break;      
                 }                   
             }        
         }                      
     }    
}
