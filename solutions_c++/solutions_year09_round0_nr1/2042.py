#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <string>

#define FOREACH( i, C ) for( __typeof(C.begin())i = C.begin(); i != C.end(); ++i )
#define CLEAR( V )      memset( V, 0, sizeof(V) )

using namespace std;

int L, D, N;
long S = 0;

vector<string> dic;
vector<string> T;

int main() {
    scanf("%d%d%d", &L, &D, &N);
    string str = "";
    for(int i = 0; i < D; ++i) {
            cin >> str;
            dic.push_back(str);               
    }    
    
    
    getchar();



        
    char c;
    for (int no = 1; no <= N; ++no) {
        S = 0;
        
        T.clear();
        while((c = getchar()) != '\n') {
                 string str = "";
                 
                 if(islower(c)) {
                               str.push_back(c);
                 }
                 else if (c == '(') {
                               while((c = getchar()) != ')') {
                                        str.push_back(c);         
                               }
                 }
                 T.push_back(str);         
        }
        
        FOREACH(w, dic) {
                   int n = w->size();
                   bool ok = true;
                   for (int i = 0; i< n; ++i) {
                       char a = (*w)[i];
                       
                       if (T[i].find_first_of(a) == string::npos) { ok = false; break;}
                   }           
                   if (ok ) ++S;
        }
        
        printf("Case #%d: %ld\n", no, S);
    }
    return 0;
}
