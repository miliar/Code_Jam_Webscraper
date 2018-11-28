#include <stdlib.h>
#include <iostream>
#include<fstream>
#include <string>
#include <vector>

using namespace std;

int main(){

    int i = 0;
    int j = 0;
    int k=0;
    int l = 0;
    int sum=0;
    int numChars=0;
    string sumstring="";
    int m, p, q, r, t, u, v, w, x, y, z=0;
    int a, b, c, d, e=0;
	 char str[2000];
        fstream file_op("C-small.in",ios::in);
        
        ofstream fout("output.txt");
        
              file_op.getline(str,2000);
              
        string s = str;
        string num = "";
        int n =  atoi(s.c_str());
        
        for (i=0;i<n;i++){
            sum=0;
            file_op.getline(str, 2000);
            
            s=str;
            
            //cout << s;
            
            for (j=0;j<s.length();j++){
                
                if (s[j]==119){//w
                   
                   for (k=1;k<s.length()-j;k++){
                       
                       if (s[j+k]==101){//e
                          
                          for (l=1;l<s.length()-j-k;l++){
                              
                              if (s[j+k+l]==108){//l
                                 
                                 for (m=1;m<s.length()-j-k-l;m++){
                                     
                                     if (s[j+k+l+m]==99){//c
                                        
                                        for (p=1;p<s.length()-j-k-l-m;p++){
                                            
                                            if (s[j+k+l+m+p]==111){//o
                                               
                                               for (q=1;q<s.length()-j-k-l-m-p;q++){
                                                   
                                                   if (s[j+k+l+m+p+q]==109){//m
                                                      
                                                      for (r=1;r<s.length()-j-k-l-m-p-q;r++){
                                                          
                                                          if (s[j+k+l+m+p+q+r]==101){//e
                                                             
                                                             for (t=1;t<s.length()-j-k-l-m-p-q-r;t++){
                                                                 
                                                                 if (s[j+k+l+m+p+q+r+t]==32){//" "
                                                                    
                                                                    for (u=1;u<s.length()-j-k-l-m-p-q-r-t;u++){
                                                                        
                                                                        if (s[j+k+l+m+p+q+r+t+u]==116){//t
                                                                           
                                                                           for (v=1;v<s.length()-j-k-l-m-p-q-r-t-u;v++){
                                                                               
                                                                               if (s[j+k+l+m+p+q+r+t+u+v]==111){//0
                                                                                  
                                                                                  for (w=1;w<s.length()-j-k-l-m-p-q-r-t-u-v;w++){
                                                                                      
                                                                                      if (s[j+k+l+m+p+q+r+t+u+v+w]==32){//" "
                                                                                         
                                                                                         for (x=1;x<s.length()-j-k-l-m-p-q-r-t-u-v-w;x++){
                                                                                             
                                                                                             if (s[j+k+l+m+p+q+r+t+u+v+w+x]==99){//c
                                                                                                
                                                                                                for (y=1;y<s.length()-j-k-l-m-p-q-r-t-u-v-w-x;y++){
                                                                                                    
                                                                                                    if (s[j+k+l+m+p+q+r+t+u+v+w+x+y]==111){//0
                                                                                                       
                                                                                                       for (z=1;z<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y;z++){
                                                                                                           
                                                                                                           if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z]==100){//d
                                                                                                              
                                                                                                              for (a=1;a<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y-z;a++){
                                                                                                                  
                                                                                                                  if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z+a]==101){//e
                                                                                                                     
                                                                                                                     for (b=1;b<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y-z-a;b++){
                                                                                                                         
                                                                                                                         if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z+a+b]==32){//" "
                                                                                                                            
                                                                                                                            for (c=1;c<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y-z-a-b;c++){
                                                                                                                                
                                                                                                                                if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z+a+b+c]==106){//j
                                                                                                                                   
                                                                                                                                   for (d=1;d<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y-z-a-b-c;d++){
                                                                                                                                       
                                                                                                                                       if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z+a+b+c+d]==97){//a
                                                                                                                                          
                                                                                                                                          for (e=1;e<s.length()-j-k-l-m-p-q-r-t-u-v-w-x-y-z-a-b-c-d;e++){
                                                                                                                                              
                                                                                                                                              if (s[j+k+l+m+p+q+r+t+u+v+w+x+y+z+a+b+c+d+e]==109){//m
                                                                                                                                                 
                                                                                                                                                 sum++;
                                                                                                                                                 
                                                                                                                                              }
                                                                                                                                                  
                                                                                                                                          }
                                                                                                                                          
                                                                                                                                       }
                                                                                                                                           
                                                                                                                                   }
                                                                                                                                   
                                                                                                                                }
                                                                                                                                    
                                                                                                                            }
                                                                                                                            
                                                                                                                         }
                                                                                                                             
                                                                                                                     }
                                                                                                                     
                                                                                                                  }
                                                                                                                      
                                                                                                              }
                                                                                                              
                                                                                                           }
                                                                                                               
                                                                                                       }
                                                                                                       
                                                                                                    }
                                                                                                        
                                                                                                }
                                                                                                
                                                                                             }
                                                                                                 
                                                                                         }
                                                                                         
                                                                                      }
                                                                                          
                                                                                  }
                                                                                  
                                                                               }
                                                                                   
                                                                           }
                                                                           
                                                                        }
                                                                            
                                                                    }
                                                                    
                                                                 }
                                                                     
                                                             }
                                                             
                                                          }
                                                              
                                                      }
                                                      
                                                   }
                                                       
                                               }
                                               
                                            }
                                                
                                        }
                                                            
                                     }
                                         
                                 }
                                                    
                              }
                                  
                          }
                          
                                             
                       }
                           
                   }
                                  
                }
                    
            }
            
            
            sum= ( sum%10000);
            
            numChars=1;
            if (sum/1000>=1){
                            numChars=4;
                            }else if (sum/100>=1){
                                  numChars=3;
                                  }else if (sum/10>=1){
                                        numChars=2;
                                        }
            
            
            
            
            fout << "Case #" << i+1 << ": " ;
            for (j=0;j<(4-numChars);j++){
                fout << "0";    
            }
            fout << sum << endl;
            
                
        }
        
        
        fout << flush;
        fout.close();
        
        file_op.close();

        system("PAUSE");

	return 0;

}
