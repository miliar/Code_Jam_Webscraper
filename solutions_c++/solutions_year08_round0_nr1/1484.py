#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <valarray>
#include <bitset>
#include <iostream>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()

 int esta(vector <string> v,string cad)
 {
	for(int i=0;i<v.size();i++)
	{
		if(cad==v[i])
			return 1;
	}
 return 0;
 }

void elimina(vector <string> &guarda, string cad)
{
 for(int i=0;i<guarda.size();i++)
 {
         if(guarda[i]==cad) 
         {
         guarda.erase(guarda.begin() + i);                 
         break;                   
         }       
         
         
 }   
}

 void metelo(vector <string> &aux,vector <string> v,string cad)
 {
	if(esta(v,cad))
	{
		if(!esta(aux,cad))
			aux.push_back(cad);
	
	}
 
 
 }
      

int main()
{
    
    int casos,con=1;
    cin>>casos;
    while(casos)
    {
       int s,q;
       string busca;
       vector < string > buscador,aux;
       cin>>s;
	   getline(cin,busca);
       while(s)
       {
       getline(cin,busca);
       buscador.push_back(busca);
       s--;
       }  
	sort(all(buscador));
       cin>>q;
	    
       int cambios=0;
       
      /* string cadena;
       getline(cin,cadena);
       while(q)
       {       getline(cin,cadena);
               
               elimina(aux,cadena);  
        if(aux.size()==0)
        {
         cambios++;
         aux=buscador;  
         elimina(aux,cadena);                                  
        }           
        q--;             
		}                
        */
	 
	   string cadena;
       getline(cin,cadena);
	   while(q)
	   {
	   getline(cin,cadena);
	   metelo(aux,buscador,cadena);
	   sort(all(aux));
	   if(aux==buscador)
	   {
	   cambios++;
	   aux.clear();
	   aux.push_back(cadena);
	   }
	   q--;
	   }

      cout<<"Case #"<<con<<": "<<cambios<<endl;
	  con++;
     casos--;           
    }

    return 0;
    }
