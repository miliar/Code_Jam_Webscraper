#include <iostream>
#include <stack>
#include <vector>
using namespace std;

typedef vector< vector<char> > Matrix;

int main() {
 int t;
 cin >> t;
 for (int i=0; i<t; i++) {
     Matrix combi(26,vector<char>(26,'z'));
     Matrix incomp(26,vector<char>(0));
     vector<int> v(26,0);
     
     int c;
     cin >> c;
     while (c--) {
           string s;
           cin >> s;
           combi[int(s[0]-'A')][int(s[1]-'A')] = combi[int(s[1]-'A')][int(s[0]-'A')] = s[2];          
     }
     int d;
     cin >> d;
     while (d--) {
           string s;
           cin >> s;
           incomp[int(s[0]-'A')].push_back(s[1]);
           incomp[int(s[1]-'A')].push_back(s[0]);     
     }
     stack<char> st;
     int n;
     cin >> n;
     while(n--) {
         char c;
         cin >> c;
         if (!st.empty()) {
            char tmp = st.top();
            char cmb = combi[int(c-'A')][int(tmp-'A')];
            if (cmb!='z') {//si combina...
               st.pop();
               st.push(cmb);
               v[int(tmp-'A')]--;
               v[int(cmb-'A')]++;  
               for (int j=0; j<incomp[int(cmb-'A')].size(); j++) {
                   if (v[int(incomp[int(cmb-'A')][j]-'A')] > 0) { //hi ha algun element incompatible
                      for (int k = 0; k<v.size(); k++) v[k] = 0;
                      while (!st.empty()) st.pop();  
                      break;                          
                   }   
               }                                        
            }
            else {
                 bool peta = false;
                 for (int j=0; j<incomp[int(c-'A')].size(); j++) {
                   if (v[int(incomp[int(c-'A')][j]-'A')] > 0) { //hi ha algun element incompatible
                      peta = true;
                      for (int k = 0; k<v.size(); k++) v[k] = 0;
                      while (!st.empty()) st.pop();  
                      break;                          
                   }   
                 }
                 if (!peta) {
                    st.push(c);
                    v[int(c-'A')]++;
                 }
            }                                               
         }
         else {
              st.push(c);
              v[int(c-'A')]++;  
         }           
     }
     cout << "Case #" << i+1 << ": [";
     stack<int> aux;     
     while (!st.empty()) {
           int aux2 = st.top();
           aux.push(aux2);
           st.pop();
     }
     if (!aux.empty()) {
        cout << char(aux.top());
        aux.pop();                  
     }
     while(!aux.empty()) {
        cout << ", " << char(aux.top());
        aux.pop();                    
     }
     cout << "]" << endl;    
 } 
}
