#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main(){
    
    int T;
    int i;
    int h;

    string cadena;
    
    cin >> T;    
    
    for(i=0;i<=T;i++){
        h=0;                     
        
        getline(cin,cadena);
    

        
        while(cadena[h]!= '\0'){
                          
           if(cadena[h]=='a'){
               cadena[h]= 'y';
               }else{
               
               if(cadena[h]=='b'){
                   cadena[h]= 'h';
               }  else{
                      if(cadena[h]=='c'){
                          cadena[h]= 'e';
                      }else{
                         if(cadena[h]=='d'){
                           cadena[h]= 's';
                         }else{
                             if(cadena[h]=='e'){
                                   cadena[h]= 'o';
                              }else{
                                    if(cadena[h]=='f'){
                                         cadena[h]= 'c';
                                    }else{
                                          if(cadena[h]=='g'){
                                               cadena[h]= 'v';
                                          }else{
                                                  if(cadena[h]=='h'){
                                                     cadena[h]= 'x';
                                                  }else{
                                                     if(cadena[h]=='i'){
                                                        cadena[h]= 'd';
                                                     }else{
                                                          if(cadena[h]=='j'){
                                                               cadena[h]= 'u';
                                                          }else{                                                                
                                                               if(cadena[h]=='k'){
                                                                   cadena[h]= 'i';
                                                                }else{
                                                                      if(cadena[h]=='l'){
                                                                         cadena[h]= 'g';
                                                                       }else{                                                                                     
                                                                           if(cadena[h]=='m'){
                                                                              cadena[h]= 'l';
                                                                           }else{
                                                                                if(cadena[h]=='n'){
                                                                                   cadena[h]= 'b';
                                                                                 }else{
                                                                                     if(cadena[h]=='o'){
                                                                                         cadena[h]= 'k';
                                                                                     }else{
                                                                                         if(cadena[h]=='p'){
                                                                                           cadena[h]= 'r';
                                                                                         }else{
                                                                                                if(cadena[h]=='q'){           
                                                                                                     cadena[h]= 'z';
                                                                                                }else{
                                                                                                         if(cadena[h]=='r'){
                                                                                                            cadena[h]= 't';
                                                                                                         }else{                                                                                                              
                                                                                                               if(cadena[h]=='s'){           
                                                                                                                 cadena[h]= 'n';
                                                                                                                }else{                                                                                                                        
                                                                                                                     if(cadena[h]=='t'){
                                                                                                                         cadena[h]= 'w';
                                                                                                                     }else{                                                                                                                           
                                                                                                                          if(cadena[h]=='u'){
                                                                                                                            cadena[h]= 'j';
                                                                                                                          }else{                                                                                                                                         
                                                                                                                                if(cadena[h]=='v'){
                                                                                                                                    cadena[h]= 'p';
                                                                                                                                }else{
                                                                                                                                    if(cadena[h]=='w'){
                                                                                                                                         cadena[h]= 'f';
                                                                                                                                    }else{
                                                                                                                                         if(cadena[h]=='x'){
                                                                                                                                             cadena[h]= 'm';
                                                                                                                                         }else{                                                                                                                                                         
                                                                                                                                             if(cadena[h]=='y'){
                                                                                                                                                  cadena[h]= 'a';
                                                                                                                                             }else{
                                                                                                                                                    if(cadena[h]=='z'){
                                                                                                                                                       cadena[h]= 'q';
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
           
               
           h++;                  
        }
        if(i>0){
        cout << "Case #" << i << ": " << cadena;
        cout << endl;
        }
    }
    return 0;    
}
