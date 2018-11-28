#include <cstdio>
#include <cstring>

using namespace std;

char words[5005][20];
char pat[20][30];
char p[10005];

int main(){
    int l,d,n;
    scanf("%d %d %d",&l,&d,&n);
    
    for(int i=0;i<d;i++)
        scanf("%s",words[i]);
    
    for(int t=1;t<=n;t++){
        printf("Case #%d: ",t);
        
        scanf("%s",p);
        memset(pat,0,sizeof(pat));
        
        int il=0,len=strlen(p);
        
        for(int i=0;i<len;)
            if(p[i]=='('){
                i++;
                while(p[i]!=')'){
                    pat[il][p[i]-'a']=1;
                    i++;
                }
                i++; il++;
            }else{
                pat[il][p[i]-'a']=1;
                i++; il++;
            }
        int res=0;
        for(int i=0;i<d;i++){
            bool f=true;
            for(int j=0;j<l;j++)    
                if(!pat[j][words[i][j]-'a']){
                    f=false;
                    break;
                }
            if(f) res++;
        }
        printf("%d\n",res);
    }
    
    return 0;
}
