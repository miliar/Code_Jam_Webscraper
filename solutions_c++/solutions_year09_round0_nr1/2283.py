#include <iostream>
#include <fstream>
using namespace std;

int L,D,N;

char language[5000][16];
char test[391];
int  total;
bool flag;

int main()
{
    int i,j,k,index,r;
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    scanf("%d",&L);
    scanf("%d",&D);
    scanf("%d",&N);
    for(i=0;i<D;i++)
        scanf("%s",&language[i]);
    for(i=1;i<=N;i++)
    {
        scanf("%s",test);
        total=0;
        for(j=0;j<D;j++)
        {
            index=0;flag=true;
            for(k=0;k < L && flag == true;k++)
            {
                if(test[index]!= '(')
                {
                    if(test[index] == language[j][k])
                        index++;
                    else
                        flag=false;
                }
                else
                {
                    index++;flag=false;
                    while(test[index]!= ')')
                    {
                        if(test[index] == language[j][k])
                        {
                            flag=true;
                            index++;
                        }
                        else
                            index++;
                    } //enf of while
                    index++;
                } //end of else
            } // end of for
            if(flag == true)
                total++;
        }
        printf("Case #%d: %d\n",i,total);
    }
    fflush(stdout);
    return 0;
}
