#include <stdio.h>
#include <string.h>

int main()
{
    int i,j,k,out,l,count,trial;
    char string[100][101]={0},temp[101];
    bool done[100]={0};
    scanf("%d",&i);
    for (int cas=1;cas<=i;cas++)
    {
          count = out = 0;
          scanf("%d",&j);
          k=j;
          getchar();
          while (k)
          {
                fgets(string[--k],100,stdin);
                string[k][strlen(string[k])-1]=0;
                //printf("%s1\n",string[k]);
          }
          scanf("%d",&k);
          getchar();
          while (k--)
          {
                fgets(temp,100,stdin);
                temp[strlen(temp)-1]=0;
                //printf("%s %d\n",temp,count);
                for (l=0;l<j;l++)
                if (!strcmp(temp,string[l]) && !done[l])
                {
                    done[l]=1;
                    trial=l;
                    count++;
                }
                if (count == j) 
                {
                    out++;
                    count=1;
                    for (l=0;l<j;l++) done[l]=0;
                    done[trial]=1;
                }
          }
          for (l=0;l<j;l++) done[l]=0;
          printf("Case #%d: %d",cas,out);
          (cas<i) && printf("\n");
    }
    return 0;
}
