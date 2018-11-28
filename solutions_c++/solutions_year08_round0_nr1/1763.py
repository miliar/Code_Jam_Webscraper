#include <iostream>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include<fstream>
using namespace std;

typedef vector <int> vi;
typedef vector<vi> vvi;
typedef vector <string> vs;
typedef vector<vs> vvs;
typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int> pii;

istringstream din;
ostringstream dout;

ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");

int dx[8] = {-1,0,1, 0,-1,-1,1,1};
int dy[8] = { 0,1,0,-1,-1, 1,1,-1};

int dirx[4] = {0, 1, 0, -1};
int diry[4] = {1, 0, -1, 0};

int N,S,Q;
int MAXINT = 1000000;
vs eng;
vs que;
int cnt[100][100];
int nxt[100];

void init()
{
    eng.clear();que.clear();
    for (int i = 0;i < 100;i++) {
        for (int j = 0;j < 100;j++)
            cnt[i][j] = MAXINT;
        nxt[i] = -1;
    }
}

int dyn()
{
    int res = MAXINT*2;
    for (int i = 0;i < S;i++) {
        if (eng[i] != que[Q-1])
            cnt[i][Q-1] = 0;
        else
            cnt[i][Q-1] = 1;
    }
    int id;
    for (int j = Q-2;j > 0;j--) {
        for (int i = 0;i < S;i++) {
            //cerr << "query : " << que[j] << endl;
            if (eng[i].compare(que[j]) == 0) { 
                int tmp = MAXINT*2;
                id = -1;
                for (int k = 0;k < S;k++) {
                    if (k == i) continue;
                    if (tmp > cnt[k][j+1]) {
                        id = k;
                        tmp = min(tmp,cnt[k][j+1]);
                    }
                }
                nxt[j] = id;
                cnt[i][j] = tmp+1;
            }else {
                cnt[i][j] = cnt[i][j+1];
            }
        }
    }
    //cerr << "here" << endl;
    for (int i = 0;i < S;i++) {
        if (eng[i].compare(que[0]) != 0) {
            id = -1;
            for (int k = 0;k < S;k++) {
                if (k == i) {
                    cnt[i][0] = min(cnt[i][0],cnt[i][1]);
                }
                else {
                    cnt[i][0] = min(cnt[i][0],cnt[i][1]+1);
                }
            }
            res = min(cnt[i][0],res);
        } 
    }
    //cerr << "here2" << endl;
/*
    for (int i = 0;i < S;i++) {
        for (int j = 0;j < Q;j++)
            //cerr << cnt[i][j] << " ";
        //cerr << endl;
    }
*/
    return res;
}
string toUpper(string);
int main()
{
    string str;
        
    fin >> N;
    cerr << "N = " << N << endl;
    for (int i = 0;i < N;i++) {
        cerr << i << " case" << endl;
        init();
        
        fin >> S;
        cerr << "S = " << S << endl;
        getline(fin,str);
        for (int j = 0;j < S;j++) {
            getline(fin,str);
            str = toUpper(str);
            eng.push_back(str);
            //cerr << str << endl;
        }
        fin >> Q;
        cerr << "Q = " << Q << endl;
        getline(fin,str);
        for (int j = 0;j < Q;j++) {
            getline(fin,str);
            str = toUpper(str);
            que.push_back(str);
            //cerr << str << endl;
        }
        int res = (Q == 0 ? 0 : dyn());
        fout << "Case #" << (i+1) << ": " << res << endl;
        
        //for (int j = 0;j < Q;j++)
            //cerr << "next#" << j << " : " << nxt[j] << endl;
    }
    fin.close();
    fout.close();
    //cerr << "here3" << endl;
    return 0;
}

string toUpper(string str) {
    string res = "";
    for (int i = 0;i < str.length();i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            res += (str[i]-'a' + 'A');
        }else {
            res += str[i];
        }
    }
    return res;
}

