#include <cstdio>

int d[10010], l[10010];
int dis[10010];

int min(int a, int b){
    return (a < b)? a: b;
}

int max(int a, int b){
    return (a > b)? a: b;
}

int main(){
    int t;
    scanf("%d" ,&t);
    for(int T = 1; T <= t; T++){
        int n, ob;
        scanf("%d" ,&n);
        for(int i = 1; i <= n; i++){
            dis[i] = 0;
            scanf("%d %d" ,&d[i] ,&l[i]);
        }
        scanf("%d" ,&ob);
        dis[1] = d[1];
        bool flag = false;
        for(int i = 1, gap = 1; i <= gap; i++){
            if(ob - d[i] <= dis[i]){
                flag = true;
                break;
            }
            for(int j = i + 1; j <= n && d[j] - d[i] <= dis[i]; j++){
                if(j > gap) gap = j;
                dis[j] = max(dis[j], min(d[j] - d[i], l[j]));
            }
        }
        printf("Case #%d: %s\n" ,T ,flag? "YES": "NO");
    }
}
