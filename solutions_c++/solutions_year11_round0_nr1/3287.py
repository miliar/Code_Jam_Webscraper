#include <cstdio>
#include <utility>
using namespace std;

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int t, n;
pair<int, int> o_aim[105];
pair<int, int>  b_aim[105];
int o_aims, b_aims;

int main()
{
    fscanf(in, "%d ", &t);
    for (int i = 0; i < t; i++) {
        o_aims = b_aims = 0;
        fscanf(in, "%d ", &n);
        for (int j = 0; j < n; j++) {
            char c; int a;
            fscanf(in, "%c%d ", &c, &a);
            if (c == 'O') {
                o_aim[o_aims].first = a;
                o_aim[o_aims].second = j;
                o_aims++;
            } else {
                b_aim[b_aims].first = a;
                b_aim[b_aims].second = j;
                b_aims++;
            }
        }
        o_aim[o_aims].second = 2000000000;
        b_aim[b_aims].second = 2000000000;
        
        int o = 1, b = 1, o_i = 0, b_i = 0, moves = 0;
        while (o_i < o_aims || b_i < b_aims) {
            if (o_aim[o_i].second < b_aim[b_i].second) {
                if (o == o_aim[o_i].first) o_i++;
                else if (o < o_aim[o_i].first) o++;
                else o--;
                
                if (b < b_aim[b_i].first) b++;
                else if (b > b_aim[b_i].first) b--;
            } else {
                if (b == b_aim[b_i].first) b_i++;
                else if (b < b_aim[b_i].first) b++;
                else b--;
                
                if (o < o_aim[o_i].first) o++;
                else if (o > o_aim[o_i].first) o--;
            }
            moves++;
        }
        fprintf(out, "Case #%d: %d\n", i+1, moves);
    }
    fclose(in);
    fclose(out);
    return 0;
}
