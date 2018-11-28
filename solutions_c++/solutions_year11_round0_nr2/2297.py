#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))

using namespace std;

int T,p,q,n;
int d[1000],c[26][26],o[26][26],h[26];
char r[1000];

void init()
{
    char st[1000];
    clr(c,-1);
    clr(o,0);
    clr(h,0);
    scanf("%d",&p);
    for (int i=0;i<p;i++){
        scanf("%s",st);
        c[st[0]-'A'][st[1]-'A']=st[2]-'A';
        c[st[1]-'A'][st[0]-'A']=st[2]-'A';
    }
    scanf("%d",&q);
    for (int i=0;i<q;i++){
        scanf("%s",st);
        o[st[0]-'A'][st[1]-'A']=1;
        o[st[1]-'A'][st[0]-'A']=1;
    }
    scanf("%d",&n);
    scanf("%s",st);
    for (int i=0;i<n;i++)
        d[i]=st[i]-'A';
//    printf("%d %d %d %d %d %d %d\n",d[0],d[1],d[2],d[3],d[4],d[5],d[6]);
}

int work()
{
    int s[1000];
    int l=0;
    for (int i=0;i<n;i++){
        if (l==0){
            s[l++]=d[i];
            h[d[i]]++;
        }else{
            if (c[s[l-1]][d[i]]!=-1){
                h[s[l-1]]--;
                s[l-1]=c[s[l-1]][d[i]];
            }else{
                int k=1;
                for (int j=0;j<26;j++)
                    if (h[j]>0&&o[j][d[i]]==1)
                        k=0;
                if (k){
                    s[l++]=d[i];
                    h[d[i]]++;
                }else{
                    l=0;
                    clr(h,0);
                }
            }
        }
//        printf("(%d)%d %d %d %d %d\n",l,s[0],s[1],s[2],s[3],s[4]);
    }
    r[0]='[';
    for (int i=0;i<l;i++){
        r[3*i+1]=s[i]+'A';
        r[3*i+2]=',';
        r[3*i+3]=' ';
    }
    if (l>0){
        r[l*3-1]=']';
        r[l*3]='\0';
    }else{
        r[1]=']';
        r[2]='\0';
    }
}

int main()
{
    FILE *cin=freopen("B.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        init();
        work();
        printf("Case #%d: %s\n",tnum,r);
    }
}
