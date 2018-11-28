/*
 * Google code jam: MagicKa
 * 
 * Author: Jim
 * Date: 2011-05-07 Sat.
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;
  
typedef struct com
{
   char a;
   char b;
   char x;         
}com;

typedef struct oppo
{
   char a;
   char b;       
}oppo;

void solve();

int main(void)
{
    int n;

    freopen("in_2.txt","r",stdin); 
    freopen("out_2.txt","w",stdout); 


    //Add Your Code Here
    cin >> n;
    for(int i=0; i<n; i++)
    {
        cout <<"Case #"<<i+1<<": ";
        solve();
    }


    fclose(stdin);
    fclose(stdout);

    return EXIT_SUCCESS;
}

void solve()
{
  int c = 0;
  int d = 0;
  int n = 0;
  
  int i = 0;
  int j = 0;
  int k = 0;
  char str[3];
  
  
  com *com_list = NULL;
  
  cin >> c;
  if(c != 0)
    com_list = new com[c];
  for(i=0; i<c; i++)
  {
      cin >> str;
      com_list[i].a = str[0];  
      com_list[i].b = str[1]; 
      com_list[i].x = str[2];       
  }
  
  oppo *op_list = NULL;
  
  cin >> d;
  if(d != 0)
     op_list = new oppo[d];
     
  for(i=0; i<d; i++)
  { 
      cin >> str;
      op_list[i].a = str[0];
      op_list[i].b = str[1];  
  }
  
  cin >> n;
  char *magic = NULL;
  magic = new char[n];
  int idx = 0;
  getchar();
  for(j=0; j<n; j++)
  {
      char ch;
      ch = getchar(); 
     // cout << ch << "-";
      bool com_flag = false;
      
      if(idx == 0)
      {
          magic[idx++] = ch;
          continue;       
      }
   
          for(i=0; i<c; i++)
          {
              if( (com_list[i].a == magic[idx-1] && com_list[i].b == ch )
                   ||
                  (com_list[i].b == magic[idx-1] && com_list[i].a == ch)
                  )         
              {
                  magic[idx-1] = com_list[i].x;
                  com_flag = true;
                  break;   
              }
          }       
          
          if(com_flag)
             continue;
          
       magic[idx++] = ch;    
       char p = 0;
       for(i=0; i<d; i++)
       {  
           p = 0;
           if(op_list[i].a == ch)
              p = op_list[i].b; 
           if(op_list[i].b == ch)
              p = op_list[i].a;
              
           if(p == 0)
              continue;
              
           for(k = 0; k < idx; k++)
           {
               if(magic[k] == p)
               {
                   idx = 0;
                   break;            
               }      
           }
           if(idx == 0)
              break;
       }
      
  }
  cout<<"[";
  for(i=0; i<idx; i++)
  {
      if(i!=0)
          cout<<", ";
      cout<<magic[i];
  }
  cout <<"]"<<endl;
}


