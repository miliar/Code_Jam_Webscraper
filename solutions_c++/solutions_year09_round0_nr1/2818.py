#include <iostream>

using namespace std;

class tree {
      public:
             bool isLeaf;
             int level;
             tree * next[26];
             tree(int l = 0){
                     level = l;
                    isLeaf = false;
                    for (int i=0; i<26; i++) next[i] = NULL;
             }
             void check(char * text){
                  if (!isLeaf){
                     for (int i=0; i<26; i++){
                         if (next[i] != NULL){
                            text[level] = i+'a';
                            next[i]->check(text);
                         }    
                     }
                  }
                  else {
                       text[level] = 0;
                       cout << text << endl;     
                  }
             }
             int eval(char * test, char * text){
                  if (isLeaf){
                     text[level] = 0;
                     return 1;
                  }
                  else {
                       char token[30];
                       int nexttoken = 1;
                       if (test[0] == '('){
                          int i = 1;
                          while (test[i] != ')'){
                                token[i-1] = test[i];      
                                i++;
                          }
                          nexttoken = i+1;
                          token[i-1] = 0;
                       }            
                       else {
                            token[0] = test[0];
                            token[1] = 0;     
                       }     
                       int i = 0;
                       int ret = 0;
                       while (token[i] != 0){
                              int index = token[i] - 'a';
                              if (next[index] != NULL){
                                 text[level] = token[i];
                                 ret += next[index]->eval(test+nexttoken, text);                
                              }
                              i++;
                        }     
                        return ret;
                  }
             }
};

tree root;

int main(){
    int L, D, N;
    cin >> L >> D >> N;
    char temp[L+1];
    tree * ttree;
    for (int i=0; i<D; i++){
        cin >> temp;
        ttree = &root;
        for (int j=0; j<L; j++){
            int index = temp[j] - 'a';
            if (ttree->next[index] == NULL){
               ttree->next[index] = new tree(j+1);
            }
            ttree = ttree->next[index];
            if (j == L-1){
               ttree->isLeaf = true;
            }
        }
    }       
    char test[30*L];
    for (int i=0; i<N; i++){
        cin >> test;
        cout << "Case #" << i+1 << ": " << root.eval(test, temp) << endl;
    }
   // root.check(temp);
    
}
