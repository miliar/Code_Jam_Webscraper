#include<stdio.h>
#include<string.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("bl.out","w",stdout);

    int i,j,k,c,d,n,t,kase=0,top,f;
    char com[150][5],opp[150][5],invoke[150],eList[150],tcom1[5],tcom2[5],pres[5],topp[5],topp1[5],temp;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&c);
        for (i=0;i<c;i++)
            scanf("%s",com[i]);
        scanf("%d",&d);
        for (i=0;i<d;i++)
            scanf("%s",opp[i]);
        scanf("%d",&n);
        scanf("%s",invoke);
        top=0;
        for (i=0;i<n;i++)
        {
            f=0;
            temp=invoke[i];
            if (top==0)
            {
                eList[top++]=invoke[i];
                continue;
            }
            //checking combination
            for (j=0;j<c;j++)
            {
                //QF
                tcom1[0]=com[j][0];tcom1[1]=com[j][1];tcom1[2]='\0';
                //FQ
                tcom2[0]=com[j][1];tcom2[1]=com[j][0];tcom2[2]='\0';
                //PRESENT COMBINATION FOUND
                pres[0]=eList[top-1];pres[1]=temp;pres[2]='\0';
                if (strcmp(tcom1,pres)==0||strcmp(tcom2,pres)==0)
                {
                eList[top-1]=com[j][2];
                f=1;
                break;
                }
            }
             if(f==1)
             continue;
             //checking oppose
            f=0;
            for(j=top-1;j>=0;j--)
            //for(j=0;j<top;j++)
            {
              //RF
              topp[0]=eList[j];topp[1]=temp;topp[2]='\0';
              //FR
              topp1[0]=temp;topp1[1]=eList[j];topp1[2]='\0';
              for(k=0;k<d;k++)
              {
                  if(strcmp(opp[k],topp)==0 || strcmp(opp[k],topp1)==0)
                  {
                      top=0;
                      f=1;
                      break;
                  }
              }
              if(f==1)
              break;
            }
            if(f==1)
            continue;
            //default invoke
            eList[top++]=temp;
        }
        //processing result
        printf("Case #%d: [",++kase);
        for(i=0;i<top;i++)
        {
            if(i!=top-1)
            printf("%c, ",eList[i]);
            else
            printf("%c",eList[i]);
        }
        printf("]\n");
    }
    return 0;
}
