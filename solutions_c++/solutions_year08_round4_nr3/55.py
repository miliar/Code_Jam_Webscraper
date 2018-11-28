#include <cmath>
#include <iostream>
using namespace std;
#define sqr(x) (x)*(x)
#define pi 3.141592653589793

const int maxn = 1010, get = 50, d = 25;
int node[maxn][4], board[3], n, i, num, j, ts, o;
double delta;
pair< double, pair <double, pair <double, double> > > list[maxn];

double dis(int lab) {
       double ret = 0;
       for (int i=1; i<=n; i++)
           ret >?= (fabs(node[i][0] - list[lab].second.first) 
                  + fabs(node[i][1] - list[lab].second.second.first)
                  + fabs(node[i][2] - list[lab].second.second.second)) / node[i][3];
       return ret;
}

void update(int lab) {
     double x = rand(), y = rand();
     x -= int(x/pi/2)*pi*2;
     y -= int(y/pi)*pi-pi/2;
     list[0].second.first  = list[lab].second.first +delta*cos(x)*cos(y);
     list[0].second.second.first = list[lab].second.second.first+delta*sin(x)*cos(y);
     list[0].second.second.second = list[lab].second.second.second+delta*sin(y);
     if ((list[0].first = dis(0)) < list[lab].first)
        list[lab] = list[0];
}

main() {
       freopen("b.in", "r", stdin);
       freopen("b.out", "w", stdout);
       
       for (cin >> ts; ++o <= ts; ) {
           cin >> n;
           for (i=1; i<=n; i++)
               cin >> node[i][0] >> node[i][1] >> node[i][2] >> node[i][3];
           num = get;
           for (i=1; i<=num; i++) {
               j = rand()%n+1;
               list[i].second.first  = node[j][0];
               list[i].second.second.first = node[j][1];
               list[i].second.second.second = node[j][2];
               list[i].first = dis(i);
//               cout << j << ' ' << dis(i) << endl;
           }
           delta = 1000000;
           while (delta>1e-7) {
                 sort(list+1, list+num+1);
                 if (num>10) num -= 5;
                 for (i=1; i<=num; i++)
                     for (j=1; j<=d; j++) 
                         update(i);
                 delta *= 0.9;
//                 cout << delta << endl;
           }
        printf("Case #%d: %.6lf\n", o, list[1].first);
        }
}
