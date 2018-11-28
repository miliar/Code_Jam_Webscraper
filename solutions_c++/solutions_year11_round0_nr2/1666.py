#include <cstdio>
#include <vector>
using namespace std;

#define ASIZE 66
#define ISIZE 666

typedef vector<int> vi;

int n;
char invoke[ISIZE];
bool opposited[ASIZE][ASIZE];
int combine[ASIZE][ASIZE];
vi v;

void load(void) {

    for (int i = 0; i < ASIZE; i++) {
        for (int j = 0; j < ASIZE; j++) {
            opposited[i][j] = false;
            combine[i][j] = -1;
        }
    }
    v.clear();

    int c, d;
    char s[48];

    scanf("%d", &c);
    for (int i = 0; i < c; i++) {
        scanf("%s", s);
        combine[s[0]-'A'][s[1]-'A'] = s[2]-'A';
        combine[s[1]-'A'][s[0]-'A'] = s[2]-'A';
    }

    scanf("%d", &d);
    for (int i = 0; i < d; i++) {
        scanf("%s", s);
        opposited[s[0]-'A'][s[1]-'A'] = true;
        opposited[s[1]-'A'][s[0]-'A'] = true;
    }

    scanf("%d", &n);
    scanf("%s", invoke);
}

void echo(void) {
    putchar('[');
    for (int i = 0; i < v.size(); i++) {
        if (i) {
            printf(", ");
        }
        putchar('A' + v[i]);
    }
    putchar(']');
}

bool is_opposite(int x) {
    for (int i = 0; i < v.size(); i++) {
        if (opposited[x][v[i]]) {
            return true;
        }
    }
    return false;
}

int main(void) {

    int t;
    scanf("%d", &t);

    for (int ti = 1; ti <= t; ti++) {
        printf("Case #%d: ", ti);
        load();

        for (int i = 0; i < n; i++) {
            int c = invoke[i] - 'A';
            if (!v.empty() && combine[c][v[v.size()-1]] >= 0) {
                v[v.size()-1] = combine[c][v[v.size()-1]];
                continue;
            }
            if (is_opposite(c)) {
                v.clear();
                continue;
            }
            v.push_back(c);
        }

        echo();

        printf("\n");
    }

    return 48-48;
}
