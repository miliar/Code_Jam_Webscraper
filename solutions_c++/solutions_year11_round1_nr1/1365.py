#include <iostream>
#include <cstdio>
using namespace std;
int t1,n,pd,pg,d,g;
bool flag;

int main()
{
    freopen("3.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t1;
    for (int t2 = 1; t2 <= t1; ++t2){
        cin>>n >>pd >>pg;
        flag = false;
        if (n > 200) n = 200;
        for (int d = 1; d <= n; ++d)
            if ((d * pd) % 100 == 0){
                int i = d * pd / 100;
                for (int g = i; g <= 200; ++g)
                    if ((g * pg) % 100 == 0){
                        int j = g * pg / 100;
                        if ((d == g)&&(i == j))
                        flag = true;
                        if ((d < g)&&((j-i) < (g-d))&&(i <= j))
                        flag = true;
                    }
            }
        cout<<"Case #" <<t2 <<": ";
        if (flag) cout<<"Possible";
            else cout<<"Broken";
        cout<<endl;
    }
}
