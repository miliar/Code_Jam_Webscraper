#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>

using namespace std;

int getInt(string,int);
string getStrFromInt(int n);
bool checkPair(int,int);

class MyStr{
public:
    MyStr(string s){
        str = s;
    }
    
    string next(int n){
        string ret;
        for(int i = 0 ; i < str.length() ; i++){
            ret += str[(n+i) % (str.length())];
        }
        return ret;
    }
private:
    string str;
};


string getStrFromInt(int n){
    string temp;
    
    while(n){
        temp += ((n%10) + '0');
        n /= 10;
    }
    
    string res;
    for(int i = temp.length()-1 ; i >= 0 ; i--){
        res += temp[i];
    }
    return res;
}

int getInt(string s, int f){
    string temp;
    
    for(int i = 0 ; i < s.length() ; i++){
        temp += s[(f+i) % (s.length()-1)];
    }
 
    return atoi(temp.c_str());
}

bool checkPair(int a, int b){
    string A = getStrFromInt(a);
    string B = getStrFromInt(b);
    
    if(A.length() != B.length()){
        return false;
    }else{
        for(int i = 1 ; i < A.length() ; i++){
            MyStr m(A);     
            if(m.next(i) == B && m.next(i) != A)
                return true;
        }
    }
    return false;
}

int main(int argc, char** argv){
    ifstream inFile(argv[1]);
    ofstream outFile(argv[2]);
    
    int line;
    inFile >> line;
    
    for(int i = 0 ; i < line ; i++){
        int tmin = 0, tmax = 2000000, ans = 0;
        inFile >> tmin >> tmax;
        

        
        int res = 0;
        int red = 0;
        
        if(tmax > 10){
            string max = getStrFromInt(tmax);
            string min = getStrFromInt(tmin);

            for(int j = tmin ; j <= tmax ; j++){
                for(int k = j ; k <= tmax ; k++){
                    if(checkPair(j,k)){
                        res++;
//                        cout << j <<"  "<<k<<endl;                    
                    }
                }
            }
        }
        
        outFile << "Case #" << i+1 << ": "<< res << endl;
        cout << "Case #" << i+1 << ": "<< res << endl;
    }
}

