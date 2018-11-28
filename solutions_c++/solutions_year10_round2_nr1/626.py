#include <iostream>
#include <sstream>
#include <set>
#include <string>


using namespace std;
/*
struct carpeta
{
  string nom;
  vector<carpeta> cDentro;
  
  carpeta(String nom)
  {
       
       
  }
  
  carpeta()
  {}
       
};
*/

set<string> directorio;
int cont=0;
void analiza(string p)
{
     string aux="";
        
     for(int a=0;a<p.length(); a++)
     {
             
             if((p[a]=='/' || a==(p.length()-1)) && (a!=0))
             {
                    //string sub=aux.substr(0,aux.length()-1);
                    if(a==(p.length()-1)) aux+=p[a];
                    //cout<<" aux   "<<aux<<endl;
                    directorio.insert(aux);           
             }
             aux+=p[a];
                
     }
}

void analiza2(string p)
{
     string aux="";
        
     for(int a=0;a<p.length(); a++)
     {
             
             
             if((p[a]=='/' || a==(p.length()-1)) && (a!=0)) 
             {
                    if(a==(p.length()-1))
                    aux+=p[a];
                    
                    if(directorio.count(aux)==1 ) 
                    {
                        //cout<< aux<<"  ya esta"<<endl;
                        
                    }
                    else 
                    {
                         //string sub=aux.substr(0,aux.length()-1);
                         //cout<<"  aux  "<<aux<<endl;
                         directorio.insert(aux); 
                               cont++;}           
             }
             aux+=p[a];   
             
     }
}


int main()
{
    int t,n,m;
    string buffer;
    getline(cin,buffer);
    istringstream is(buffer);
    is>>t;
    string buf;
    for(int i=1; i<=t; i++)
    {
                getline(cin,buf);
                istringstream iss(buf);
                iss>>n>>m;
                //cout<<" n "<<n<<"  m  "<<m<<endl;
                //leo conocidos
                directorio= set<string>();
                cont=0;
                for(int j=0; j<n; j++)
                {
                        getline(cin,buffer);        
                        analiza(buffer);
                }
                for(int j=0; j<m; j++)
                {
                        getline(cin,buffer);
                        analiza2(buffer);     
                }
                cout<<"Case #"<<i<<": "<<cont<<endl;
    }
    
    return 0;    
}
