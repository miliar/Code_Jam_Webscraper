#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

char table[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {

    FILE *input = fopen("A-small-attempt1.in", "r");
    FILE *output = fopen("A.out", "w");

    int T;
    {
        int d = 0;
        while (true) {
            char ch = fgetc(input);
            if (ch == '\n') break;
            d = d * 10 + (ch  - '0');
        }
        T = d;
    }

    for (int t = 0; t < T; t++) {
        char c[100 + 1];
        fgets(c, 110, input);
        
        string in(c);
        in.erase(in.end() - 1);

        string out;
        for (int i = 0; i < in.size(); i++){
            out.push_back(in[i] == ' ' ? ' ' : table[in[i] - 'a']);
        }

        fprintf(output, "Case #%d: ", t + 1);
        fprintf(output, "%s\n", out.c_str());
    }

    return 0;
}
