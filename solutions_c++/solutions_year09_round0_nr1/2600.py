#include<iostream>
using namespace std;
char word[5000][20]={0},word1[2000]={0};
int n,i,d,l,j;


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d %d %d",&l,&d,&n);
    scanf(" \n");
    for (i=1;i<=d;i++) { 
        for (j=0;j<l;j++) 
        scanf("%c",&word[i][j]); 
        scanf(" \n");
    }
    for (i=1;i<=n;i++)
    {
        j=0;int p=0;
        memset(word1,0,sizeof(word1));
        while (j<l)
        {
              scanf("%c",&word1[p]);
              p++;
              if (word1[p-1]=='(')
              {
                               while (word1[p-1]!=')') {scanf("%c",&word1[p]);p++;}
              }
              j++;
        }
        scanf(" \n");
        int ans=0;
        for (j=1;j<=d;j++)
        {
            bool f=true;
            int k=0,start=0;
            while (f&&(k<l))
            {
                  if (word1[start]!='(')
                  {
                      if (word1[start]!=word[j][k]) {f=false;break;}
                  }
                  else
                  {
                      bool f1=true;
                      while (word1[start]!=')')
                      {
                            if (word[j][k]==word1[++start]) {f1=false;}
                      }
                      if (f1) f=false;
                  }
                  k++;start++;
            }
            if (f) ans++;
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
