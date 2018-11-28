#include <iostream>
#include <map>
#include <set>
using namespace std;





map <string, set <string> > data;

int T;
int N,M;
int br = 0;



void isinside(string vertex,string candidate)
 {
  string next = "";
  string nc = "";
  bool match = 0;
  int i;
  
   for(i = 1; i < candidate.size(); i++) 
    {
     if(candidate[i] == '/' && match == 0)
      {
       match = 1;
       nc+='/';
      }
      else 
       {
        if(match == 0)
          {
           next += candidate[i];
          }
          else
           {
            nc+=candidate[i];
           }
       }
    } 
    
   // cout<<vertex<<endl;
   // cout<<next<<"----->"<<nc<<endl;
   if(data[vertex].find(next) != data[vertex].end())
    {
     if(nc.size() != 0) 
     isinside((vertex + (next + '/')),nc);
    }
   else
   {
    br++;
    data[vertex].insert(next);
    if(nc.size() != 0)
    isinside((vertex + (next + '/')),nc);
    }
 }


int main()
{
    int i;
    cin>>T;
     for(i = 1; i <= T; i++)
      {
       cin>>N>>M;
        int j;
        data.clear();
        br = 0;
        string temp;
         for(j = 1; j <= N; j ++)
          {
           cin>>temp;
           //cout<<temp<<endl;
            int k;
            string root = "/"; 
            string next = "";
             for(k = 1; k < temp.size(); k++)
              {
               if(temp[k] == '/')
                {
                // cout<<root<<"-->"<<next<<endl;
                 data[root].insert(next);
                 root = root + (next + '/');
                 next = "";
                }
                else
                {
                 next+=temp[k];
                }
              } 
                //cout<<root<<"-->"<<next<<endl;
               
              data[root].insert(next);
           
         
          }
         for(j = 1; j <= M; j++)
          {
           cin>>temp;
           isinside("/",temp);          
          } 
        printf("Case #%d: %d\n",i,br);        
      }
    return 0;
}
