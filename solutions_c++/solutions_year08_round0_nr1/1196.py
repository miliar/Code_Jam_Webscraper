#include<stdio.h>
#include<string.h>
#include<string>
#include<map>
#include<vector>
using namespace std;

int ile, s, q;
int cnum, ret, nseen;
int seen[102];
char ch;
string tmp;
map<string,int> amap;
vector<string> query;

int main() {
    scanf("%d",&ile);
    for(int z=0;z<ile;z++) {        
        ret = 0; cnum = 1;
        amap.clear();
        query.clear();
        scanf("%d",&s);
        scanf("%c",&ch);
        for(int i=0;i<s;i++) {            
            tmp = "";
            while(scanf("%c",&ch)) {
                if(ch == '\n') break;
                tmp += ch;
            }
            amap[tmp] = cnum++;
        }        
        scanf("%d",&q);
        scanf("%c",&ch);       
        for(int i=0;i<q;i++) {
            tmp = "";
            while(scanf("%c",&ch) == 1) {
                if(ch == '\n') break;
                tmp += ch;
            }            
            query.push_back(tmp);          
        }        
        memset(seen,0,sizeof(seen));
        nseen = 0;
        for(int i=0;i<q;i++) {
            if(seen[amap[query[i]]] == 0) {
                seen[amap[query[i]]] = 1;
                nseen++;
                if(nseen == s) {
                    ret++;
                    i--;
                    nseen = 0;
                    memset(seen,0,sizeof(seen));
                }
            }
        }
        printf("Case #%d: %d\n",z+1,ret);        
    }
}
