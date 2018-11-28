#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;



int main()
{
    
    char arr[26]  ;
    
   for(int k=0;k<26;k++)
      arr[k] = k+97;
      
  char arr2[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
  
    
    int cases=0;
    ifstream in;
    in.open("A-small-attempt2.in");
    
    string s;
    getline(in,s,'\n');
    
    cases = atoi(s.c_str());
    
    
    
  ofstream out;
  out.open("output.txt");
   
  int t=1;
  
      
  while(!in.eof()&& t<=cases)
    {
                  
    getline(in,s,'\n');
    cout<< s<<endl;
  
   out<<"Case #"<<t<<": ";
  int i=0;
  
   while(s[i]!='\0') 
    {
     
                   
    if (s[i] == 32)
       out<<s[i];
        
    else
    { 
    
     for( int j=0; j < 26 ; j++ ){
   
         if(s[i] == arr2[j])
          {out<<arr[j];}
     }    
   
    }
    i++; 
  }// end of while   
    out<<endl;
    
  
    t++;
    
   }//end of file               
  
    in.close();
    out.close();
    system("pause");
    
    return 0;
}

