#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<time.h>
//using namespace std;
typedef long long LL;
inline LL Min(LL a,LL b){
    return a<b?a:b;
}
inline LL Max(LL a,LL b){
    return a>b?a:b;
}
inline LL Abs(LL a){
    return a>0?a:-a;
}
bool cmp(LL a,LL b){
    return a<b;
}
struct INDEX{
    int ptr;
    int tos;
    bool operator<(INDEX b)  const{
        return tos<b.tos;
    }
}ind[10010];
struct WORD{
    char tex[12];
    int len,cnt[27],tsn,ans;
}dic[10010];
char ord[27];
int ivo[27];
int casN,n,m,mxa,map,tmp;
inline int calc(int a,int b){
    int i,ans=0;
    for(i=0;i<27;i++){
        if(dic[a].cnt[i]!=dic[b].cnt[i])break;
        if(!dic[a].cnt[i])ans++;
    }
    if(!dic[a].cnt[i])ans++;
    return ans;
}
int main(){
    scanf("%d",&casN);
    //clock_t clk=clock();
    for(int III=0;III<casN;III++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++){
            scanf("%s",dic[i].tex);
            dic[i].len=strlen(dic[i].tex);
        }
        printf("Case #%d:",III+1);
        for(int ii=0;ii<m;ii++){
            scanf("%s",ord);
            for(int i=0;i<26;i++){
                ivo[ord[i]-'a']=i+1;
            }
            for(int i=0;i<n;i++){
                dic[i].cnt[0]=dic[i].len;
                for(int j=1;j<=26;j++)dic[i].cnt[j]=0;
                for(int j=0;j<dic[i].len;j++){
                    dic[i].cnt[ivo[dic[i].tex[j]-'a']]|=1<<j;
                }
            }
            for(int i=0;i<n;i++){
                ind[i].ptr=i;
                ind[i].tos=0;
                dic[ind[i].ptr].tsn=n;
                dic[ind[i].ptr].ans=0;
            }
            for(int j=0;j<27;j++){
                int cur=0,add,ctn=1,str=0;
                for(int i=0;i<n;i++){
                    if(i==n-1||ind[i].tos!=ind[i+1].tos){
                        add=1;
                    }
                    else add=0;
                    ind[i].tos=cur*30000+dic[ind[i].ptr].cnt[j];
                    cur+=add;
                }
                std::sort(ind,ind+n);
                for(int i=0;i<n;i++){
                    if(i==n-1||ind[i].tos!=ind[i+1].tos){
                        for(int k=str;k<=i;k++){
                            if(ctn!=dic[ind[k].ptr].tsn&&!dic[ind[k].ptr].cnt[j])dic[ind[k].ptr].ans++;
                            dic[ind[k].ptr].tsn=ctn;
                        }
                        str=i+1;
                        ctn=0;
                    }
                    ctn++;
                }
            }
            mxa=0;
            for(int i=0;i<n;i++){
                /*if(i!=0){
                    tmp=calc(ind[i].ptr,ind[i-1].ptr);
                    if(tmp>mxa||(tmp==mxa&&ind[i].ptr<map)){
                        mxa=tmp;
                        map=ind[i].ptr;
                    }
                }
                if(i!=n-1){
                    tmp=calc(ind[i].ptr,ind[i+1].ptr);
                    if(tmp>mxa||(tmp==mxa&&ind[i].ptr<map)){
                        mxa=tmp;
                        map=ind[i].ptr;
                    }
                }*/
                //fprintf(stderr,"%s %d\n",dic[i].tex,dic[i].ans);
                if(dic[ind[i].ptr].ans>mxa||(dic[ind[i].ptr].ans==mxa&&ind[i].ptr<map)){
                    mxa=dic[ind[i].ptr].ans;
                    map=ind[i].ptr;
                }                    
            }
            printf(" %s",dic[map].tex);
        }
        //fprintf(stderr,"%d\n",clock()-clk);
        puts("");
    }
    scanf(" ");
    return 0;
}

