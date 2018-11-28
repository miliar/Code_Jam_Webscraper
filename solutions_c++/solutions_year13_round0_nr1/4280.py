#include<cstdio>
#define XW 3
#define XWS (3*3*3)

#define OW 2
#define OWS (2*2*2)

#define DW 1
#define GNC 4

char s[10][10];
int ts[10][10];

int toint(char ch)
{
    if(ch=='X') return 3;
    if(ch=='O') return 2;
    if(ch=='T') return 1;
    return 0;
}

int check(void)
{
    int ans,flag=1;
    for(int i=0;i<4;i++) {
        ans=1;
        for(int j=0;j<4;j++) ans*=ts[i][j];
        if(ans==XWS || ans==XWS*XW) return XW;
        if(ans==OWS || ans==OWS*OW) return OW;
        if(ans==0) flag=0;
        
        ans=1;
        for(int j=0;j<4;j++) ans*=ts[j][i];
        if(ans==XWS || ans==XWS*XW) return XW;
        if(ans==OWS || ans==OWS*OW) return OW;
        if(ans==0) flag=0;
    }
    ans=ts[0][0]*ts[1][1]*ts[2][2]*ts[3][3];
    if(ans==XWS || ans==XWS*XW) return XW;
    if(ans==OWS || ans==OWS*OW) return OW;
    if(ans==0) flag=0;
    ans=ts[0][3]*ts[1][2]*ts[2][1]*ts[3][0];
    if(ans==XWS || ans==XWS*XW) return XW;
    if(ans==OWS || ans==OWS*OW) return OW;
    if(ans==0) flag=0;
    if(flag==0) return GNC;
    return DW;
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int cas=1;
    while(t--) {
       for(int i=0;i<4;i++) scanf("%s",s[i]);
       for(int i=0;i<4;i++) {
          for(int j=0;j<4;j++) ts[i][j]=toint(s[i][j]);
       }
       int state=check();
       printf("Case #%d: ",cas++);
       if(state==XW) printf("X won\n");
       if(state==OW) printf("O won\n");
       if(state==DW) printf("Draw\n");
       if(state==GNC) printf("Game has not completed\n");
    }
    return 0;
}
