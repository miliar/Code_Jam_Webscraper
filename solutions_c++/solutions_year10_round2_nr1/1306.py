#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<set>
#include<algorithm>


using namespace std;

char dic[300][200];
int d;

int main(){
    int t;
    scanf("%d",&t);
    char s[110];
    for(int c=1;c<=t;c++){
        int n,m;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++){
            scanf("%s",dic[i]);
        }
        d=n;
        int resp=0;
        for(int i=0;i<m;i++){
            scanf("%s",s);
            int cara=-1,mini=0;
            for(int j=0;s[j];j++)
                if(s[j]=='/')
                    mini++;
            
            for(int j=0;j<d ;j++){
              //  printf("aqui\n");
                int l=0,k,cnt=0;
                for(k=0;s[k] && dic[j][k] && s[k]==dic[j][k];k++)
                    if(s[k]=='/')l=k;
                if(s[k] && dic[j][k]){
                 ; 
                }
                else if(s[k]){
                    if(s[k]=='/')
                        l=k;
                }
                else if(dic[j][k]){
                    if(dic[j][k]=='/')
                        l=k;                
                }
                else{
                    l=k;
                }
                for(k=l;s[k];k++)
                    if(s[k]=='/')cnt++;
                if(cnt<mini)
                    mini=cnt;
            } 
            
            resp+=mini;
            strcpy(dic[d++],s);
        }
        printf("Case #%d: %d\n",c,resp);
    }
    return 0;
}
