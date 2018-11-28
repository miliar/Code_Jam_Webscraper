#include <cstdio>
#include <cstring>
#include <utility>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cs,n;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        vector<int> a,b;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            int pos;
            char s[100];
            scanf("%s%d",s,&pos);
            if(*s=='O'){
                while(a.size()<b.size()) a.push_back(-pos);
                a.push_back(pos);
            }else{
                while(b.size()<a.size()) b.push_back(-pos);
                b.push_back(pos);
            }
        }
        while(a.size()<b.size()) a.push_back(-1);
        while(b.size()<a.size()) b.push_back(-1);
        int ans=0,m=a.size(),x=1,y=1;
        for(int i=0;i<m;i++){
            bool over=false;
            while(!over){
                ans++;
                if(x!=abs(a[i])) x+=(abs(a[i])-x<0?-1:1); else if(a[i]>0) over=true;
                if(y!=abs(b[i])) y+=(abs(b[i])-y<0?-1:1); else if(b[i]>0) over=true;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
