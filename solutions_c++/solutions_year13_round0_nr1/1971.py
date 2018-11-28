#include<stdio.h>
int t,i,j,k,cntx1,cntx2,cntx3,cntx4,cnto1,cnto2,cnto3,cnto4,flag,c;
char arr[8][8],s[8];
int main()
{
    scanf("%d",&t);

    while(t--)
    {
        ++c;
        for(i=1;i<=4;i++)
        {
            scanf("%s",&s);
            for(j=1;j<=4;j++)
            {

                arr[i][j]=s[j-1];

            }

        }
        k=4;
        cntx3=0;cntx4=0;cnto3=0;cnto4=0;flag=0;
        for(i=1;i<=4;i++)
        {
            cntx1=0;cnto1=0;cntx2=0;cnto2=0;
            for(j=1;j<=4;j++)
            {
                if(arr[i][j]=='X' || arr[i][j]=='T')
                ++cntx1;
                if(arr[i][j]=='O' || arr[i][j]=='T')
                ++cnto1;
                if(arr[j][i]=='X' || arr[j][i]=='T')
                ++cntx2;
                if(arr[j][i]=='O' || arr[j][i]=='T')
                ++cnto2;
                if(arr[i][j]=='.')
                flag=1;

            }
            if(arr[i][i]=='X' || arr[i][i]=='T')
            ++cntx3;
            if(arr[i][i]=='O' || arr[i][i]=='T')
            ++cnto3;
            if(arr[i][k]=='X' || arr[i][k]=='T')
            ++cntx4;
            if(arr[i][k]=='O' || arr[i][k]=='T')
            ++cnto4;
            if(cntx1==4 || cnto1==4 || cntx2==4 || cnto2==4)
            break;
            k--;
        }
        if(cntx1==4 || cntx2==4 || cntx3==4 || cntx4==4)
        printf("Case #%d: X won\n",c);
        else if(cnto1==4 || cnto2==4 || cnto3==4 || cnto4==4)
         printf("Case #%d: O won\n",c);
         else if(flag==0)
          printf("Case #%d: Draw\n",c);
          else
           printf("Case #%d: Game has not completed\n",c);

    }
    return 0;
}
