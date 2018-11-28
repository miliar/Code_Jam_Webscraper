#include <cstdio>
#include <cstring>
#include <utility>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        int c,d,n;
        char co[26][26]={};
        char op[26][26]={};
        scanf("%d",&c);
        for(int i=0;i<c;i++){
            char s[100];
            scanf("%s",s);
            co[s[0]-'A'][s[1]-'A']=s[2];
            co[s[1]-'A'][s[0]-'A']=s[2];
        }
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            char s[100];
            scanf("%s",s);
            op[s[0]-'A'][s[1]-'A']=1;
            op[s[1]-'A'][s[0]-'A']=1;
        }
        char s[500];
        scanf("%d",&n);
        scanf("%s",s);
        vector<char> u;
        for(int i=0;i<n;i++){
            u.push_back(s[i]);
            if(u.size()>=2 && co[u[u.size()-2]-'A'][u[u.size()-1]-'A']){
                s[i--]=co[u[u.size()-2]-'A'][u[u.size()-1]-'A'];
                u.pop_back();
                u.pop_back();
                continue;
            }
            for(int j=0;j<int(u.size())-1;j++)
                if(op[u.back()-'A'][u[j]-'A']) u.clear();
        }
        printf("Case #%d: [",t);
        for(int i=0;i<int(u.size());i++){
            if(i) printf(", ");
            putchar(u[i]);
        }
        puts("]");
    }
}
