#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>

char names[2000][11];
int curname = 1;

struct tree
{
    double p;
    int dec;
    tree *sub[2];
};

tree trees[2000];
int curtree = 1;
inline tree *new_tree(void)
{
    return trees+curtree++;
}

inline bool nonclose(int c) { return c != ')' && !isalpha(c); }

inline void init_tree(void)
{
    memset(trees, 0, sizeof(trees));
    curname = 1;
    curtree = 1;
}

inline tree *read_tree(void)
{
    tree *t = new_tree();
    int c;
    while ((c = getchar()) != '(');
    scanf("%lf", &t->p);
    while (nonclose(c = getchar()));
    if (c == ')')
        return t;
    names[curname][0] = c;
    int i = 1;
    for ( ; isalpha(c = getchar()) ; i++)
        names[curname][i] = c;
    names[curname][i] = 0;
    t->dec = curname;
    curname++;
    t->sub[0] = read_tree();
    t->sub[1] = read_tree();
    while ((c = getchar()) != ')');
    return t;
}

bool curanimal[2000];
inline void read_animal(void)
{
    char s[11];
    memset(curanimal, 0, sizeof(curanimal));
    int n;
    scanf("%*s%d", &n);
    for (int f = 0 ; f < n ; f++)
        {
            scanf("%s", s);
            for (int i = 1 ; i < curname ; i++)
                {
                    if (strcmp(s, names[i]))
                        continue;
                    curanimal[i] = true;
                }
        }
}

inline double nice(tree *t, double p)
{
    p = p * t->p;
    if (!t->dec)
        return p;
    if (curanimal[t->dec])
        return nice(t->sub[0], p);
    return nice(t->sub[1], p);
}

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int t = 1 ; t <= T ; t++)
        {
            printf("Case #%d:\n", t);
            init_tree();
            scanf("%*d");
            tree *t = read_tree();
            int A;
            scanf("%d\n", &A);
            for (int a = 0 ; a < A ; a++)
                {
                    read_animal();
                    printf("%0.9f\n", nice(t, 1.0));
                }
        }

    return 0;
}
