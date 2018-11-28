#include <iostream>
#include <cmath>
#include <map>
using namespace std;
int main()
{
   // printf("%d\n",1<<1);
 freopen("b6.txt","r",stdin);
   freopen("b6out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int c,d,n;
        int com[30][30];
        int clear[30][30];
        for(int i=0;i<26;i++)
        {
            for(int j=0;j<26;j++)
            {
                com[i][j]=-1;
                clear[i][j]=0;
            }
        }
        scanf("%d",&c);
        char word[128];
        for(int i=0;i<c;i++)
        {
            scanf("%s",word);
            //printf("%d %d %d\n",word[0]-'A',word[1]-'A',word[2]-'A');
            com[word[0]-'A'][word[1]-'A']=word[2]-'A';
            com[word[1]-'A'][word[0]-'A']=word[2]-'A';
        }
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%s",word);
            clear[word[0]-'A'][word[1]-'A']=1;
            clear[word[1]-'A'][word[0]-'A']=1;
        }
        scanf("%d",&n);
        scanf("%s",word);
        int stack[128];
        int top=-1;
        for(int i=0;i<n;i++)
        {
            int now=word[i]-'A';
            stack[++top]=now;
//            printf("%d %d %d\n",stack[top],stack[top-1],com[stack[top]][stack[top-1]]);
            while(top>0 && com[stack[top]][stack[top-1]]!=-1)
            {
                stack[top-1]=com[stack[top]][stack[top-1]];
                top--;
            }
            for(int j=0;j<top;j++)
            {
                if(clear[stack[j]][stack[top]]==1)
                {
                    top=-1;
                    break;
                }
            }
           // printf("%d\n",top);
            //for(int j=0;j<=top;j++)
            //{
             //   printf("%c",stack[j]+'A');
            //}
            //printf("\n");
        }
        printf("Case #%d: [",t);
        for(int i=0;i<=top;i++)
        {
            if(i==0)
            {
                printf("%c",stack[i]+'A');
            }
            else
            {
                printf(", %c",stack[i]+'A');
            }
        }
        printf("]\n");
    }
	return 0;
}
