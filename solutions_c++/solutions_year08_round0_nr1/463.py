#include <stdio.h>
#include <map>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef map<string, int> ms;
typedef vector<int> vi;
typedef set<int> si;

#define FOR(i,f,t) for(int i=f; i<t; ++i)
#define REP(i,n) for(int i=0; i<n; ++i)

char engine[110];
char query[110];

ms ens;
vi qs;

int main(){
    int k;
    FILE* f=fopen("test.txt", "r");
    FILE* fo=fopen("test_out.txt", "w+");
    fscanf(f, "%d", &k);
    REP(i,k){
        int s, t;
        fscanf(f, "%d\n", &s);
        REP(j,s){
            fgets(engine, sizeof(engine), f);
            t=strlen(engine);
            if(engine[t-1]=='\n') engine[t-1]='\0';
            ens[string(engine)]=j;
        }
        int q;
        fscanf(f, "%d\n", &q);
        qs.resize(q);
        REP(j,q){
            fgets(query, sizeof(query), f);
            t=strlen(query);
            if(query[t-1]=='\n') query[t-1]='\0';
            qs[j]=ens[string(query)];
        }
        si found;
        int res=0;
        REP(j,q){
            if (found.find(qs[j])==found.end()){
                if (found.size() < s-1){
                    found.insert(qs[j]);
                } else {
                    // qs[i] - is the least engine (others was found earlier)
                    // here we change
                    ++res;
                    found.clear();
                    // forbid to switch to this engine next time
                    found.insert(qs[j]);
                }
            }
        }
        fprintf(fo, "Case #%d: %d\n", i+1, res);
    }
    return 0;
}
