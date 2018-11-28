#include<stdio.h>
#include<string.h>
#include<vector>
#include<list>
using namespace std;
struct WORD{
    char s[12];
    void scan(){scanf("%s",s);}
}word[10000];
vector<int>d[11][26][1024];
int have[10000][26],len[10000];
bool have2[10000][26];
vector<int>have3[10000];
int cti(char c){return c-'a';}
void Pre(int N){
    int i,j,k,now;
    for(i=1;i<=10;i++)
        for(j=0;j<26;j++)
            for(k=0;k<1024;k++)d[i][j][k].clear();
    for(i=0;i<N;i++)
        for(j=0;j<26;j++)have2[i][j]=0;
    for(i=0;i<N;i++)have3[i].clear();
    for(i=0;i<N;i++){
        len[i]=strlen(word[i].s);
        for(j=0;j<26;j++){
            now=0;
            for(k=0;k<len[i];k++)
                if(cti(word[i].s[k])==j)now+=1<<k;
            d[len[i]][j][now].push_back(i);
            have[i][j]=now;
            if(now)have2[i][j]=1,have3[i].push_back(j);
        }
    }
}
list<int>List;
int Do(int x,char in[],int N){
    int i,j,an=0;
    int possible[26];
    for(i=0;i<26;i++)possible[i]=0;
    List.clear();
    for(i=0;i<N;i++){
        if(len[i]==len[x]){
            List.push_back(i);
            for(j=0;j<have3[i].size();j++)possible[have3[i][j]]++;
        }
    }
    for(i=0;i<26;i++){
        if(possible[cti(in[i])]>0){
            if(!have2[x][cti(in[i])])an++;
            list<int>::iterator it;
            for(it=List.begin();it!=List.end();){
                if(have[*it][cti(in[i])]!=have[x][cti(in[i])]){
                    for(j=0;j<have3[*it].size();j++)possible[have3[*it][j]]--;
                    it=List.erase(it);
                }
                else it++;
            }
        }
    }
    return an;
}
int Go(char in[],int N){
    int i,tmp,an,ma=-1;
    for(i=0;i<N;i++){
        tmp=Do(i,in,N);
        if(tmp>ma){
            ma=tmp;
            an=i;
        }
    }
    return an;
}
main(){
    int T,i,N,M,t=0;
    char in[32];
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&N,&M);
        for(i=0;i<N;i++)word[i].scan();
        printf("Case #%d:",++t);
        Pre(N);
        while(M--){
            scanf("%s",in);
            printf(" %s",word[Go(in,N)].s);
        }
        puts("");
    }
}
