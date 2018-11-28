#include<stdio.h>
#include <map>
#include<string>
using namespace std;
map<string,int> search_eng;

int main ()
{   int kasus,i,j,z,S,Q,ct,akhir;
    char str[105][105],Query[1005][2000],temp[20]; 
    fgets(temp,20,stdin);
    sscanf(temp,"%d",&kasus);
    for(z=0;z<kasus;z++)
    {   search_eng.clear();ct=0;akhir=0;
        fgets(temp,20,stdin);
        sscanf(temp,"%d",&S);
        for(i=0;i<S;i++)
        {  fgets(str[i],105,stdin); 
           search_eng[str[i]]=1;
        }
        fgets(temp,20,stdin);
        sscanf(temp,"%d",&Q);
        for(i=0;i<Q;i++)
        {  fgets(Query[i],2000,stdin); 
        }
        for(i=0;i<Q;i++)
        { if(search_eng[Query[i]]==1)
          {  search_eng[Query[i]]++;
             ct++;
          }
          if(ct==S)
          {  ct=0;
             akhir++;
             for (map<string, int>::iterator it = search_eng.begin(); it != search_eng.end(); it++)
             {  (*it).second=1;
             }
             i--;
          }
        }
        printf("Case #%d: %d\n",z+1,akhir);
    }
    return 0;
}
