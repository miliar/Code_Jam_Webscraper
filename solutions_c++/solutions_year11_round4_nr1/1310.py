#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

namespace
{
}
struct Walkway{
    int B, E, w;
};
bool operator<(const Walkway &a, const Walkway &b){
    return a.w<b.w;
}

int main()
{
    int T;
    cin >> T;
    REP(i, T){
        int X, S, R, t, N;
        double totalTime=0;
        cin >> X >> S >> R >> t >> N;

        int curPos=0;
        double runTime=0;
        vector<Walkway> w;
        REP(j, N){
            Walkway way;
            cin >> way.B >> way.E >> way.w;
            if(curPos!=way.B){
                Walkway way2={curPos, way.B, 0};
                w.push_back(way2);
            }
            w.push_back(way);
            curPos=way.E;
        }
        if(curPos!=X){
            Walkway way2={curPos, X, 0};
            w.push_back(way2);
        }
        
        sort(w.begin(), w.end());
        FOR(it, w){
            //cout << it->E << ", " << it->B << ", " << it->w << endl;
            double t2=((double)(it->E-it->B)/(R+it->w));
            if(runTime+t2>t){
                t2=(((double)it->E-it->B-(R+it->w)*(t-runTime))/(S+it->w)+(t-runTime));
                runTime=t;
                totalTime+=t2;
                //cout << "run+walk" << t2 << endl;
            }else{
                runTime+=t2;
                totalTime+=t2;
                //cout << "run" << t2 << endl;
            }
        }
        /*
        totalTime=(double)X/S; // 全部歩いた場合
        if(totalTime>=t){
            // 走った分短縮される時間
            totalTime-=(t*(R-S));
        }else{
            totalTime-=(totalTime*(R-S));
        }
        */
/*
        REP(j, N){
            int B, E, w;
            cin >> B >> E >> w;
            if(curPos!=B){
                double t2=((double)(B-curPos)/R);
                if(runTime+t2>t){
                    t2=(((double)B-curPos-R*(t-runTime))/S)+(t-runTime);
                    runTime=t;
                    totalTime+=t2;
                    curPos=B;
                    //cout << "run+walk" << t2 << endl;
                }else{
                    runTime+=t2;
                    totalTime+=t2;
                    curPos=B;
                    //cout << "run" << t2 << endl;
                }
            }
            {
                double t2=((double)(E-B)/(R+w));
                if(runTime+t2>t){
                    //cout << runTime << ", " << t2 << ", " << t << endl;
                    t2=(((double)E-B-(R+w)*(t-runTime))/(S+w))+(t-runTime);
                    //cout << R*(t-runTime) << endl;
                    runTime=t;
                    totalTime+=t2;
                    curPos=E;
                    //cout << "run+walk+autowalk" << t2 << endl;
                }else{
                    runTime+=t2;
                    totalTime+=t2;
                    curPos=E;
                    //cout << "run+autowalk" << t2 << endl;
                }
            }
            //totalTime-=((E-B)/w);
        }
        if(curPos!=X){
            {
                double t2=((double)(X-curPos)/R);
                if(runTime+t2>t){
                    t2=(((double)X-curPos-R*(t-runTime))/(S))+(t-runTime);
                    runTime=t;
                    totalTime+=t2;
                    curPos=X;
                    //cout << t2 << endl;
                }else{
                    runTime+=t2;
                    totalTime+=t2;
                    curPos=X;
                    //cout << t2 << endl;
                }
            }
        }
*/
        printf("Case #%d: %.07f\n", (i+1), totalTime);
    }
    return 0;
}
