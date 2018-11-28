#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;


int main()
{

    int cas,ct=1;
    int i,j,k;
    int n;

    //freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);


    scanf("%d",&cas);
    while (cas--)
    {

        scanf("%d%d",&n,&k);

        k = k%(2<<(n-1));
        bool flag = false;

		int t = 2<<(n-1);
		t --;
        if (k == t)
        {
            flag = true;
        }



        printf("Case #%d: ",ct++);
        if (flag) printf("ON\n");
        else printf("OFF\n");
        }

return 0;
}