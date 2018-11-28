
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
//#include <assert>

//#define debug

using namespace std;

//struct node;

struct node {
    vector <node *> children;
    vector <int> weight;
};

inline int convert(char c) {
    return ((int)c)-((int)((char)'a'));
}


int rek(node *n, char *tokens, int pos, int length) {
    unsigned int ret = 0;

    #ifdef debug
        cerr << "rek: " << tokens << " pos: " << pos << " length: " << length << endl;
    #endif


    // parsowanie tokenów
    vector <bool> possible;
    possible.resize(26, false);
    if (tokens[pos] == '(') {
        pos++;
        while (tokens[pos] != ')') {
            possible[convert(tokens[pos])] = true;
            pos++; 
        }
    } else
        possible[convert(tokens[pos])] = true;
    pos++;
    
    for (int i = 0; i < 26; i++) {
        #ifdef debug
            fprintf(stderr, "rek %d possible[i]: %d \n", i, (int)possible[i]);
        #endif

        if (possible[i] && (n->children[i] != NULL)) {
        #ifdef debug
            fprintf(stderr, "rek %d\n", i);
        #endif
            if (pos < length)
                ret += rek(n->children[i], tokens, pos, length);
            else {
                ret += 1;
            #ifdef debug
                fprintf(stderr, "ret+=1\n");
            #endif
            }
        }
    }
    return ret;
}   


node *create(char *word, int depth, int length, node *p, node *n) {


    #ifdef debug
        cerr << "create: " << word << " depth: " << depth << "ac: " << convert(word[depth]) << " length: " << length << endl;
    #endif
    if (n == NULL) {
        n = new node;
        n->children.resize(26, NULL);
        n->weight.resize(26, 0);
    }

    if (depth < length) {
        n->children[convert(word[depth])] = create(word, depth+1, length, n, n->children[convert(word[depth])]);
        n->weight[convert(word[depth])]++;
    }  
    return n;
}

int main() {
    unsigned int L, D, N;
    cin >> L >> D >> N;

    node *tree = NULL;

    char word[17];
    for (int i = 0; i < D; i++) {   
        cin >> word;
        // konstrukcja drzewa - słownika
        tree = create(word, 0, L, NULL, tree);
    } 
    unsigned int result;
    char tokens[18*25];
    for (int i = 0; i < N; i++) {
        cin >> tokens;
        result = rek(tree, tokens, 0, strlen(tokens));
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}
