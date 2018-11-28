#include <fstream>
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cstring>
#include <cmath>

#include <cstdio>
#include <cstdlib>

using namespace std;

#define HASH_SIZE ('z' - 'a' + 1)

double fl_freq[HASH_SIZE];
double freq[HASH_SIZE];

double rel_freq[HASH_SIZE];

char mapping[HASH_SIZE];

vector<char *> words[128];

#define WREL_FREQ(x, y)  rel_freq[x - 'a'] = y

void init() {
    WREL_FREQ('a', 0.08167);
    WREL_FREQ('b', 0.01492);
    WREL_FREQ('c', 0.02782);
    WREL_FREQ('d', 0.04253);
    WREL_FREQ('e', 0.12702);
    WREL_FREQ('f', 0.02228);
    WREL_FREQ('g', 0.02015);
    WREL_FREQ('h', 0.06094);
    WREL_FREQ('i', 0.06966);
    WREL_FREQ('j', 0.00153);
    WREL_FREQ('k', 0.00772);
    WREL_FREQ('l', 0.04025);
    WREL_FREQ('m', 0.02406);
    WREL_FREQ('n', 0.06749);
    WREL_FREQ('o', 0.07507);
    WREL_FREQ('p', 0.01929);
    WREL_FREQ('q', 0.00095);
    WREL_FREQ('r', 0.05987);
    WREL_FREQ('s', 0.06327);
    WREL_FREQ('t', 0.09056);
    WREL_FREQ('u', 0.02758);
    WREL_FREQ('v', 0.00978);
    WREL_FREQ('w', 0.02360);
    WREL_FREQ('x', 0.00150);
    WREL_FREQ('y', 0.01974);
    WREL_FREQ('z', 0.00074);
}

char line[32][128];
char result[32][128];
int nchars = 0;
int nflchars = 0;

void sum_freq(char *line) {
    int len = strlen(line);
    int new_word = 1;

    for (int i = 0; i < len; i++) {
        if (line[i] >= 'a' && line[i] <= 'z') {
            if (new_word) {
                fl_freq[line[i] - 'a']++;
                nflchars++;
            }
            new_word = 0;
            nchars++;
            freq[line[i] - 'a']++;
        }
        else {
            new_word = 1;
        }
    }

    char *str = strtok(line, " \n");
    if (str) {
        words[strlen(str)].push_back(strdup(str));
    }
    while ((str = strtok(NULL, " \n")) != NULL) {
        if (str) {
            words[strlen(str)].push_back(strdup(str));
        }
    }
}

//#define DEBUG

void count_freq() {
    if (nchars == 0)
        return;

    for (int i = 0; i < HASH_SIZE; i++) {
        freq[i] /= nchars;
        fl_freq[i] /= nflchars;
#ifdef DEBUG
        printf("%c => %lf\n", i + 'a', fl_freq[i]);
#endif
    }
}

void do_inplace_replace(char *str, int len) {
    for (int i = 0; i < len; i++) {
        if (str[i] < 'a' || str[i] > 'z') {
            continue;
        }
        else if (mapping[str[i] - 'a'] != 'N') {
            str[i] = mapping[str[i] - 'a'];
        }
    }
}

void compute_mapping() {
    for (int i = 0; i < HASH_SIZE; i++) {
        mapping[i] = 'N';
    }


    string src = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string dst = "our language is impossible to understand";

    for (int i = 0; i < src.size(); i++) {
        mapping[src[i] - 'a'] = dst[i];
    }
                
    src = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    dst = "there are twenty six factorial possibilities";

    for (int i = 0; i < src.size(); i++) {
        mapping[src[i] - 'a'] = dst[i];
    }

    src = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    dst = "so it is okay if you want to just give up";

    for (int i = 0; i < src.size(); i++) {
        mapping[src[i] - 'a'] = dst[i];
    }

    mapping['y' - 'a'] = 'a';
    mapping['q' - 'a'] = 'z';
    mapping['e' - 'a'] = 'o';
    // z remains unmapped
    mapping['z' - 'a'] = 'q';
}

void do_convert(char *line, char *result) {
    int len = strlen(line);

    for (int i = 0; i < len; i++) {
        if (line[i] >= 'a' && line[i] <= 'z') {
            result[i] = mapping[line[i] - 'a'];
        }
        else {
            result[i] = line[i];
        }
    }
}

int main() {
    int T;
    scanf("%d\n", &T);

    //memset(fl_freq, 0, HASH_SIZE * sizeof(double));
    //memset(freq, 0, HASH_SIZE * sizeof(double));

    compute_mapping();

    for (int i = 0; i < T; i++) {
        memset(line[i], 0, 128);
        fgets(line[i], 128, stdin);
        //sum_freq(line[i]);
        do_convert(line[i], result[i]);
        printf("Case #%d: %s", i + 1, result[i]);
    }

    //count_freq();

    return 0;
}

