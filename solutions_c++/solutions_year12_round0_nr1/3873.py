

#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

pair<string, string> corpus[3];

int main() {

    corpus[0] = pair<string, string>("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    corpus[1] = pair<string, string>("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    
    // augment the corpus with the z -> q and q -> z mappings from the hint
    corpus[2] = pair<string, string>("de kr kd eoya kw aej tysr re ujdr lkgc jv zq", "so it is okay if you want to just give up qz");
    
    /*
    for (int c = 'a'; c <= 'z'; c++) {
        bool ispresent = false;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < corpus[i].first.length(); j++)
                if (corpus[i].first[j] == c) {
                    ispresent = true;
                    goto next;
                }
    next:
        if (!ispresent) {
            printf("Missing %c\n", c);
        }
    }
    */
    
    
    char line[200];
    
    int T;
    cin >> T;
    cin.getline(line, 200); // eat '\n'
    
    for (int i = 1; i <= T; i++) {
    
        cout << "Case #" << i << ": ";
        
        cin.getline(line, 200);
        int len = strlen(line);
        
        
        for (int i = 0; i < len; i++) {
            
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < corpus[j].first.length(); k++)
                    if (corpus[j].first[k] == line[i]) {
                        cout << corpus[j].second[k];
                        goto next;
                    }        
        next:;
        }
    
        cout << endl;
    }
    
}
