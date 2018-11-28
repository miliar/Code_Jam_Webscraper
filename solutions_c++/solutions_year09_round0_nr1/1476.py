#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

struct token {
       char letter;
       token *next;
};

token* tokens[15];
char dictionary[5000][15];
int L,D,N;

bool contains(char a, token *t) {
     if (t == NULL) return false;
     else if (t->letter == a) return true;
     else return contains(a,t->next);
}


int main() {
    scanf("%d %d %d\n", &L,&D,&N);
    for (int i=0; i<D; i++) {
        for (int j=0; j<=L; j++) {
            char letter;
            scanf("%c", &letter);
            if (letter != 10) dictionary[i][j] = letter;
        }  
    }
    
    for (int i=0; i<N; i++) {
        int open = 0;
        int counter = 0;
        int len = 0;
        for (int j=0; j<L; j++) tokens[j] = NULL;
        while (true) {
              char letter;
              int scan = scanf("%c", &letter);
              if ((scan == EOF) || (letter == 10)) {
                 break;
              }
              else {
                   if (letter == '(') open = 1;
                   else if (letter == ')') {
                        open = 0;
                        len++;
                   }
                   else {
                        token *e = new token;
                        e->letter = letter;
                        e->next = tokens[len];
                        tokens[len] = e;
                        if (open == 0) len++;
                   } 
              }
        }
        
        for (int j=0; j<D; j++) {
            int check = 0;
            while (check < L) {
                bool cont = contains(dictionary[j][check],tokens[check]);
                if (cont == false) break;
                check++;
            }
            if (check == L) counter++;
        }
        printf("Case #%d: %d\n", i+1, counter);
        for (int j=0; j<L; j++) {
            token *e = tokens[j];
            while (e != NULL) {
                  token *f = e->next;
                  delete e;
                  e = f;
            }
        }          
    }
}
       
