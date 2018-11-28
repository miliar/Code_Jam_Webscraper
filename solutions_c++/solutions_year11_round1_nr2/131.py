#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int T;

class Word{
public:
    int len;
    int value;
    int mask[26];
    void in(char str[],int v){
        len=strlen(str);
        memset(mask,0,sizeof mask);
        for (int i=0;i<len;++i)
            mask[str[i]-'a']|=1<<i;
        value = v;
    }
}word[11000];

bool cmplen(const Word &a,const Word &b){
    return a.len<b.len;
}

int now;
char list[100];
int bh[11000];

bool cmp(const int &a,const int &b){
    return word[a].mask[now]<word[b].mask[now];
}

pair<int,int> calc(int l,int r,int d,int v){
//    printf("%d %d %d %d\n",l,r,d,v);
    if (l==r)
        return make_pair(v,-word[bh[l]].value);
    now=list[d]-'a';
    int nnow=now;
    sort(bh+l,bh+r+1,cmp);
    pair<int,int> ans=make_pair(0,-word[bh[l]].value);
    for (int i=l;i<=r;){
        int j=i;
        while (j<=r && word[bh[j]].mask[nnow]==word[bh[i]].mask[nnow])
            ++j;
        ans=max(ans,calc(i,j-1,d+1,v+(!word[bh[i]].mask[nnow]&&j<=r)));
        i=j;
    }
    return ans;
}

int I=0,n,m,i,j;
char w[11000][20];

int main(){
    scanf("%d",&T);
    while (T--){
        printf("Case #%d:",++I);
        scanf("%d%d",&n,&m);
        for (i=0;i<n;++i){
            scanf(" %s",w[i]);
            word[i].in(w[i],i);
        }
        sort(word,word+i,cmplen);
        for (int cases=0;cases<m;++cases){
            scanf(" %s",list);
            pair<int,int> ans=make_pair(0,0);
            for (i=0;i<n;++i)
                bh[i]=i;
            for (i=0;i<n;){
                j=i;
                while (j<n && word[j].len==word[i].len) ++j;
                ans=max(ans,calc(i,j-1,0,0));
                i=j;
            }
//            printf(" %d",ans.first);
            printf(" %s",w[-ans.second]);
        }
        puts("");
    }
}
