#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define inf 0x3f3f3f3f
using namespace std;

#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}

int main(){
    int cases;
    scanf("%d",&cases);
    for(int ncase=0;ncase<cases;ncase++){
        int C,D,N; char buffer[200]; string buff;
        scanf("%d",&C);
        vector<pair<string,string>> comb(C);
        for(int i=0;i<C;i++){
            scanf(" %s",buffer);
            buff = buffer;
            comb[i].first = buff.substr(0,2);
            comb[i].second = buff[2];
        }
        scanf("%d",&D);
        vector<string> opp(D);
        for(int i=0;i<D;i++){
            scanf(" %s",buffer);
            opp[i] = buffer;
        }
        scanf("%d %s",&N,buffer);
        string lista,rev;
        buff = buffer;
        size_t found,found2;
        for(int i=0;i<N;i++){
            lista.push_back(buff[i]);
            for(int j=0;j<C;j++){
                found = lista.find(comb[j].first);
                if(found != string::npos)
                    lista.replace(found,comb[j].first.size(),comb[j].second);
                else{
                    rev = comb[j].first;
                    reverse(all(rev));
                    found = lista.find(rev);
                    if(found != string::npos)
                        lista.replace(found,comb[j].first.size(),comb[j].second);
                }
            }
            for(int j=0;j<D;j++){
                found = lista.find(opp[j][0]);
                found2 = lista.find(opp[j][1]);
                if(found != string::npos && found2 != string::npos)
                    lista.clear();
            }
        }
        printf("Case #%d: [",ncase+1);
        for(int i=0,w=lista.size();i<w;i++)
            if(i==0)
                printf("%c",lista[i]);
            else
                printf(", %c",lista[i]);
        printf("]\n");

    }
    return 0;
}