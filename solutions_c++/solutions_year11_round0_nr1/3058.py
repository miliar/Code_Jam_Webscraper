#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;

int main()
{
    char c[20];
    int temp;
    int n;

    char str[100];
    int numo[100];
    int numb[100];
    int cnt=0;
    int cnto=0;
    int cntb=0;
    int cntt=0;
    FILE *in=fopen("A-large.in","r");
    FILE *out=fopen("A-large.out","w");
    fscanf(in,"%d",&n);
    //scanf("%d",&n);
    while(n--)
    {
        cntt++;
        cnto=0;
        cntb=0;
        fscanf(in,"%d",&cnt);
        //scanf("%d",&cnt);
        for(int i=0;i<cnt;i++)
        {
            fscanf(in,"%s%d",c,&temp);
            //scanf("%s%d",c,&temp);
            str[i]=c[0];
            if(c[0]=='O')
                numo[cnto++]=temp;
            else
                numb[cntb++]=temp;
        }
        int currento=1;
        int currentb=1;
        int ans=0;
        int i=0;
        int j=0;
        int k=0;
        while(k<cnt)
        {
            ans++;
            if(str[k]=='O')
            {
                if(currento==numo[i])
                {
                    k++;
                    i++;
                }
                else
                {
                    if(numo[i]>currento) currento++;
                    else currento--;
                }
                if(currentb!=numb[j])
                {
                    if(numb[j]>currentb) currentb++;
                    else currentb--;
                }
            }
            else
            {
                if(currentb==numb[j])
                {
                    k++;
                    j++;
                }
                else
                {
                    if(numb[j]>currentb) currentb++;
                    else currentb--;
                }
                if(currento!=numo[i])
                {
                    if(numo[i]>currento) currento++;
                    else currento--;
                }
            }
        }

        fprintf(out,"Case #%d: %d\n",cntt,ans);
    }
    return 0;

}
