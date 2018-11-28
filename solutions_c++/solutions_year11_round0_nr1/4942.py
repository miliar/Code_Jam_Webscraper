#include <cstdlib>
#include <iostream>

using namespace std;
      
int main(int argc, char *argv[])
{
    int i,j,t,n,o,b,diff,index, index_o, old, index_b;   static int a[100], result[100];    char r; int p;  
    cin>>t;
    for(i=0;i<t;i++) 
    {
     cin>>n; 
     o = b = 1; index = index_o = index_b = old = 0;
     for(j=0;j<n;j++) 
     {
      cin>>r>>p;
      if (r=='O')
      {
       diff=abs(p-o);
       index_o+=(diff+1);
       o=p;
       if (index_o<=old) index_o=old+1;
       old=index_o;
      }
      else
      {
       diff=abs(p-b);
       index_b+=(diff+1);
       b=p;
       if (index_b<=old) index_b=old+1;
       old=index_b;
      }     
     }
	 result[i]=(index_b>index_o?index_b:index_o);
    }
    for (i=0;i<t;i++) cout<<"\nCase #"<<i+1<<":"<<result[i];
    system("PAUSE");
    return EXIT_SUCCESS;
}
