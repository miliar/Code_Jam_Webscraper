#include <iostream>
#include<string>
using namespace std;

int main()
{
   int t;
  cin>>t;
  int c=1;
  
 
 hi:
  while(t-->0)
  {
  int point=0;
    string a[4];
    int p=-1;
    for(int i=0;i<4;i++)
    
  {
  cin>>a[i];
 p=a[i].find('.');
   if(p!=4&&p!=-1)
   point=1;
  }
    
    
    
  int digX=0;
    int digO=0;
    int digx=0;
    int digo=0;
    for(int k=0;k<4;k++)
  {
  if(a[k].at(k)=='X'||a[k].at(k)=='T')
    digX++;
   
     if(a[k].at(k)=='O'||a[k].at(k)=='T')
   digO++;
  
     if(a[k].at(4-k-1)=='O'||a[k].at(4-k-1)=='T')
   digo++;
    
     if(a[k].at(4-k-1)=='X'||a[k].at(4-k-1)=='T')
   digx++;
     }
  
    if(digX==4||digx==4)
    {cout<<"Case #"<<c<<": X won"<<endl;
   c++;
     goto hi;
    }else
      if(digO==4||digo==4)
    {cout<<"Case #"<<c<<": O won"<<endl;
    c++;
     goto hi;
    } 
      
    for(int z=0;z<4;z++)
      {
      int rowX=0;
    int rowO=0;
    int rowx=0;
    int rowo=0;
      for(int z1=0;z1<4;z1++)
    {
   if(a[z].at(z1)=='X'||a[z].at(z1)=='T')
    rowX++;
   
     if(a[z].at(z1)=='O'||a[z].at(z1)=='T')
   rowO++;
      if(a[z1].at(z)=='X'||a[z1].at(z)=='T')
    rowx++;
   
     if(a[z1].at(z)=='O'||a[z1].at(z)=='T')
   rowo++;
    
      }
       
       if(rowX==4||rowx==4)
    {cout<<"Case #"<<c<<": X won"<<endl;
    c++;
     goto hi;
    }else
      if(rowO==4||rowo==4)
    {cout<<"Case #"<<c<<": O won"<<endl;
     c++;
     goto hi;}
    }
    
    
    if(point==1)
      cout<<"Case #"<<c<<": Game has not completed"<<endl;
    else
      if(point==0)
      cout<<"Case #"<<c<<": Draw"<<endl;
      
    c++;
  
  }
   return 0;
}
   