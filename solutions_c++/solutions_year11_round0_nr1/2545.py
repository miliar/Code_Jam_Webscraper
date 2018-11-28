#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#define pb(x) push_back(x)
using namespace std;

vector<char> order;
vector<int> o,b;

int main(){
        int n,t,cnt=1;
        scanf("%d", &t);
        while(t--){
                order.clear(); o.clear(); b.clear();
                scanf("%d", &n);
                char c;
                int p;
                for(int i=0; i<n;i++){
                        scanf(" %c %d",&c,&p);
                        order.pb(c);
                        if(c=='O') o.pb(p);
                        else if(c=='B') b.pb(p);
                }
                int orderp=0,op=0,bp=0,ans=0,roboto=1,robotb=1;
                while(orderp < order.size()){
                        int s = 0;
                        if(op < o.size()){
                                if(roboto == o[op] && order[orderp]=='O') {op++;s=1;}
                                else if(roboto < o[op]){roboto++;}
                                else if(roboto > o[op]){roboto--;}
                        }
                        if(bp < b.size()){
                                if(robotb== b[bp] && order[orderp]=='B'){bp++;s=1;}
                                else if(robotb < b[bp]) {robotb++;}
                                else if(robotb > b[bp]){robotb--;}
                        }
                        if(s) orderp++;
                        ans++;
                }
                printf("Case #%d: %d\n", cnt++,ans);
        }
        return 0;
}
