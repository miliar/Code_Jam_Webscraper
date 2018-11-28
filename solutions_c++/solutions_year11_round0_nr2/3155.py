#include <cstdio>
#include <utility>
using namespace std;

#define I(x) ((x)-'A')

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int t, c, d, n;
pair<bool, char> combine[30][30];
bool oppose[30][30];
char list[105];

int main()
{
    fscanf(in, "%d", &t);
    for (int i = 0; i < t; i++) {
        for (int x = 0; x < 30; x++) {
            for (int y = 0; y < 30; y++) {
                combine[x][y] = make_pair(false, '\0');
                oppose[x][y] = false;
            }
        }
        
        fscanf(in, "%d", &c);
        for (int j = 0; j < c; j++) {
            char a, b, ab;
            fscanf(in, " %c%c%c ", &a, &b, &ab);
            combine[I(a)][I(b)] = combine[I(b)][I(a)] = make_pair(true, ab);
        }
        
        fscanf(in, "%d", &d);
        for (int j = 0; j < d; j++) {
            char a, b;
            fscanf(in, " %c%c ", &a, &b);
            oppose[I(a)][I(b)] = oppose[I(b)][I(a)] = true;
        }
        
        int last = -1; char ch;
        fscanf(in, "%d", &n);
        for (int j = 0; j < n; j++) {
            fscanf(in, " %c ", &ch);
            list[++last] = ch;
            if (last > 0 && combine[I(list[last])][I(list[last-1])].first) {
                list[last-1] = combine[I(list[last])][I(list[last-1])].second;
                last--;
            } else {
                for (int k = 0; k < last; k++) {
                    if (oppose[I(list[k])][I(list[last])]) {
                        last = -1;
                        break;
                    }
                }
            }
        }
        
        fprintf(out, "Case #%d: [", i+1);
        for (int j = 0; j < last; j++)
            fprintf(out, "%c, ", list[j]);
        if (last > -1)
            fprintf(out, "%c", list[last]);
        fprintf(out, "]\n");
    }
    
    fclose(in);
    fclose(out);
    return 0;
}
