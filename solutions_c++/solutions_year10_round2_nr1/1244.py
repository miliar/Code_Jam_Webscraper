#include <stdio.h>
#include <iostream>
#include <string>

#include <set>

using namespace std;

int main(void)
{
   int T, prontas, criar, z, custo;
   string linha;

   set<string> diretorios;

   scanf("%d", &T);
   for (int i = 0 ; i < T ; i ++ ) 
   {
      diretorios.clear();
      custo = 0;
      scanf("%d %d", &prontas, &criar);
      for ( int j = 0; j < prontas ; j ++ )
      {
         linha.clear();
         cin>>linha;
         for ( z = 1 ; z <= linha.length() ; z++ )
         {
            if ( linha[z] == '/' || linha[z] == 0 )
            {
               string tmp = linha.substr(0,z);
               if ( diretorios.find(tmp) == diretorios.end() )
               {
                  diretorios.insert(tmp );
               }
            }
         }
      }
      for ( int j = 0 ; j < criar ; j ++ )
      {
         linha.clear();
         cin>>linha;
         for ( z = 1 ; z <= linha.length() ; z++ )
         {
            if ( linha[z] == '/' || linha[z] == 0 )
            {
               string tmp = linha.substr(0,z);
               if ( diretorios.find(tmp) == diretorios.end() )
               {
                  diretorios.insert(tmp );
                  custo++;
               }
            }
         }

      }
      cout<<"Case #"<<i+1<<": "<<custo<<endl;
   }
   return 0;
}
