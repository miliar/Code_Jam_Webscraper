#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int nT;
string s, kq;

ifstream fi("in.txt");
ofstream fo("out.txt");
     


int main(int argc, char *argv[])
{
    fi >>nT;
    char ss[200];
    fi.getline(ss,200);
    for (int i = 1; i<=nT; i++){
        fi >> s;
        fi.getline(ss,200);
        kq = "";

        cout <<s;        
        int ls = s.size();

        
        bool ch = true;
        int d = 0;
        for (int j = ls-2; j>=0; j--){
            if (s[j] <  s[j+1]){
                ch = false;
                d = j;
                break;
            }
        }
        
        cout <<" d" <<d <<" ch" <<ch; 
        if (! ch){

            for (int j = 0; j<d; j++){
                kq += s[j];
            }
            
            cout <<" kq" <<kq;       
            
            
            //tim so thay the
            int k = ls-1;
            while (s[k] <= s[d]) 
                k--;
            
            //swap k d
            {   
                char tmp = s[k];
                s[k] = s[d];
                s[d] = tmp;
            } 
            kq += s[d];
            
            //swap chuoi
            for (int j = ls-1; j>d; j--){
                kq += s[j];
            }
        }  
        else {
            kq = "0";
            int j = ls-1;
            while (s[j] == '0'){
                kq += s[j];
                j--;
            }
            kq = s[j] + kq;
            j--;
            while (j>=0){
                kq+=s[j];
                j--;
            }
        }
        
        fo <<"Case #" <<i<<": " <<kq <<endl;
        cout <<"Case #" <<i<<": " <<kq <<endl;
    }
    
    fi.close();
    fo.close();     
    system("PAUSE");
    return EXIT_SUCCESS;
}
