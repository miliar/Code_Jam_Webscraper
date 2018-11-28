#include<iostream>
using namespace std;
char str[110][2];
int num[110];
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%s%d",&str[i],&num[i]);
        }
        int l=1,r=1;
        int tl=0,tr=0;
        int res=0;
        for(int i=0;i<n;i++)
        {
            if(str[i][0]=='O')
            {
                int need=abs(num[i]-l);
                int have=res-tl;
                if(need<have) res++;
                else res+=need-have+1;
                l=num[i];
                tl=res;
            }
            else
            {
                int need=abs(num[i]-r);
                int have=res-tr;
                if(need<have) res++;
                else res+=need-have+1;
                r=num[i];
                tr=res;
            }

        }
        printf("Case #%d: %d\n",ca,res);
    }
}
