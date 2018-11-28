#include <stdlib.h>
#include <iostream>
#include<fstream>
#include <string>
#include <vector>

using namespace std;

int main(){

    int i = 0;
    int j = 0;
    vector<string> words;
    vector<string> testCases;
    vector<string> fixChars;
	 char str[2000];
        fstream file_op("A-large.in",ios::in);
      
              file_op.getline(str,2000);
        
        string s = str;
        string num = "";
        int l, d, n;
        bool lSet=false;
        
        for (i=0;i<s.length();i++){
            
            if (s[i]==32){
               if (lSet){
                  d = atoi(num.c_str());
                  num="";
               }else{
                     l = atoi(num.c_str());
                     num="";
                     lSet=true;      
               }
            }else{
                
               num += s[i]; 
               } 
        }
        
        n = atoi(num.c_str());
        num="";
        
        for (i=0;i<l;i++){
            
            fixChars.push_back("");
            
        }
        
        for (i=0;i<d;i++){
            
              file_op.getline(str,2000);
              
              words.push_back(str);
        }
        
        bool recording=false;
        int onWhichChar = 0;
        int k = 0;
        int m=0;
        int p=0;
        int q=0;
        bool matching=true;
        int matches=0;
        
        
        ofstream fout("output.txt");
        
       for (i=0;i<n;i++){
           
           for (q=0;q<l;q++){
            
                fixChars[q]="";
            
            }
            
            matches=0;
            k=0;
            onWhichChar=1;
            file_op.getline(str, 2000);
              testCases.push_back(str);
              
              num=str;
              
              for (j=0;j<num.length();j++){
                  
                  if (num[j]==40){
                     
                     recording=true;
                                      
                  }
                  
                  if (!recording){
                     
                     fixChars[onWhichChar-1]+=num[j];
                                     
                  }
                  
                  if (num[j]==41){
                     
                     recording=false;
                                     
                  }
                  
                  if (recording){
                     
                     if (num[j]!=40){
                         fixChars[onWhichChar-1]+=num[j];
                     }
                                    
                  }else{
                     
                     onWhichChar++;  
                   }
              }
              
              for (j=0;j<d;j++){
                  
                  for (m=0;m<l;m++){
                      matching=false;
                      for (p=0;p<fixChars[m].length();p++){
                          
                          if (fixChars[m].at(p) == words[j].at(m)){
                             
                             matching=true;
                             break;
                                                   
                          }
                              
                      }
                      if (!matching){
                         
                         break;
                                        
                      }
                      if (matching && m==(l-1)){
                         
                         matches++;
                                      
                      }
                          
                  }
                      
              }
              
              fout << "Case #" << i+1 << ": " << matches << endl;
              
              
                
        }
        fout << flush;
        fout.close();
 
        file_op.close();

	return 0;

}
