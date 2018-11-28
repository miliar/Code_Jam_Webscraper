#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define erro 1e-12
#define igual(X,Y) ( fabs((X) - (Y)) < erro)

struct X {
    int t;
    int f;
};

vector<X> v[100];

int main() {
    int N;
    scanf("%d" , &N);
    for(int I = 1; I <= N ; I++) {
        int i,n,m,t,j;
        X aux;
        scanf("%d %d" , &n, &m);
        for(i=0;i<m;i++) 
            v[i].clear();
        for(i=0;i<m;i++) {
            scanf("%d" , &t);
            for(j=0;j<t;j++) {
                scanf("%d %d" , &aux.t , &aux.f);
                aux.t -= 1;
                v[i].push_back(aux);
            }
        }

        int pode;
        int k;

            
        int vec[10];


vi R;
R.clear();
int tenho = -1;


        for(i=0;i<=(1<<n);i++) {
            pode = 1;

            int tmp = i;
            for(int l = 0; l<n;l++) {
                vec[l] = tmp%2;
                tmp/=2;
            }

            for(j=0;j<m && pode;j++) {
                for(k=0;k<(int)v[j].size();k++) {
//                    int se = (i ^ (1<< (v[j][k].t)));

  //                  printf("OU de %d com %d = %d\n" , i , (1<< (v[j][k].t)) , se );

                    //se &= i;
    /*                if(se != 0) 
                        se/=se;

                    if( se != v[j][k].f )    
                        break;*/
                    if(vec[v[j][k].t] == v[j][k].f)
                        break;
                }
                if(k == (int) v[j].size()) {
//                    printf("com i = %d nao deu para o customer %d\n" , i , j);
                    pode  = 0;
                }
            }
            if(pode) {
                vi AUX;
                int aiai = 0;
                for(int p = 0; p<n;p++) {
                    AUX.push_back(vec[p]);                
                    if(vec[p]) aiai++;
                }
                    if(R.empty()) {
                        R = AUX;
                        tenho = aiai;
                    }
                    else if(aiai < tenho) {
                        R = AUX;
                        tenho = aiai;
                    }
            }
        }
        printf("Case #%d: " , I);
        if(R.empty()) printf("IMPOSSIBLE\n");
        else {
            for(j=0 ; j< (int)R.size();j++) {
                printf("%d " , R[j]);                
            }
            printf("\n");
        }
    }
    return 0;
}

