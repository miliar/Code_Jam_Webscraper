#include <iostream>
#define MAX 109
using namespace std;

main()
{
      bool byl[110], ok;
      char nazwa[110][110], pyt[110];
      int n, a, b, ile, dl[110], len, res;
      scanf("%d",&n);
      for(int i=0;i<n;i++)
      {
              res=0;
              scanf("%d\n",&a);        
              for(int j=0;j<a;j++)
              {
                      cin.getline(nazwa[j], MAX);         
                      byl[j]=0;
                      dl[j]=strlen(nazwa[j]);
              }
              scanf("%d\n",&b);
              ile=0;
              for(int j=0;j<b;j++)
              {
                      cin.getline(pyt, MAX);
                      len=strlen(pyt);        
                      for(int x=0;x<a;x++)
                      {
                              if(len==dl[x]) ok=1;
                              else continue;
                              for(int y=0;y<len;y++)
                              {
                                      if(pyt[y]!=nazwa[x][y]) 
                                      { 
                                        ok=0; 
                                        break;
                                      }        
                              }
                              if(ok)
                              {
                                    if(!byl[x])
                                    {
                                        byl[x]=1;
                                        ile++;                
                                    }
                                    if(ile==a)
                                    {
                                              ile=1;
                                              for(int y=0;y<a;y++) byl[y]=0;
                                              byl[x]=1;
                                              res++;          
                                    }
                                    break;
                              }
                      }
              }
              printf("Case #%d: %d\n",i+1,res);
      }
      return 0;      
}
