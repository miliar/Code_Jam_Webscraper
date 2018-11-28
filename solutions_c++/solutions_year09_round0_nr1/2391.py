#include<cstdio>
#include<iostream>
#include<fstream>
#include<cstdlib>
#include<string>
#include<vector>
#include<iterator>



using namespace std;

 vector<string> getTokens(string s);
 bool matchWords(string word,vector<string> pattern);
 bool contains(string s, char c);

int main(){

    ifstream cin("alien_language.in");
  ofstream cout("alien_language.out");
    
    vector<string> words,  pattern;
    
    
    int L,D,N,i,j,c;
    string aux;
    
 
        
        cin>>L>>D>>N;
        
     
        
        for(i=0;i<D;i++)//getting vocabulary
        {
            cin>>aux;
            words.push_back(aux);
        }
       
        
       
        for(i=0;i<N;i++){//getting test cases
            cin>>aux;
            
            pattern=getTokens(aux);
             //copy(pattern.begin(), pattern.end(), ostream_iterator<string>(cout, "\n"));
             //cout<<"\n";
            c=0;
            for(j=0;j<D;j++)//matching testCase posibilities in vocabulary
               if(matchWords(words[j],pattern))
                c++;
                
            
            cout<<"Case #"<<i+1<<": "<<c<<endl;
                    
          
        }
      
           
 

system("pause"); return 0;   

}

bool matchWords(string word,vector<string> pattern){
    int c=0;
        if(word.size()!=pattern.size())
            return false;
            
        for(int i=0;i<word.size();i++){
            //cout<<" look for "<<word[i]<<" in "<<pattern[i]<<": "<<contains(pattern[i],word[i])<<endl;
            if(contains(pattern[i],word[i]))
                c++;
      }
      
    //cout<<endl;
                
    return c==word.size();
                
        
    
}

bool contains(string s, char c){
    
    for(int i=0;i<s.size();i++)
        if(s[i]==c)
            return true;
    
    return false;
}

 vector<string> getTokens(string s){
      
      vector<string> res;
      int closePos;
      
      for(int i=0;i<s.size();i++)
      {
           if(s[i]=='('){
                    closePos=s.find(')',i+1);
                  
                    res.push_back( s.substr(i+1,closePos-i-1)); 
                    
                    i=closePos;
                  continue;
            }
          
           
            res.push_back(*(new string()));
            
            res.back().push_back(s[i]);
     }
     
     return res;
        
}
