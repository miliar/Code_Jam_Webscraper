#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int L, D, N, it;
    string s, a;
    vector<string> vs;
    vector<string>::iterator it1;
    scanf("%d%d%d",&L,&D,&N);
    F(i,D){
        cin>>s;
        vs.PB(s);
    }
    F(qwe,N){
        cin>>s;
        set<string> aux(ALL(vs));
        it = 0;
        int posi = 0;
        while(posi < L){
            vector<string> palabras(ALL(aux));
            aux.clear();
            if(s[it] == '('){
                it++;
                while(s[it]!=')'){
                    F(j,palabras.S){
                        a = palabras[j];
                        if(a[posi] == s[it]){
                            aux.insert(a);
                        }
                    }
                    it++;
                }
                it++;
            }
            else{
                F(j,palabras.S){
                    a = palabras[j];
                    if(a[posi] == s[it]){
                        aux.insert(a);
                    }
                }
                it++;
            }
            posi++;
        }
        printf("Case #%d: %d\n",qwe+1,aux.S);
    }
    fclose(stdout);
    //system("pause");
    return 0;
}
