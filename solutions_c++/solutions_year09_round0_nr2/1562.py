#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define INF 100000

using namespace std;

int filas,columnas;

inline bool inside(int cord1,int cord2)
{
    return (cord1>=0 && cord1<filas && cord2>=0 && cord2<columnas);
}

int main()
{

    freopen("Bs.in","r",stdin);
    freopen("Bs.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    int dirs[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
    FOR (casos,cases)
    {
        char etiqueta='a';
        map<pair<int,int>, char>  mapa;
        scanf("%d%d",&filas,&columnas);
        vector<vector<int> > matrix(filas,vector<int>(columnas));
        vector<vector<char> > matrixr(filas,vector<char>(columnas,'1'));
        FOR (i,filas)
            FOR (j,columnas)
                scanf("%d",&matrix[i][j]);
        FOR (i,filas)
            FOR (j,columnas)
            {
                int cord1=-1,cord2=-1,ncord1=i,ncord2=j;
                while (!(ncord1==cord1 && cord2==ncord2))
                {
                    cord1=ncord1;
                    cord2=ncord2;
                    int minimo=INF;
                    FOR (k,4)
                        if (inside(cord1+dirs[k][0],cord2+dirs[k][1]) && matrix[cord1][cord2]>matrix[cord1+dirs[k][0]][cord2+dirs[k][1]] && matrix[cord1+dirs[k][0]][cord2+dirs[k][1]]<minimo)
                        {
                            ncord1=cord1+dirs[k][0];
                            ncord2=cord2+dirs[k][1];
                            minimo=matrix[ncord1][ncord2];
                        }
                }
                if (mapa.find(make_pair(ncord1,ncord2))==mapa.end())
                {
                    mapa[make_pair(ncord1,ncord2)]=etiqueta;
                    etiqueta++;
                }
                matrixr[i][j]=mapa[make_pair(ncord1,ncord2)];
            }

        printf("Case #%d:\n",casos+1);
        FOR (i,filas)
        {
            int j;
            for (j=0;j<columnas-1;j++)
                printf("%c ",matrixr[i][j]);
            printf("%c\n",matrixr[i][j]);
        }

    }
    return 0;
}
