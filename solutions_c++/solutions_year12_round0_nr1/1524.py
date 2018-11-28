#include <cstdio>

int n;
char alpha[26] = {0};
char used[26] = {0};
char remaining[26] = {0};

void assign(char src, char dest) {
    alpha[src - 'a'] = dest;
    used[src - 'a'] = 1;
    remaining[dest - 'a'] = 1;
}

void pre_cal() {
    const char* src = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    const char* des = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    assign('y', 'a');
    assign('e', 'o');
    assign('q', 'z');
    int count = 3, c = 0, d = 0;
    while(src[c] != 0) {
        if(src[c] == ' ') {
            ++c;
            ++d;
            continue;
        }
        if(used[(src[c] - 'a')] == 0) {
            alpha[(src[c] - 'a')] = des[d];
            remaining[des[d] - 'a'] = 1;
            ++count;
            used[src[c] - 'a'] = 1;
        }
        ++c;
        ++d;
    }
    //printf("%d\n", count);
    for(int i = 0; i < 26; ++i) {
        if(used[i] == 0) {
            for(int j = 0; j < 26; ++j) {
                if(remaining[j] == 0) {
                    alpha[i] = (char)(j + 'a');
                    return;
                }
            }
        }
    }
}

void output(int cases) {
    printf("Case #%d: ", cases);
    char c;
    while((c = getchar()) != '\n') {
        if(c == ' ') {
            putchar(' ');
        } else {
            putchar(alpha[c - 'a']);
        }
    }
    puts("");
}

int main() {
    pre_cal();
    scanf("%d", &n);
    while(getchar() != '\n') {
    }
    for(int i = 1; i <= n; ++i) {
        output(i);
    }
    return 0;
}
