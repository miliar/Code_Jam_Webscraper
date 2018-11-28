#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <fstream>

using namespace std;

int a, b, ev;
vector <string> trans(a);
vector <string> opp(b);
vector <char> v;

bool estransf (char a, char b, char& c){
     string tmp = "";
     tmp+=a;
     tmp+=b;
     string tmp2 = "";
     tmp2+=b;
     tmp2+=a;
     //cout <<"tmptmp2 "<<tmp<<" "<<tmp2<<endl;
     for (int i = 0; i < trans.size(); i++){
         string aux = trans[i].substr (0, 2);
         if (tmp == aux or tmp2==aux) {c = trans[i][2]; return true; }
     }
     return false;
}

bool esopp(char a){
     
     for (int i = 0; i < opp.size(); i++){
         if (opp[i][0]==a){
            char aux = opp[i][1];
            for (int j = 0; j < v.size(); j++){
                if (v[j]==aux) return true;
            }
         } 
         if (opp[i][1] == a){
            char aux = opp[i][0];
            for (int j = 0; j < v.size(); j++){
                if (v[j]==aux) return true;
            }
         }
     }
     
     return false;
}


int main(){
    ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");
    int c;
    fin >>c;
    for (int d = 0; d < c; d++){
        
        fin >>a;
        trans = vector <string> (a);
        for (int i = 0; i < a; i++) fin >>trans[i];
        fin >>b;
        opp = vector <string > (b);
        for (int i = 0; i < b; i++) fin >>opp[i];
        string s;
        fin >>ev;
        fin >>s;
        v = vector <char> ();
        v.clear();
        for (int i = 0; i < ev; i++){
            if (v.empty()) v.push_back(s[i]);
            else {
                 char res;
                 if (estransf(v.back(), s[i], res)){
                    v.pop_back();
                    v.push_back(res);
                 }
                 else {
                      if (esopp(s[i])) v.clear();
                      else v.push_back(s[i]);
                 }
            }
        }
        int cont = 0;
        fout <<"Case #"<<d+1<<": [";
        for (int i = 0; i < v.size(); i++){
            if (cont == 0) fout <<v[i];
            else fout <<", "<<v[i];
            cont++;
        }
        fout <<"]"<<endl;
    }
}
