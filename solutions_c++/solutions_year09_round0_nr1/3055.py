#include <cstdlib>
#include <iostream>
#include <set>
#include <String>
#include <vector>


using namespace std;

int main(int argc, char *argv[])
{
    
    int l,d,n;
    cin >> l ; //largo palabras;
    cin >> d; //numero de palabras
    cin >> n; // casos de prueba
    vector< set<char> > bolsag;
    
        
    string dic[6000];
    string men[501];
    
    //cout << "---diccionario" << endl;
    for(int i = 0; i < d; i++ ){
            cin >> dic[i];
            //cout << endl;        
            
    }
    
    //cout << "---mensajes" << endl;
    
    for (int i = 0; i < n; i++){
            cin >> men[i];
            //cout << endl;
    }
    
    set<char> tmp;


    
    for(int i = 0 ; i < n; i++){
                bool ab = false;
                int count = 0;
                bool bol;
                bolsag.clear();
            for (int j = 0 ;  j < men[i].size() ; j++){
                if( men[i][j] == '(' ){
                    ab = true;
                    //cout << men[i][j] << "   ";
                    tmp.clear();             
                } 
                else if (men[i][j] == ')'){
                     //cout << men[i][j] << "   ";
                     ab =false;
                     bolsag.push_back(tmp); 
                     tmp.clear();
                              
                }
                else{
                     //cout << men[i][j] << "   ";
                     if(ab){
                            tmp.insert(men[i][j]);
                     }
                     else{
                          tmp.clear();
                          tmp.insert(men[i][j]);
                          
                          bolsag.push_back(tmp);  
                          tmp.clear();        
                     }
                     
                }
           
            } 
            
            for(int i1 = 0 ; i1 < d; i1++){
            bol = true;
                for (int j = 0 ;  j < dic[i1].size() ; j++){
                    if ( !bolsag[j].count(dic[i1][j])){
                    bol = false; 
                    break;
                    }
                }
                if(bol) {
                count++;
                        //cout << dic[i1] << endl;
                } 
                   
            }
    
            cout << "Case #"<< i+1  << ": "<<  count << endl;
    
            
                                    
    }
    

  /*  
 
    
    */
    
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
