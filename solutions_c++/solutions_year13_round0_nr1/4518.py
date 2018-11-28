#include <vector>
#include <algorithm>

//#include <sstream>
#include <iostream>

#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    int t,k=1;
    freopen("t.in","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>t;
    while(k <= t)
    {

        char s[10][10];
        int a[4][4];
        int f = 0;
        for(int i = 0; i < 4; i++)
        {
            scanf("%s",&s[i]);
            for(int j = 0; j < 4; j++)
            {
                if(s[i][j]=='X')
                    a[i][j]=1;
                else if(s[i][j]=='O')
                    a[i][j] =2;
                else if(s[i][j]=='T')
                    a[i][j] = 3;
                else{
                    a[i][j] = 0;
                    f = 1;
                    //cout<<a[i][j];
                }
                //cout<<endl;
            }
        }

        int p=0;
        if(a[0][0]&a[0][1]&a[0][2]&a[0][3])
        {
            p = a[0][0]&a[0][1];
            //cout<<p<<" a"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[1][0]&a[1][1]&a[1][2]&a[1][3])
        {
            p = a[1][0]&a[1][1];
            //cout<<p<<" b"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if( a[2][0]&a[2][1]&a[2][2]&a[2][3] )
        {
            p = a[2][0]&a[2][1];
            //cout<<p<<" c"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[3][0]&a[3][1]&a[3][2]&a[3][3])
        {
            p = a[3][0]&a[3][1];
            //cout<<p<<" d"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][0]&a[1][0]&a[2][0]&a[3][0])
        {
            p = a[0][0]&a[1][0];
            //cout<<p<<" e"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][1]&a[1][1]&a[2][1]&a[3][1])
        {
            p = a[0][1]&a[1][1];
            //cout<<p<<" f"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][2]&a[1][2]&a[2][2]&a[3][2])
        {
            p = a[0][2]&a[1][2];
            //cout<<p<<" g"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][3]&a[1][3]&a[2][3]&a[3][3])
        {
            p = a[0][3]&a[1][3];
            //cout<<p<<" h"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][0]&a[1][1]&a[2][2]&a[3][3])
        {
            p = a[0][0]&a[1][1];
            //cout<<p<<" i"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else if(a[0][3]&a[1][2]&a[2][1]&a[3][0])
        {
            p = a[0][3]&a[1][2];
            //cout<<p<<" j"<<endl;
            if(p == 1)
                printf("Case #%d: X won\n",k);
            else printf("Case #%d: O won\n",k);
        } else
        {
            //cout<<"k"<<endl;
            if(f == 1)
                printf("Case #%d: Game has not completed\n",k);
            else printf("Case #%d: Draw\n",k);
        }
        k++;
    }
}
