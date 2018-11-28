#include <cstdio>
#include <utility>
using namespace std;

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int t, n;
unsigned c[20];
pair<unsigned, unsigned> p[2];
bool found;
unsigned answer;

unsigned max(unsigned a, unsigned b) {
    return (a > b ? a : b);
}

void func(int j, int k) {
    if (j == n) {
        if (p[0].first == p[1].first && p[0].second && p[1].second) {
            found = true;
            answer = max(answer, max(p[0].second, p[1].second));
        }
        return;
    }
    p[k].first ^= c[j];
    p[k].second += c[j];
    func(j+1, 0);
    func(j+1, 1);
    p[k].first ^= c[j];
    p[k].second -= c[j];
}

int main()
{
    fscanf(in, "%d", &t);
    for (int i = 0; i < t; i++)
    {
        found = false;
        answer = 0;
        fscanf(in, "%d", &n);
        for (int j = 0; j < n; j++)
            fscanf(in, "%u", &c[j]);
        func(0, 0);
        func(0, 1);
        fprintf(out, "Case #%d: ", i+1);
        if (found) fprintf(out, "%u\n", answer);
        else fprintf(out, "NO\n");
    }
    
    fclose(in);
    fclose(out);
    return 0;
}
