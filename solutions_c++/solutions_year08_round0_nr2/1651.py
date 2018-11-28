#include <stdio.h>
#include <list>
#include <vector>
using namespace std;

struct sched
{
    int s, f, p;
    bool operator<(const sched & other)
    {
        return (s < other.s) || ((s == other.s) && (f < other.f));
    }
};

list<sched> l;
list<sched>::iterator it, et;

vector<int> va, vb;
vector<int>::iterator vit, vet;

int n, nn, t, na, nb, i;
char s[100];
sched sch;

int main()
{
    FILE * f = fopen("input.txt", "rt");
    fscanf(f, "%d", &n);
    for(nn = 1; nn <= n; ++nn)
    {
        l.clear();
        fscanf(f, "%d%d%d", &t, &na, &nb);
        for(i = 0; i < na; ++i)
        {
            sch.p = 0;
            fscanf(f, "%s", s);
            sch.s = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
            fscanf(f, "%s", s);
            sch.f = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
            l.push_back(sch);
        }
        for(i = 0; i < nb; ++i)
        {
            sch.p = 1;
            fscanf(f, "%s", s);
            sch.s = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
            fscanf(f, "%s", s);
            sch.f = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + (s[4] - '0');
            l.push_back(sch);
        }

        na = nb = 0;
        va.clear();
        vb.clear();
        l.sort();
        et = l.end();
        for(it = l.begin(); it != et; ++it)
        {
            if(it->p == 0)
            {
                vet = va.end();
                for(vit = va.begin(); vit != vet; ++vit)
                {
                    if(*vit <= it->s) break;
                }
                if(vit == vet) ++na;
                else va.erase(vit);
                vb.push_back(it->f + t);
            }
            else
            {
                vet = vb.end();
                for(vit = vb.begin(); vit != vet; ++vit)
                {
                    if(*vit <= it->s) break;
                }
                if(vit == vet) ++nb;
                else vb.erase(vit);
                va.push_back(it->f + t);
            }
        }

        printf("Case #%d: %d %d\n", nn, na, nb);
    }
    fclose(f);

    printf("Press ENTER...");
    gets(s);
    return 0;
}
