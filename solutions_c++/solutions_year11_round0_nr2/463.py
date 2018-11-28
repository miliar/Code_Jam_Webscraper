#include<fstream>
#include<cstring>
#include<string>
#include<cstdio>
using namespace std;
char c[50][3],d[50][2],s[1000];
int m,m1,m2,n,tot;
int can[30];
char now,temp;
bool find1(char a1,char a2)
{
    for(int i=1;i<=m1;i++)
        if((a1==c[i][1] && a2==c[i][0]) || (a1==c[i][0]&&a2==c[i][1])){
            can[s[tot-1]-'A']--;can[s[tot]-'A']--;
            s[tot-1]=c[i][2];can[s[tot-1]-'A']++;
            return true;
        }
    return false;
}
bool find2()
{
    for(int i=1;i<=m2;i++)
        if(can[d[i][0]-'A']>0&&can[d[i][1]-'A']>0){
            for(int j=1;j<=tot;j++)
                can[s[j]-'A']=0;
            return true;
        }
    return false;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("2.out","w",stdout);
    int i,j,k,l;
    scanf("%d",&n);//fin>>n;
    for(l=1;l<=n;l++){
        memset(can,0,sizeof(can));
        tot=0;
        scanf("%d",&m1);//fin>>m1;
        for(i=1;i<=m1;i++)
            scanf("%c%c%c%c",&temp,&c[i][0],&c[i][1],&c[i][2]);//fin>>c[i][0]>>c[i][1]>>c[i][2];
        scanf("%d",&m2);//fin>>m2;
        for(i=1;i<=m2;i++)
            scanf("%c%c%c",&temp,&d[i][0],&d[i][1]);//fin>>d[i][0]>>d[i][1];
        scanf("%d%c",&m,&temp);//fin>>m;
        for(i=1;i<=m;i++){
            scanf("%c",&now);//fin>>now;
            s[++tot]=now;
            can[now-'A']++;
            if(find1(s[tot-1],s[tot]))
                tot--;
            if(find2())
                tot=0;
        }
        printf("Case #%d: [",l);//fout<<"Case #"<<l<<": [";
        if(tot>0){
            for(i=1;i<tot;i++)
                printf("%c, ",s[i]);//fout<<s[i]<<", ";
            printf("%c",s[tot]);//fout<<s[tot];
        }
        printf("]\n");//fout<<"]"<<endl;
    }
    return 0;
}

