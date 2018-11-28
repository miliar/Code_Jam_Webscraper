
#include <stdio.h>
#include <stdlib.h>

//---------------------------------------------------------------------------


int main(int argc, char* argv[])
{
        char s[1000],s1[1000];
        int n, i;
        char k;
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        char ss[33] = "yhesocvxduiglbkrztnwjpfmaq";
        gets(&k);
        n=k-'0';
        for (int j=0;j<n;j++)
        {
                if (j>0) printf("\n");
                printf("Case #%d: ",j+1);
                gets(s);
                for (i=0;s[i];i++)
                {
                        if (s[i]>='a'&&s[i]<='z')
                                printf("%c",ss[s[i]-'a']);
                        else printf("%c",s[i]);
                }

        }
        /*s[i] = 0;
          for (i=0;(s1[i]=getchar())!='\n';i++);
          s1[i]=0;
        */
        /*for (char i='a';i<='z'; i++)
        {
              for (int j=0;s[j];j++)
              {
                    if (s[j]==i)
                  {
                        printf ("%c",s1[j]);
                         break;
                   }
                }
         }
        */
        scanf("%d",&n);
        return 0;
}
