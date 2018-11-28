#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int sum_Pa(int a ,int b)
{
    int sum=0;


    for(int i=0; i<31;i++)
    {
        if((a&1)&& !(b&1))
        {
            sum = sum | (1<<i);
        }
        else if(!(a&1)&&(b&1))
        {
            sum = sum | (1<<i);
        }
        a = a>>1;
        b = b>>1;
    }

    return sum;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    vector<int> L;
    int sum;
    int temp;
    int n;
    int m;
    int l;

    scanf("%d\n",&n);
    for(int i=0; i<n; i++){

        scanf("%d\n", &m);
        sum = 0;
        for(int j=0; j<m; j++)
        {
            scanf("%d", &temp);

            sum = sum_Pa(sum, temp);
            L.push_back(temp);
        }

        if(sum!=0)
          printf("Case #%d: NO\n",i+1);
        else{
            sum = temp =0;
            l = L.size();

           sort(L.begin(),L.end());

            for(int k=l-1; k>-1; k--)
            {
                sum = sum_Pa(sum,L[k]);

                if(sum == 0)
                 break;

                 temp += L[k];
            }
            printf("Case #%d: %d\n", i+1, temp);
        }

        L.clear();
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
