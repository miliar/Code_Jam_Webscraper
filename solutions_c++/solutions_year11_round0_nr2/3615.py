#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;


int tab[256][256];


int main()
{

    int t,d,n,n2;
    int a,b,c;
    char comb[3];
    scanf("%d\n",&t);
    for(int i = 1; i<=t;++i)
    {
        for(int ii = 0;ii<256;++ii)
        {
            for(int ij = 0; ij<256; ++ij)
            {
                tab[ii][ij] = 0;
            }
        }
        scanf("%d ",&d);
        for(int j = 0;j <d;++j)
        {
            scanf("%s ",comb);
            a = comb[0];
            b = comb[1];
            c = comb[2];
            tab[a][b] = c;
            tab[b][a] = c;
        }
        scanf("%d ",&n);
        for(int j =0;j<n;++j)
        {
            scanf("%s",comb);
            a = comb[0];
            b = comb[1];
            if(tab[a][b] > 0)
            {
                tab[a][b] = -tab[a][b];
                tab[b][a] = -tab[b][a];
            }
            else
            {
                tab[a][b] = -1;
                tab[b][a] = -1;
            }
        }
        scanf(" %d ",&n2);
        vector<int> v;
        char cc;
        scanf("%c",&cc);
        a = cc;
        v.push_back(a);
        for(int j =1; j<n2; ++j)
        {
            scanf("%c",&cc);
            a = cc;
            int tmp = v.back();
            if(tab[tmp][a] > 0)
            {

                v.pop_back();
                v.push_back(tab[tmp][a]);
                goto end;
            }
            else if(tab[tmp][a] <-1)
            {
                v.pop_back();
                v.push_back(-tab[tmp][a]);
                goto end;
            }
            else
            {
                v.push_back(a);
            }
            for(unsigned int k = 0; k<v.size(); ++k)
            {
                if(tab[a][v[k]] < 0)
                {
                    v.clear();
                    if(j +1 < n2)
                    {
                        scanf("%c",&cc);
                        ++j;
                        a = cc;
                        v.push_back(a);
                    }
                    goto end;
                }
            }
end:
            continue;
        }
        printf("Case #%d: [",i);
        while(v.size() > 1)
        {
            printf("%c, ",v.front());
            v.erase(v.begin());
        }
        if(v.size() == 1)
        {
            printf("%c",v.front());
        }
        printf("]\n");

    }


    return 0;
}
