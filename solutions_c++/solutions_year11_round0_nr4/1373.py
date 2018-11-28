#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    //freopen("entrada.in","r",stdin);
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int ic,casos,elem,n,i;
    float hit;
    vector<int> elementos;
    vector<int> original;
    ic=1;
    scanf("%d ",&casos);
    while(casos--){
        scanf("%d ",&n);
        for(i=0;i<n;i++){
            scanf("%d ",&elem);
            elementos.push_back(elem);
            original.push_back(elem);
        }
        stable_sort(elementos.begin(),elementos.end());
        hit=0.0;
        for(i=0;i<original.size();i++){
            if(original[i]!=elementos[i]) hit++;
        }
        printf("Case #%d: %.6f\n",ic,hit);
        elementos.clear();
        original.clear();
        ic++;
    }
    return 0;
}
