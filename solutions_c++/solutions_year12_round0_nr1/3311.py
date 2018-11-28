#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

void fun_1(const int & z, const string & napis,ostream & wyj)
{
 wyj<<"Case #"<<z<<": ";
 
 for(int i=0;i<napis.size();i++)
 {
         if(napis[i] == ' ')
        wyj<<' ';
         
         if(napis[i] == 'a')
         wyj<<'y';
         
         if(napis[i] == 'b')
         wyj<<'h';
         
          if(napis[i] == 'z')
         wyj<<'q';
         
        
         
          if(napis[i] == 'c')
         wyj<<'e';
         
         if(napis[i] == 'd')
         wyj<<'s';
         
          if(napis[i] == 'e')
         wyj<<'o';
         
         if(napis[i] == 'o')
         wyj<<'k';
        
         
          if(napis[i] == 'f')
         wyj<<'c';
         
          if(napis[i] == 'g')
         wyj<<'v';
         
           if(napis[i] == 'h')
         wyj<<'x';
         
         if(napis[i] == 'i')
         wyj<<'d';
         
         if(napis[i] == 'j')
         wyj<<'u';
         
          if(napis[i] == 'm')
         wyj<<'l';
         
            if(napis[i] == 'l')
         wyj<<'g';
         
          if(napis[i] == 'n')
         wyj<<'b';
         
          
         
             if(napis[i] == 'p')
         wyj<<'r';
         
           if(napis[i] == 'q')
         wyj<<'z';
         
           if(napis[i] == 'r')
         wyj<<'t';
         
           if(napis[i] == 's')
         wyj<<'n';
         
           if(napis[i] == 't')
         wyj<<'w';
         
          
           if(napis[i] == 'u')
         wyj<<'j';
         
           if(napis[i] == 'v')
         wyj<<'p';
         
            if(napis[i] == 'w')
         wyj<<'f';
         
          if(napis[i] == 'x')
         wyj<<'m';
         
          if(napis[i] == 'y')
         wyj<<'a';
         
         if(napis[i] == 'k')
         wyj<<'i';
         
        
 }    
     
     
}

void wczytaj()
{
     int N;
     ofstream wyjscie("Problem A. Speaking in Tongues.out");
     ifstream plik("Problem A. Speaking in Tongues.in");
     
     if(plik.good())
     {
                
               plik>>N;
           
               
               string test;
               getline(plik,test);  
              
               
               for(int i=0;i<N;++i)
               {
                       string temp;
                       getline(plik,temp);
                       fun_1(i+1,temp,wyjscie);
                       wyjscie<<endl;
                     
                   
               }
               
     }     
     
     
     
     
     
     
     

}

int main()
{
    
    
    
    wczytaj();
    
    

return 0;
}
