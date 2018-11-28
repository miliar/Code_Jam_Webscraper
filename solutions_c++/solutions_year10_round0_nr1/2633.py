#include <fstream>
#include <string>
#include <iostream>
#include <cmath>
using namespace::std;

string suma(string, string);

int main()
{
    int long long k;    
    int n;
    int long long red;
    int casos;
    int cont=1;
       
    ifstream entrada("prueba.txt");
    ofstream salida("soluc.txt");
   
    entrada>>casos;
        
    while(casos--)
    {
       entrada>>n>>k;     
       
       string elem(n,'0');
       string comp(n,'1');
       
       red = pow(2.0,(double)n);
       
       k = k%red; 
       k = red-k;
       
       if(k==1) 
          salida<<"Case #"<<cont<<": ON"<<endl;
       else
          salida<<"Case #"<<cont<<": OFF"<<endl;        
       
       /*for(int i=0; i<k; i++)
          elem = suma(elem,"1");
        
       if(elem==comp)
          salida<<"Case #"<<cont<<": ON"<<endl;
       else
          salida<<"Case #"<<cont<<": OFF"<<endl;*/
         
        cont++;               
    }
    
    entrada.close();
    salida.close();
    
}

string suma(string a, string b)
{
    int l = 1 + (a.length() > b.length() ? a.length() : b.length());
    int longitud = a.length();
    string c(l, '0');
    
    a = string(l - a.length(), '0') + a;
    b = string(l - b.length(), '0') + b;
    
    int ac = 0, sum = 0;
    
    for (int i=l-1; i>=0; i--)
    {
        sum = a[i] + b[i] - '0' - '0' + ac;
        c[i] = (sum % 2) + '0';
        ac = sum / 2;
    }
    
    if(longitud<c.length())
       c.erase( c.begin());
    return c;
}
