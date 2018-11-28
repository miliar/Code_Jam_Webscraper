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

double CalcWp(vector<char> &v)
{
/*
    FOR(it, v){
        cout << (*it) << ", ";
    }
    cout << endl;
*/
    int win=0, total=0;
    FOR(it, v){
        switch(*it){
        case '1':
            win++;
            total++;
            break;
        case '0':
            total++;
            break;
        case '.':
        default:
            break;
        }
    }
/*
    cout << win << ", " << total << endl;
    cout << (double)win/(double)total << endl;
*/
    return (double)win/(double)total;
}
double CalcWp(vector<char> &v, int ignoreIndex)
{
    int win=0, total=0;
    int index=0;
    FOR(it, v){
        if(index==ignoreIndex){
            index++;
            continue;
        }
        switch(*it){
        case '1':
            win++;
            total++;
            break;
        case '0':
            total++;
            break;
        case '.':
        default:
            break;
        }
        index++;
    }
    return (double)win/(double)total;

}

int main()
{
    int T;
    cin >> T;
    REP(i, T){
        int N;
        cin >> N;
        vector<vector<char> > v(N);
        REP(j, N){
            REP(k, N){
                char c;
                cin >> c;
                v[j].push_back(c);
            }
            cin.ignore();
        }
/*
        REP(j, N){
            REP(k, N){
                cout << v[j][k] << ", ";
            }
            cout << endl;
        }
*/
        vector<double> wp(N);
        REP(j, N){
            wp[j]=CalcWp(v[j]);
        }
        vector<double> owp(N);
        REP(j, N){
            int total=0;
            double wpsum=0;
            REP(k, N){
                if(v[j][k]!='.'){
                    wpsum+=CalcWp(v[k], j);
                    total++;
                }
            }
            owp[j]=wpsum/(double)total;
        }
        vector<double> oowp(N);
        REP(j, N){
            int total=0;
            double owpsum=0;
            REP(k, N){
                if(v[j][k]!='.'){
                    owpsum+=owp[k];
                    total++;
                }
            }
            oowp[j]=owpsum/(double)total;
        }
/*
        REP(j, N){
            cout << wp[j] << ", " << owp[j] << ", " << oowp[j] << endl;
        }
*/
        cout << "Case #" << (i+1) << ":" << endl;
        REP(j, N){
            printf("%.12f\n", (0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]));
        }
    }
    return 0;
}
