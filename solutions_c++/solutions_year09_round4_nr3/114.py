/*ITA - O que é Overflow?*/
/*Algoritmo Húngaro sem pesos, matching bipartido em O(n^3), mas roda bem rápido*/
#include<cstdio>

#define MAXN 110

int m, n;
int matm[MAXN],mrkm[MAXN];
int matn[MAXN],mrkn[MAXN];
int tab[MAXN][MAXN];

int match(int v){
    
    int i;
    mrkn[v] = 1;
    
    for(i=0;i<m;i++){
        
        if(mrkm[i] || !tab[v][i]) continue;
        /*direto*/
        if(matm[i] < 0){
            matm[i] = v;
            matn[v] = i;
            return 1;   
        }
        
        mrkm[i] = 1;
        /*remove esse matching e tenta*/
        if(match(matm[i])){
            matm[i] = v;
            matn[v] = i;
            return 1;   
        }   
        
    }
    
    return 0;   
    
}

/*matching hungaro 0-1, tab construido*/
int hungarian(){
    
    int i,j;
        
    for(i=0;i<n;i++)
        matn[i] = -1;   
    for(i=0;i<m;i++)
        matm[i] = -1;
        
    for(i=0;i<n;i++){
            
        for(j=0;j<n;j++)
            mrkn[j] = 0;   
        for(j=0;j<m;j++)
            mrkm[j] = 0;
            
        match(i);
    }
        
    return 0;
    
}

int values[MAXN][MAXN];
int k;

int main()
{
    int t, teste;
    int i, j, a;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        scanf("%d %d", &n, &k);
        for (i=0; i<n; i++)
        {
            for (j=0; j<k; j++)
            {
                scanf("%d", &values[i][j]);
            }
        }
        for (i=0; i<n; i++)
        {
            for (j=0; j<n; j++)
            {
                if (j == i)
                {
                    tab[i][j] = 0;
                }
                else
                {
                    tab[i][j] = 1;
                    for (a = 0; a < k; a++)
                    {
                        if (values[i][a] <= values[j][a])
                            break;
                    }
                    if (a < k)
                    {
                        tab[i][j] = 0;
                    }
                }
            }
        }
        m = n;
        hungarian();
        int resp = 0;
        for (i=0; i<n; i++)
        {
            if (matn[i] == -1)
                resp++;
        }
        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;
}
