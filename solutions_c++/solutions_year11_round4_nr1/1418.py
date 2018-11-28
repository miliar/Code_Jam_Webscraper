/*
 * Author: NomadThanatos
 * Created Time:  2011/6/4 22:20:20
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())

const int MAXINT = -1u>>1;
const int MAXN = 5000;
const double EPS = 1e-9;

int X,S,N,R;
double ti;

int sgn(const double &x) {return (int)((x > EPS) - (x < -EPS));}

struct Way {
    int L,R,sp;
    double len;
    Way(int _L,int _R,int _sp) :
        L(_L),R(_R),sp(_sp) {
            len = R - L;
        };
    Way() {};
    void input() {
        scanf("%d%d%d",&L,&R,&sp);
        len = R - L;
        sp += S;
    }
}tmp[MAXN],way[MAXN];

//vector<Way> way;

bool cmp1st(const Way &A,const Way &B){
    return A.L < B.L;
}

bool cmp2nd(const Way &S1,const Way &S2){
    //return sgn((S1.sp * S1.sp + S1.sp * R) * S2.len - (S2.sp * S2.sp + S2.sp * R) * S1.len) == 1;
    return S1.sp < S2.sp;
}

int main() {
    freopen("A.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        //way.clear();
        scanf("%d%d%d%lf%d",&X,&S,&R,&ti,&N);
        R -= S;
        int NN = 2 * N + 1;
        for(int i = 0 ; i < N ; i++) {
            tmp[i].input();
        }
        sort(tmp,tmp + N,cmp1st);
        int back = 0;
        for(int i = 0 ; i < N ; i++) {
            if (i > 0) back = tmp[i - 1].R;
            way[i * 2] = Way(back,tmp[i].L,S);
            //if (sgn(tmp[i].L - back) > 0) {
                //way.push_back(Way(back,tmp[i].L,S));
            //}
            way[i * 2 + 1] = tmp[i];
            //way.push_back(tmp[i]);
        }
        way[2 * N] = Way(tmp[N - 1].R,X,S);
        //sort(way.begin(),way.end(),cmp2nd);
        sort(way,way + NN,cmp2nd);
        double res = 0.0;
        for(int i = 0 ; i < NN ; i++) {
            //printf("%d %d %d %d %d\n",way[i].L,way[i].R,way[i].sp,R,S);
            double tmp = double(way[i].R - way[i].L) / (way[i].sp + R);
            //double tmp = double(way[i].R - way[i].L) / (way[i].sp);
            if (sgn(tmp - ti) > 0) {
                //printf("%lf %lf\n",tmp,ti);
                res += ti;
                tmp = double(way[i].R - way[i].L - (way[i].sp + R) * ti) / (way[i].sp);
                res += tmp;
                ti = 0.0;
            }
            else {
                ti -= tmp;
                res += tmp;
            }
        }
        //while(way.size() > 0) {
            //Way fst,snd;
            //fst = way.back();
            //way.pop_back();
            //if (way.size() > 0) {
                //snd = way.back();
                //way.pop_back();
                //double tmplen = fst.len - (fst.sp * fst.sp + fst.sp + R) * snd.len / (snd.sp * snd.sp + snd.sp + R);
                //double tmp = tmplen / (fst.sp + R);
                //double tmp = way[i].len / (way[i].sp + R);
                //if (sgn(tmp - ti) > 0) {
                    //printf("%lf %lf\n",tmp,ti);
                    //res += ti;
                    //fst.len -= ti * fst.sp + R;
                    //ti = 0.0;
                //}
                //else {
                    //ti -= tmp;
                    //res += tmp;
                //}
            //}
            //else {
                //double tmp = way[i].len / (way[i].sp + R);
                //if (sgn(tmp - ti) > 0) {
                    //printf("%lf %lf\n",tmp,ti);
                    //res += ti;
                    //tmp = double(way[i].R - way[i].L - (way[i].sp + R) * ti) / (way[i].sp);
                    //res += tmp;
                    //ti = 0.0;
                //}
                //else {
                    //ti -= tmp;
                    //res += tmp;
                //}
            //}

        //}
        //if (ti > 0) printf("%d\n",t + 1);
        printf("Case #%d: %0.12lf\n",t + 1,res);
    }
    return 0;
}

