#include<iostream>
#include<stdio.h>
#include<set>
#include<string.h>
#include<vector>
using namespace std;
typedef long long LL;
int t,txt,a,b,n,tot;
#define S 2000005
char ch[10];
//vector<int>V[S];
set<int>V[S];
int main(){
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int i = 1; i < S; ++i){
	    memset(ch, 0, sizeof ch);
        sprintf(ch,"%d",i);
        for(int j = 1; ch[j]; ++j){
            int num = 0;
            for(int k = j; ch[k]; ++k)num = num * 10 + (ch[k] - '0');
            for(int k = 0; k < j; ++k)num = num * 10 + (ch[k] - '0');
            //V[i].push_back(num);
            V[i].insert(num);
        }
	}
	while(t--){
	    scanf("%d%d",&a,&b);
	    //memset(used, 0, sizeof used);
	    tot = 0;
	    for(int i = a; i <= b; ++i){
	        set<int>::iterator it = V[i].begin();
            for(;it != V[i].end(); it++){
                int num = *it;
                if(num < a || num > b)continue;
                if(num <= i)continue;
                tot++;
            }
	    }
	    printf("Case #%d: %d\n",++txt,tot);
	}
    return 0;
}
