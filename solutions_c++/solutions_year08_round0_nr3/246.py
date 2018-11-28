#include <stdio.h>
#include <stdlib.h>
#include <math.h>
const double EPS = 1e-8;

double dist(double x1, double y1, double x2, double y2){
    return sqrt( (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) );
}

//线段和圆相交求交点 
bool intersect(double x1, double y1, double x2, double y2, double xr, double yr, double r, int &num, double &px1, double &py1, double &px2, double &py2){
    double low, up, mid, d, d2;
    if (dist(x1, y1, xr, yr) < r){
        if (dist(x2, y2, xr, yr) < r - EPS) return false;
        low = 0; up = 1;
        while (true){
            mid = (up + low) / 2;
           // //printf("up = %lf low = %lf\n", up, low);
            d = dist(x1 + mid * (x2 - x1), y1 + mid * (y2 - y1), xr, yr);
            if (fabs(d - r) < EPS) break;
            if (d < r){
                low = mid;
            }
            else{
                up = mid;
            }
        }
        num = 1;
        px1 = x1 + mid * (x2 - x1);
        py1 = y1 + mid * (y2 - y1);
        return true;
    }
    else {
        if (dist(x2, y2, xr, yr) < r){
            return intersect(x2, y2, x1, y1, xr, yr, r, num, px1, py1, px2, py2);
        }
        if (((xr - x1) * (xr - x2) + (yr - y1) * (yr - y2)) > EPS) return false;
        d = fabs(((x2 - x1) * (yr - y1) - (xr - x1) * (y2 - y1))) / dist(x1, y1, x2, y2);
        if (d > r + EPS) return false;
        d2 = sqrt((xr - x1) * (xr - x1) + (yr - y1) * (yr - y1) - d * d);
        double sx = x1 + d2 / dist(x1, y1, x2, y2) * (x2 - x1);
        double sy = y1 + d2 / dist(x1, y1, x2, y2) * (y2 - y1);
        px1 = sx + sqrt(r * r - d * d) / dist(sx, sy, x1, y1) * (x1 - sx);
        py1 = sy + sqrt(r * r - d * d) / dist(sx, sy, x1, y1) * (y1 - sy);
        px2 = sx + sqrt(r * r - d * d) / dist(sx, sy, x2, y2) * (x2 - sx);
        py2 = sy + sqrt(r * r - d * d) / dist(sx, sy, x2, y2) * (y2 - sy);
        num = 2;
        return true;
    }
}

bool intersect(double x1, double y1, double x2, double y2, double xr, double yr, double r){
    double low, up, mid, d, d2;
    if (dist(x1, y1, xr, yr) < r){
        if (dist(x2, y2, xr, yr) < r - EPS) return false;
        return true;
    }
    else {
        if (dist(x2, y2, xr, yr) < r){
            return true;
        }
        if (((xr - x1) * (xr - x2) + (yr - y1) * (yr - y2)) > EPS) return false;
        d = fabs(((x2 - x1) * (yr - y1) - (xr - x1) * (y2 - y1))) / dist(x1, y1, x2, y2);
        if (d > r + EPS) return false;
        return true;
    }
}

