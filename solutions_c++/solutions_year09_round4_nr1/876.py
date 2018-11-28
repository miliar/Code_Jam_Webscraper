#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>

using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef long long LL;



int last1(string s){
    int sol=0;
    REPSZ(i,s) if(s[i]=='1') sol = i;
    return sol;
}
struct Node{
    vector<int> v;
    int pasos;
};

bool vale(vector<int> v){
    REPSZ(i,v){
        if(v[i]>i) return false;
    }
    return true;
}
map<vector<int>, bool> visited;
int bfs(vector<int> val){
    queue<Node > q;
    Node ini;
    ini.v=val;
    ini.pasos = 0;
    q.push(ini);
    visited.clear();
    while(!q.empty()){
        Node node = q.front();
        q.pop();
        vector<int> w = node.v;
        if(vale(node.v)) return node.pasos;
        if(visited.find(node.v)!=visited.end()) continue;
        visited[node.v]=true;
        REP(i,SZ(node.v)-1){
            vector<int> wi=node.v;
            int aux = wi[i];
            wi[i]=wi[i+1];
            wi[i+1]=aux;
            if(visited.find(wi)==visited.end()) {
            Node nue;
            nue.v = wi;
            nue.pasos = node.pasos+1;
            q.push(nue);
            }
        }
    }
    return -1;
}

void run1(int caso){

int N;
cin >>N;
string s;
vector<int> val;
REP(i,N){
    cin >> s;
    val.push_back(last1(s));
}



	int sol=bfs(val);

	cout << "Case #"<<caso<<": "<< sol<<endl;
}



void run2(int caso){

int N;
cin >>N;
string s;
vector<int> val;
REP(i,N){
    cin >> s;
    val.push_back(last1(s));
}



	int sol=0;

    while(!vale(val)){
        REP(i,SZ(val)-1){
            if(val[i]>i){
                vector<int> pos;
                FORE(j,i+1,SZ(val)){
                    if(val[j]<=i){
                        pos.push_back(j);
                        break;
                    }
                }
                int valor = val[pos[0]];
                val.erase(val.begin()+pos[0]);
                val.insert(val.begin()+i,valor);
                sol+=(pos[0]-i);
            }
        }
    }


	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run2(i);
	return 0;
}
