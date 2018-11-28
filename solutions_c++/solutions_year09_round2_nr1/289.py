#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iomanip>
using namespace std;

#define SZ size()
#define PB push_back
#define B begin()
#define E end()
#define SORT(a) sort((a).B, (a).E)
#define REV(a) reverse((a).B, (a).E)
#define UNQ(a) (a).resize(unique((a).B, (a).E) - (a).B)
#define SUM(a) accumulate((a).B, (a).E, 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.B) i = a.B; i != a.E; i++)

struct node
{
    string feature;
    int yes, no;
    double weight;
};

node tree[200];
int L, A, len;
string s, S;
set<string> animal;

double get(int ind, double prob)
{
    prob *= tree[ind].weight;
    if(tree[ind].feature == "NONE"){
        return prob;
    }
    if(animal.find(tree[ind].feature) != animal.E){
        return get(tree[ind].yes, prob);
    }
    else{
        return get(tree[ind].no, prob);
    }
}

double toDouble(string d)
{
    int x = 0, p = 1;
    FOR(i, 0, d.SZ){
        if(d[i] == '.'){
            FOR(j, 0, d.SZ - i - 1){
                p *= 10;
            }
            continue;
        }
        x *= 10;
        x += d[i] - '0';
    }
    return x / (double)p;
}

void build(int l, int r, int ind)
{
    tree[ind].yes = tree[ind].no = -1;
    string w = "";
    int i = l;
    while(S[i] == ' '){
        i++;
    }
    while(S[i] != ' ' && S[i] != ')'){
        w += S[i++];
    }
    tree[ind].weight = toDouble(w);
    while(S[i] == ' '){
        i++;
    }
    if(S[i] == ')'){
        tree[ind].yes = tree[ind].no = -1;
        tree[ind].feature = "NONE";
    }
    else{
        tree[ind].feature = "";
        while(S[i] >= 'a' && S[i] <= 'z'){
            tree[ind].feature += S[i++];
        }
        int tl, cnt = 0;
        while(i <= r){
            if(S[i] == '('){
                if(!cnt){
                    tl = i + 1;
                }
                cnt++;
            }
            if(S[i] == ')'){
                cnt--;
                if(!cnt){
                    if(tree[ind].yes == -1){
                        tree[ind].yes = ++len;
                    }
                    else{
                        tree[ind].no = ++len;
                    }
                    build(tl, i - 1, len);
                }
            }
            i++;
        }
    }
    //cout << ind << ": " << tree[ind].feature << " " << tree[ind].weight << " " << tree[ind].yes << " " << tree[ind].no << endl;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int testCnt;
    fin >> testCnt;
    for(int test = 1; test <= testCnt; test++){
        fout << "Case #" << test << ":" << endl;
        fin >> L;
        getline(fin, s);
        len = 0;
        S = "";
        FOR(i, 0, L){
            getline(fin, s);
            S += s;
        }
        build(1, S.SZ - 2, 0);
        fin >> A;
        getline(fin, s);
        FOR(i, 0, A){
            fin >> s;
            int N;
            animal = set<string>();
            fin >> N;
            FOR(j, 0, N){
                fin >> s;
                animal.insert(s);
            }
            fout.setf(ios::fixed);
            fout << setprecision(7) << get(0, 1.) << endl;
        }
    }
}