double trianglearea(double x1, double y1, double x2, double y2, double x3, double y3){
    return fabs((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / 2;
}

double sector(double x1, double y1, double x2, double y2, double xr, double yr, double r){
    double alpha;
    alpha = acos(((x1 - xr) * (x2 - xr) + (y1 - yr) * (y2 - yr)) / (dist(x1, y1, xr, yr) * dist(x2, y2, xr, yr)));
    return alpha * r * r / 2;
}

//正方形和圆相交面积 
double getarea(double x, double y, double len, double xr, double yr, double r){
    bool bo[4], adj = false;
    int i;
    int num = 0;
    const int dx[] = {-1, -1, 1, 1, -1, -1, 1, 1};
    const int dy[] = {-1, 1, 1, -1, -1, 1, 1, -1};
    for (i = 0; i < 4; i++){
        bo[i] = intersect(x + dx[i] * len / 2, y + dy[i] * len / 2, x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, r);
        num += bo[i];
    }
    for (i = 0; i < 4; ++i){
        if (bo[i] && bo[(i + 1) % 4]) adj = true;
    }
    
    if (num == 0) return len * len;
    if (num == 2){
        double px1, py1, px2, py2, tmpx, tmpy;
        if (adj){
        //    //printf("1\n");
            double res;
            for (i = 0; i < 4; ++i){
                if (bo[i] && bo[(i + 1) % 4]) break;
            }
            if (false == intersect(x + dx[i] * len / 2, y + dy[i] * len / 2, x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, r, num, px1, py1, tmpx, tmpy)){
                //printf("error\n");
            }
            if (false == intersect(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, x + dx[i + 2] * len / 2, y + dy[i + 2] * len / 2, xr, yr, r, num, px2, py2, tmpx, tmpy)){
                //printf("error\n");
            }
            //printf("px1 = %lf py1 = %lf px2 = %lf py2 = %lf\n", px1, py1, px2, py2);
  //          //printf("i = %d\n", i);
    //        //printf("%lf %lf\n", x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2);
            //printf("dist = %lf %lf\n", dist(px1,py1,0,0), dist(px2, py2, 0, 0));
            //printf("sec = %lf tri = %lf tri = %lf\n", sector(px1, py1, px2, py2, xr, yr, r), trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px1, py1), trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px2, py2));
            if (dist(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr) > r){
                res = sector(px1, py1, px2, py2, xr, yr, r)
                - trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px1, py1)
                - trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px2, py2) + len * len;
            }
            else {
                res = sector(px1, py1, px2, py2, xr, yr, r)
                - trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px1, py1)
                - trianglearea(x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, px2, py2);
            }
            //printf("%lf\n", res);
            return res;
        }
        else {
      //      //printf("0\n");
            double res;
            for (i = 0; i < 4; ++i){
                if (bo[i]) break;
            }
            if (false == intersect(x + dx[i] * len / 2, y + dy[i] * len / 2, x + dx[i + 1] * len / 2, y + dy[i + 1] * len / 2, xr, yr, r, num, px1, py1, tmpx, tmpy)){
                //printf("error\n");
            }
            if (false == intersect(x + dx[i + 2] * len / 2, y + dy[i + 2] * len / 2, x + dx[i + 3] * len / 2, y + dy[i + 3] * len / 2, xr, yr, r, num, px2, py2, tmpx, tmpy)){
                //printf("error\n");
            }
            if (dist(x + dx[i] * len / 2, y + dy[i] * len / 2, xr, yr) > r || dist(x + dx[i + 3] * len / 2, y + dy[i + 3] * len / 2, xr, yr) > r){
                //printf("error");
                system("pause");
            }
            res = (dist(px1, py1, x + dx[i] * len / 2, y + dy[i] * len / 2) + dist(px2, py2, x + dx[i + 3] * len / 2, y + dy[i + 3] * len / 2)) * len / 2;
            res += sector(px1, py1, px2, py2, xr, yr, r) - trianglearea(px1, py1, px2, py2, xr, yr);
            //printf("sec - tri = %lf\n", sector(px1, py1, px2, py2, xr, yr, r) - trianglearea(px1, py1, px2, py2, xr, yr));
            //printf("px1 = %lf py1 = %lf px2 = %lf py2 = %lf\n", px1, py1, px2, py2);
            //printf("dist = %lf %lf\n", dist(px1,py1,0,0), dist(px2, py2, 0, 0));
            //printf("%lf\n",res);
            return res;
        }
    }
    //printf("num = %d, error\n", num);
    system("pause");
}

double solve(double f, double R, double t, double r, double g){
    double sum = 0, x = r + g / 2, y = r + g / 2, x0 = r, y0 = r, res;
    double r0 = R - t - f, len = g - 2 * f, r02 = r0 * r0;
    int count = 0;
    if (r0 < EPS) return 1;
    if (len < EPS) return 1;
    x = r + g / 2;
    x0 = x - len / 2;;
    while (x0 < r0){
        y = r + g / 2;
        y0 = y - len / 2;
        while (x0 * x0 + y0 * y0 < r02){

            res = getarea(x, y, len, 0, 0, r0);
            if (fabs(res - len * len) < EPS) count++;
            else {
                 sum += res;
                 //printf("x = %lf y = %lf res = %lf \n", x, y, res);
            }
            y += g + 2 * r;
            y0 = y - len / 2;
        }
        x += g + r * 2;
        x0 = x - len / 2;
    }
    sum += count * len * len;
    //printf("%lf %lf %lf %lf\n", r0, r, len, sum);
    return 1 - 4 * sum / (acos(-1) * R * R);
}

int main(){
    double f, R, t, r, g;
    int n, N;
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &N);
    for (n = 1; n <= N; ++n){
        scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
        printf("Case #%d: %.6lf\n", n, solve(f, R, t, r, g));
    }
    return 0;
}
