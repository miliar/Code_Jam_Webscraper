#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{   
    int t,o;
   // freopen("E:/in.txt","r",stdin);
//freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        int p,q;
        int a[1001],i,j,k,l;
        scanf("%d%d",&p,&q);
        for(i=1;i<=q;i++) scanf("%d",&a[i]);
        int minnum = 214748364;
        do
        {
            int num = 0;
            bool flag[1001] = {false};
            for(i=1;i<=q;i++)
            {
                flag[a[i]] = true;
                k = a[i]+1;
                while(k <=p && !flag[k])
                {
                    k ++;
                    num++;
                }
                k = a[i]-1;
                while(k >=1 && !flag[k])
                {
                    k --;
                    num++;
                }
            }
            if(num < minnum) minnum = num;
        }while(next_permutation(a+1,a+1+q));
        printf("Case #%d: %d\n",o,minnum);
    }
    return EXIT_SUCCESS;
}
