#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>

using namespace std;
int main()
{
    FILE* f1;
    f1=fopen("opt.txt","w");
	int tc,tc1,n,n1,s,p,i=0;
	int size=0;
    int ti[100]={0};
    int ans[100]={0};
	scanf("%d",&tc);
	tc1=tc;
	while(tc--)
	{
        scanf("%d",&n);
        scanf("%d",&s);
        scanf("%d",&p);
        n1=n;
        for(i=0;i<n;i++)
            ti[i]=0;
        while(n--)
        {
            scanf("%d",&ti[n1-n-1]);
        }
        n=n1;
        for(i=0;i<n;i++)
        {
            printf("checking if %d %d has best > p\n",i,ti[i]);
            if(ti[i]>=p)
            {

            if(ti[i]>=3*p)
            {
                if(ti[i]%3==0)
                {
                    printf("%d has best from F\n",i);
                            ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                    continue;
                }
            }

            if(ti[i]>=3*(p-2)+5)
            {
                if(ti[i]%3==2)
                    {
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                        printf("%d has best from Q\n",i);
                        continue;
                    }
                else
                {
                    printf("failed Q");
                }
            }
            if(ti[i]>=3*(p-2)+4)
            {
                if(ti[i]%3==1)
                    {
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                        printf("%d has best from A\n",i);
                        continue;
                    }
                else
                {
                    printf("failed A");
                }
            }
            if(ti[i]>=3*(p-2)+2)
            {
                if(ti[i]%3==0 && s!=0)
                    {
                        printf("%d has best from B\n",i);
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                        s--;

                    }


                else if(ti[i]%3==2 && s!=0 )
                    {
                        printf("%d has best from C\n",i);
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                        s--;

                    }
                else if(ti[i]%3==1 && s!=0 )
                    {
                        printf("%d has best from D\n",i);
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;
                        s--;

                    }
                else if(ti[i]==0 && s==0)
                {
                    printf("%d has best from E\n",i);
                        ans[tc1-tc-1]=ans[tc1-tc-1]+1;

                }

            }

        }
    }
        printf("\n");
    }
	tc=tc1;
	while(tc--)
		{   fprintf(f1,"Case #%d: %d\n",tc1-tc,ans[tc1-tc-1]);
            printf("Case #%d: %d\n",tc1-tc,ans[tc1-tc-1]);
		}
  fclose(f1);
  cin.sync();
  cin.get();

  return 0;

}
