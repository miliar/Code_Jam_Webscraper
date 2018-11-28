#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int nbTests;
    scanf("%d", &nbTests);
    for(int test=1; test<=nbTests; test++)
    {
        int nbBoutons;
        scanf("%d", &nbBoutons);
        vector<int> pos[2];
        vector<bool> k;        
        for(int bouton=0; bouton<nbBoutons; bouton++)
        {
            char type[2]; int posi;
            scanf("%s %d", type, &posi);
            bool type_ = type[0] == 'B';
            pos[type_].push_back(posi);
            k.push_back(type_);
        }

        int p[2] = {1,1};
        int d[2] = {0,0};
        int time = 0;
        for(int bouton=0; bouton<nbBoutons; bouton++)
        {
            bool x = k[bouton];
            int t = abs(pos[x][d[x]]-p[x]) + 1;
            time += t;
            p[x] = pos[x][d[x]];
            d[x]++;
            x = !x;
            if(d[x] == pos[x].size())
                continue;
            if(pos[x][d[x]] < p[x])
                p[x] = max(pos[x][d[x]], p[x]-t);
            else
                p[x] = min(pos[x][d[x]], p[x]+t);
        }
        
        for(int i=0; i<2; i++)
            pos[i].clear();
        k.clear();
        
        printf("Case #%d: %d\n", test, time);
    }
            
    return 0;
}