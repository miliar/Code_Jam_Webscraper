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
    for(int i=0;i<cases;i++){
        int n,b,posO=1,posB=1,res=0,aux=0; char r; bool w=true;
        scanf("%d",&n);
        for(int j=0;j<n;j++){
            scanf(" %c",&r);
            scanf(" %d",&b);
            if(r == 'O'){
                if(!w){
                    if(b > posO)
                        posO = min(posO+aux,b);
                    else
                        posO = max(posO-aux,b);
                    aux = abs(posO-b)+1;
                    res+= aux;
                    posO=b;
                }else{
                    aux+= abs(posO-b)+1;
                    res+= abs(posO-b)+1;
                    posO=b;
                }
                w = true;
            }else{
                if(w){
                    if(b > posB)
                        posB = min(posB+aux,b);
                    else
                        posB = max(posB-aux,b);
                    aux = abs(posB-b)+1;
                    res+=aux;
                    posB=b;
                }else{
                    aux+= abs(posB-b)+1;
                    res+= abs(posB-b)+1;
                    posB=b;
                }
                w = false;
            }
        }
        printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}