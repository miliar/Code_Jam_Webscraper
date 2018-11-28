#include<iostream>
using namespace std;
int n,i,j,k;
char ch[1000];
int ans[20],ans1[20];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d\n",&n);
    for (i=1;i<=n;i++)
    {
        memset(ch,0,sizeof(ch));
        memset(ans,0,sizeof(ans));
        //getline(ch,sizeof(ch));
        //scanf("%s",ch);
        //cin.getline(ch,sizeof(ch));
        scanf("%c",&ch[0]);
        int p=0;
        while (ch[p]!='\n')
        {
              scanf("%c",&ch[++p]);
        }
        for (j=0;j<strlen(ch);j++)
        {
            for (int k=0;k<=20;k++) ans1[k]=ans[k];
            if (ch[j]=='d') 
              {
                            ans[14]=(ans1[14]+ans1[13])%10000;
              }
            if (ch[j]=='j') 
              {
                            ans[17]=(ans1[17]+ans1[16])%10000;
              } 
              if (ch[j]=='a') 
              {
                            ans[18]=(ans1[18]+ans1[17])%10000;
              }  
              if (ch[j]==' ')
              {
                 ans[8]=(ans1[8]+ans1[7])%10000;
                 ans[11]=(ans1[11]+ans1[10])%10000;
                 ans[16]=(ans1[16]+ans1[15])%10000;
              } 
            switch(ch[j])
            {
             case'w':ans[1]=(ans1[1]+1)%10000;break;
             case'e':ans[2]=(ans1[1]+ans1[2])%10000;ans[15]=(ans1[15]+ans1[14])%10000;ans[7]=(ans1[7]+ans1[6])%10000;break;
             case'l':ans[3]=(ans1[2]+ans1[3])%10000;break;
             case'c':ans[4]=(ans1[3]+ans1[4])%10000;ans[12]=(ans1[12]+ans1[11])%10000;break;
             case'o':ans[5]=(ans1[4]+ans1[5])%10000;ans[10]=(ans1[9]+ans1[10])%10000;ans[13]=(ans1[13]+ans1[12])%10000;break;
             case'm':ans[6]=(ans1[5]+ans1[6])%10000;ans[19]=(ans1[19]+ans1[18])%10000;break;
             case't':ans[9]=(ans1[8]+ans1[9])%10000;break;
             }
        }
        printf("Case #%d: ",i);
        int ans1=ans[19];
        if (ans1<10) printf("000%d",ans1);
        else if (ans1<100) printf("00%d",ans1);
        else if (ans1<1000) printf("0%d",ans1);
        else printf("%d",ans1);
        printf("\n");
    }
    return 0;
}
