#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

ifstream fin("c:\\A-large.in");
ofstream fout("c:\\Download A-large.out");

/*
bool estaEn(string s,char c) {
     
     
     for(int i=0;i<s.size();i++) {
             
             if(c==s[i]) return true;
             
     }

     return false;
     
}
*/


vector<string> separar(string s) {
      
      vector<string>ret;
      
      string t;
      bool p=false;

      for(int i=0;i<s.size();i++) {
      
      
              if(s[i]=='(') p=true;
              if(s[i]==')') p=false;
              
              if(p && s[i]!='('  && s[i]!=')' ) t+=s[i]; 
 
              
              if(!p && s[i]!='('){
                                  if(s[i]!=')') t+=s[i];
                                  ret.push_back(t);
                                  t="";
              }
              
  
      }       
               

      return ret;
               
}




bool contar (string texto, string palabra) {
    
    
    vector<string> separadas=separar(texto);
    
    for(int i=0;i<palabra.size();i++) {
            
            if(separadas[i].find_first_of(palabra[i])==-1) return false;
    
    }
    
    
    return true;
}


int main (){

	int L;
	int D;
	int N;
    
    vector<string> palabras;
    vector<string> text;

	fin >> L;
	fin >> D;
	fin >> N;

    	
    for(int i=0;i<D;i++) {
            
            string temp;
            fin>>temp;
            palabras.push_back(temp);        
    }
    

    
    for(int i=0;i<N;i++){	
	
	        string temp;
            fin>>temp;
            text.push_back(temp);   
	
    }
    
    

    vector<int> ret;
    
    for(int i=0;i<text.size();i++) {

            int c = 0;
            
            for(int j=0;j<palabras.size();j++) {
                    
                    c = c + contar(text[i],palabras[j]);
                    
            }        
 
            fout << "Case #" <<i+1<<": "<<c;
            if (i+1<text.size()) fout << endl;  
            
            //ret.push_back(c);           
    }
 /*   

    for(int i=0;i<ret.size();i++) { 
            fout << "Case #" <<i+1<<": "<<ret[i];
            if (i+1<ret.size()) fout << endl;        
    }
*/
    system("pause");

}
