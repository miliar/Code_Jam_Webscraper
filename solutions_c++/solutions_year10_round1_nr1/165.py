#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

char map[60][60];
int top[60],n,k1;

bool smallJudge(int x,int y,int dx,int dy){
    char ch=map[x][y];
    int ans=0;
    while((x>0)&&(x<=n)&&(y>0)&&(y<=top[x])&&(map[x][y]==ch)){
        ++ans;
        x+=dx;
        y+=dy;
    }
    return (ans>=k1);
}


bool judge(int x,int y){
    return smallJudge(x,y,1,0)||smallJudge(x,y,0,1)||smallJudge(x,y,1,-1)||smallJudge(x,y,1,1);
}

char s[60];

void solve(){
    scanf("%d%d",&n,&k1);
    int i,j;
    for(i=1;i<=n;++i){
        scanf("%s",s+1);
        top[i]=0;
        for(j=n;j>0;--j)if(s[j]!='.')map[i][++top[i]]=s[j];
    }
    bool fr=false,fb=false;
    for(i=1;i<=n;++i)
        for(j=1;j<=top[i];++j)if(map[i][j]=='R')fr|=judge(i,j);else fb|=judge(i,j);
    if(fr){
        if(fb)printf("Both\n");else printf("Red\n");
    }else{
        if(fb)printf("Blue\n");else printf("Neither\n");
    }
}

int main(){
    freopen("gcja.in","r",stdin);
    freopen("gcja.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        solve();
    }

}


