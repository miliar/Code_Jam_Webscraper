#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

#define SZ(x) ((int)(x).size())

using namespace std;

int main(){
    int tcc = 0, tc = 0;
    for(scanf("%d", &tc); tc; --tc){
                int k;
                string s;

                cin >> k >> s;
                
                vector<int> p;
                for (int i = 0; i < k; i++)
                    p.push_back(i);
                
                int best = SZ(s);
                    
                do{
                   int len = 0;
                   for (int j = 0; j < SZ(s) && len < best; j += k){
                       if ( j == 0 ) len++;
                       if ( j > 0 ){
                          if ( s[j + p[0]] != s[j - k + p[k - 1]] ) len++;
                       }                       
                       for (int i = 1; i < k; i++){
                           if ( s[j + p[i]] != s[j + p[i - 1]] ) len++;
                       }
                   }           
                   if ( len < best ) best = len;   
                   
                  /* for (int i = 0; i < k; i++)
                       cout << p[i] << " ";
                   cout << ":" << len << endl;     */
                }while(next_permutation(p.begin(), p.end()));
                
                printf("Case #%d: %d\n", ++tcc, best);
    }
    return 0;    
}
