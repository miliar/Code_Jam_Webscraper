 #include<iostream>
 #include<fstream>
 #include<vector>
 using namespace std;
 
 int main() {
    
    ifstream IN("in.txt");
    ofstream OUT("out.txt");
    int L, D, N;
    IN >> L >> D >> N;
    vector<string> V(D);
    vector<char> C;
    vector<bool> check(D,1);
    for (int i = 0; i < D; i++) {
           IN >> V[i];     
    }
    string s;
    int a,poz,start,sum;
    for (int i = 1; i <= N; i++) {
           IN >> s;
           sum = 0;
           poz = 0;
           a = 0;
           for (int j = 0; j < s.size(); j++) {
              if (s[j] == '(') { 
                   a = 1;
                   j++;
              }
              if (a == 0) {
                for (int k = 0; k < V.size(); k++) {
                  if (check[k]) {
                    if (V[k][poz] != s[j]) 
                      check[k] = 0;
                   }
                }   
                poz++;
              }
              if (a == 1) {
                if(s[j] != ')')
                  C.push_back(s[j]);
              }
             
              if (s[j] == ')') {
                for (int k = 0; k < V.size(); k++) {
                  if (check[k]) {
                    start = 1;
                    for (int m = 0; m < C.size(); m++) 
                      if (C[m] == V[k][poz]) start = 0;
                    if (start) check[k] = 0;
                  }
                }
                poz++;
                C.clear();
                a = 0;
             }     

           }
           for (int j = 0; j < D; j++) 
            if (check[j]) sum++;
          OUT<<"Case #"<<i<<": "<<sum<<endl;
          for (int j = 0; j < D;j++) check[j] = 1;    
    }
}
    
    