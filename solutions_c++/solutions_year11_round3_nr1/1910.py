#include<cstdio>

char a[55][55];

int
main()
{
    int t;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc ++){
        int n,m;
        scanf("%d %d",&n,&m);
        for(int i = 0; i < n; i ++)
            scanf("%s",a[i]);

        for(int i = 0; i+1 < n; i ++)
            for(int j = 0; j+1 < m; j ++)
                if(a[i][j] == '#' && a[i][j+1] == '#'
                 && a[i+1][j] == '#' && a[i+1][j+1] == '#'){
                    a[i][j] = '/';
                    a[i+1][j] = '\\';
                    a[i][j+1] = '\\';
                    a[i+1][j+1] = '/';
                }
        bool good = true;
        printf("Case #%d:\n",tc);
        for(int i = 0; i < n; i ++)
            for(int j = 0; j < m; j ++)
                if(a[i][j] == '#') good = false;
        if(good){
            for(int i = 0; i < n; i ++)
                printf("%s\n",a[i]);
        }else printf("Impossible\n");
    }
    return 0;
}
