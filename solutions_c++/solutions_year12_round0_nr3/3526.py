#include<iostream>
#include<fstream>
using namespace std;

bool fun(int a_, int b_)
{
//-------------------------------------------
string tmp_3; // brzydkie rozwi¹zanie
itoa(a_, (char*)tmp_3.c_str(), 10);
string a = tmp_3.c_str();

itoa(b_, (char*)tmp_3.c_str(), 10);
string b = tmp_3.c_str();
//-------------------------------------------

int z = 0;
while( z != a.size()-1)
{
    char pom = a[a.size()-1];
   // cout<<pom;
    
    for(int i=a.size()-1;i>0;i--)
    {
            a[i] = a[i-1];
    }
    
    a[0] = pom;
  //  cout<<endl<<a;
   
   if(a == b)
   return true;
   
  
z++; 
}          
return false;
}

void fun_2(int i,int A,int B,ifstream & wejscie,ofstream & wyjscie)
{
  int licznik = 0;   
while(A<B)
{
           for(int i=A;i<B;i++)
           {
           if(fun(A,i+1))
           licznik++;
           }
           
A++;           
}     
               
  wyjscie<<"Case #"<<i+1<<": "<<licznik<<endl;   
     
}
void wczytaj()
{
     ifstream wejscie("Problem C. Recycled Numbers.in");
     ofstream wyjscie("Problem C. Recycled Numbers.out");
     int N;
     wejscie>>N;
   
     
     if(wejscie.good())
     {
     for(int i=0;i<N;++i)
     {       int A,B; 
     wejscie>>A>>B;
     
     fun_2(i,A,B, wejscie,wyjscie);
     
     
     }
     }
     
}


int main()
{
    
    wczytaj();
// fun(12345,34512);   
    
    
    
getchar();
cin.ignore();
return 0;
}
