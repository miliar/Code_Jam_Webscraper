/****** Welcome to the code jam ***********/
#include<cstdio>
#include<algorithm>
using namespace std;
#define len 20

int n;
char s[600];
char conS[600];
char o[]={"welcome to code jam"};
int cntC[20]={0};
int saveNum[500]={0};
int id=0;

int cnt, start, sStart, runStart, ed;

int w[20]={0};
void dfs(int index, int bes){
    if(18-index > ed - bes) return;
    for(int i=0; i<index; ++i) if(!w[i]) return;
    if(index==19){
        int tem=1;
        for(int i=0; i<index; ++i)
            tem*=w[i];
        cnt+=tem;
    }else{
        for(int i=bes; i<=ed; ++i)
            if(o[index]==conS[i]){
                /*printf("--%c-%d--", conS[i], saveNum[i]);*/
                w[index]=saveNum[i];
                dfs(index+1, i);
                w[index]=0;
            }
    }
    return;
}

int main(){
/*    freopen("s1.in", "r", stdin);
    freopen("s.out", "w", stdout);*/
    
    gets(s);
    sscanf(s, "%d", &n);
    for(int z=1; z<=n; ++z){
        gets(s);
        int sLen,i;
        for(i=0; (s[i]>='a'&&s[i]<='z')||s[i]==' '; ++i)
            saveNum[i]=0;
        sLen=i;
        
        id=0;
        saveNum[id]=1;
        conS[id]=s[0];
        for(int i=1; i<sLen; ++i){
            if(s[i]==conS[id]) ++saveNum[id];
            else{
                 conS[++id]=s[i];
                 saveNum[id]=1;
            }
        }
        ++id;
        
        start = -1;
        cnt=0;
        ed = id-1;
        
        for(int i=id-1; i>start+18; --i)
            if(conS[i]=='m'){ed=i;break;}
        for(int i=0; i<id; ++i)
            if(conS[i]=='w'){start=i;break;}
        for(int i=0; i<20; ++i)
            w[i]=0;
/*        
        printf("%d %d %d\n", id, start, ed);
        for(int i=start; i<=ed; ++i)
            printf("%c", conS[i]);
        puts("");
*/        
        dfs(0, start);
        if(cnt>999)
            printf("Case #%d: %d\n",z, cnt%10000);
        else if(cnt>99)
            printf("Case #%d: 0%d\n",z, cnt);
        else if(cnt>9)
            printf("Case #%d: 00%d\n",z, cnt);
        else
            printf("Case #%d: 000%d\n",z, cnt);
            
    }
    return 0;
}
