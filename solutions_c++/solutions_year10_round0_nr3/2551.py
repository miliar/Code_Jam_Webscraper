#include <fstream>
#include <string>
#include <iostream>
#include <list>

using namespace::std;

int main()
{
    int long long r,k,n;
    int long long aux;
    int long long aux1;
    int long long inicial;
    int long long div;
    int long long din;
    bool esta;
    int casos;
    int ite=1;
    list <int long long> estado;
    list <int long long> replica;
    list <int long long> estadoaux;
    
    list <int long long>::iterator it;
    list <int long long>::iterator it1;
    
    ifstream entrada("prueba3.txt");
    ofstream salida("soluc3.txt");
    
    entrada>>casos;
    
    while(casos--)
    {
       entrada>>r>>k>>n;
       din=0;
       aux1=0;
       inicial=0;
       esta=true;
       estado.clear();
       
       for(int i=0; i<n; i++)
       {
          entrada>>aux;
          estado.push_back(aux);
       }
       
       for(int i=0; i<r; i++)
       {
          aux1=0;
          
          while(aux1+estado.front()<=k && estado.size()>0)
          {
             aux1+=estado.front();
             aux=estado.front();          
             estadoaux.push_back(aux);
             estado.pop_front();
          }
                    
          din+=aux1;                  
          while(estadoaux.size())
          {
             estado.push_back(estadoaux.front());
             estadoaux.pop_front();
          }
          
          /*if(i==0)
          {
             replica = estado;
             inicial=din;
          }
             
          else 
          {
             it=estado.begin();
             it1=replica.begin();
             
             while(it!=estado.end())
             {
                if(*it != *it1)
                {
                   esta=false;
                   break;
                }
                //cout<<*it<<" ";
                it++;
                it1++;
             }
             
             if(esta && i>1)
             {
                 div = (r-2)/(i-1);                 
                 din+= din*div;
                 i+=(i-1)*(div-1);
             }
            
          }*/
          //cout<<endl;
       }
       
       salida<<"Case #"<<ite++<<": "<<din<<endl;
    }
    
    system("pause");
    
}
