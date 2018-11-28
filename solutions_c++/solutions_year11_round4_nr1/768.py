#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int casos, x, s, r, t, n, a, b, total;
double tt;
double tempo;

struct walk{
    double leng;
    int speed;
    
    const bool operator < (const walk &that) const{
        return speed < that.speed;
    }
} walks[1005];

int main (){
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
	scanf("%d", &casos);
	int contador = 1;
	while(casos--){
	    total = 0;
        printf("Case #%d: ", contador++);
        scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
        for(int i = 1; i <= n; i++){
            scanf("%d %d %d", &a, &b, &walks[i].speed);
            walks[i].speed += s;
            walks[i].leng = b-a;
            total += b-a;
        }
        sort(walks+1, walks+n+1);
        total = x-total;
        walks[0].leng = total;
        walks[0].speed = s;
        tt = t;
        int inc = r-s;
        tempo = 0;
        for(int i = 0; i <= n; i++){
             if((walks[i].speed+inc) * tt <= walks[i].leng){
                 tempo += tt;
                 walks[i].leng -= (walks[i].speed+inc) * tt;
                 tt = 0;
             }
             else{
                 double z = walks[i].leng / (double)(walks[i].speed+inc);
                 tempo += z;
                 tt -= z;
                 walks[i].leng = 0;
             }
             tempo += walks[i].leng/ (double)walks[i].speed;
             
        }
        printf("%.7lf\n", tempo);
	}
    return 0;
}
