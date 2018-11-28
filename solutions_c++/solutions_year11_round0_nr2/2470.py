#include <iostream>
#include <cmath>
#include <math.h>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

string reverse(string s){
       string s1 = "";
       for (int i = s.length()-1; i>=0; i--){
               s1.push_back(s[i]);
       }
       return s1;
       }

int main(){
    ifstream myf;
    myf.open("input2.txt");
    
    int T;
    myf>>T;
    
    ofstream myfile;
    myfile.open("result2.txt");
    
    for (int it = 0; it < T; it++){
        int C;
        myf>>C;
        //cout<<C;
        map<string,int> comb1;
        map<string,char> comb2;
        
        for (int i = 0; i < C; i++){
            string s;
            myf>>s;
            string s1 = s.substr(0,2);
            comb1[s1]=1;
            comb2[s1]=s[2];
            string s2 = reverse(s1);
            comb1[s2]=1;
            comb2[s2]=s[2];
            
            
            //cout<<it+1<<" "<<s<<endl;
            //cout<<it+1<<" "<<s2<<" "<<s[2]<<endl;
        }
        
        int d;
        myf>>d;
        //cout<<d<<endl;
        map<string,int> op;
        
        for (int i = 0; i < d; i++){
            string s;
            myf>>s;
            op[s]=1;
            op[reverse(s)]=1;
        }
        
        vector<char> res;
        int rn = -1;
        
        int n;
        myf>>n;
        
        
        for (int i = 0; i < n; i++){
            char c;
            myf>>c;
            string s1="",s2="";
            int chk = 0;
            
            if (rn > -1){
            s1.push_back(res[rn]);
            s1.push_back(c);
            
            
            
            if (comb1[s1]) {res[rn] = comb2[s1]; continue;}
            
            
            
            for (int j = 0; j <= rn; j++){
                s1="";
                
                s1.push_back(res[j]);
                s1.push_back(c);
            
                
                if (op[s1] ) {res.clear(); rn = -1;
                chk = 1;
                break;
                }
                
                    
            }
            
            if (chk == 0){res.push_back(c); rn++;}
            
            }
            
            else {res.push_back(c); rn++;}  
        }
        //cout<<it+1<<" "<<rn<<endl;
        
        myfile<<"Case #"<<it+1<<": [";
        for(int i = 0; i <= rn; i++){
                myfile<<res[i];
                if (i < rn) myfile<<", ";
        }
    
        myfile<<"]"<<endl;
        
        cout<<endl<<endl<<endl;
    }
    
    myfile.close();
    myf.close();
    return 0;    
}
