#include <iostream>
  using namespace std;
  int son[250000][27],ans,n,l,d,allzm;
  char s[20];bool flag;bool t[20][26];
void ins(int x,int p){
     if(p==l)return;
     int y;
     if(son[x][s[p]-'a']>0)y=son[x][s[p]-'a'];else
     {y=++allzm;son[x][s[p]-'a']=y;};
     ins(y,p+1);
}
void findd(int x,int p,int y){
     int i;
     if(son[x][y]>0){
       if(p==l){ans++;return;};
       for(i=0;i<26;i++)if(t[p+1][i])findd(son[x][y],p+1,i);
       }
     else return;       
}
main(){
     freopen("a.in","r",stdin);
     freopen("a.out","w",stdout);
     scanf("%d%d%d\n",&l,&d,&n);
     memset(son,0,sizeof(son));
     allzm=1;
     int i,tt,tot,j,x,y;
     for(i=1;i<=d;i++){
       gets(s);
       ins(1,0);
       };
     char ch;
     bool bx;
     for(i=1;i<=n;i++){
        memset(t,false,sizeof(t));
        printf("Case #%d: ",i);
        ans=0;tot=1;bx=false;y=0;
        for(x=1;x<=l;x++){
          scanf("%c",&ch);
          if(ch=='('){
            scanf("%c",&ch);
            while(ch!=')'){
              t[x][ch-'a']=true;
              scanf("%c",&ch);
              };
            }else t[x][ch-'a']=true;
          };
          scanf("%c",&ch);
          for(x=0;x<26;x++)if(t[1][x])findd(1,1,x);
          printf("%d\n",ans);
      };
}
