#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>

#define PI 3.14159265358979
#define PB(x) push_back(x)
using namespace std;
typedef long long LL;
void debug_array(int i,int j,int data[]){while (i<j){cout<<"     [ "<<i<<" ] : "<<data[i];i++;}cout<<endl;}

const int N = 200000;

int len,str[N];
bool v[N];
int bs[10],bnum;

    int change(int b,int x)
    {
        len = 0;
        while (x >0)
        {
            str[len++] = x%b;
            x /= b;
        }
//        debug_array(0,len,str);//debug
        int i;
        int sum = 0;
        for ( i=0;i<len;i++ )
        sum += str[i] * str[i];
        return sum;
    }

    void show_inbase(int x,int b)
    {
        len = 0;
        while (x >0)
        {
            str[len++] = x%b;
            x /= b;
        }
        printf("x: %d   base : %d :",x,b);
        for (int  i=0;i<len;i++ )
        printf(" %d",str[i]);
        printf("\n");
    }

    bool check(int x,int b)
    {
        memset(v,0,sizeof(v));
        v[ x ] = 1;
        while (1)
        {
            int temp = change(b,x);
            if ( temp == 1 ) break;
            if ( v[ temp ] ) return 0;
            v[temp] = 1;
            x = temp;
        }
        return 1;
    }

    void inputing()
    {
        int i;
        char st[5];
        int num(0);
        bnum = 0;
        while (1)
        {
            scanf("%s", st);
            for (i = num = 0; st[i]; i++) num = num * 10 + st[i] - '0';
            bs[bnum++] = num;
            if (getchar() == '\n') break;
        }
    }

    void work()
    {
        int x,i;
        x = 10;
        int maxb = 2;
        for ( i=maxb;i<1000000;i++ )
        {
//            int b=10;
            int j;
//            if ( check(i,2) && check(i,3 ) && check(i,7) && check(i,9) && check(i,8 ) && check(i,5) )
            for ( j=0;j<bnum;j++ )
            if ( !check(i,bs[j]) )
            break;
            if ( j == bnum)
            {
                printf("%d\n",i);break;
            }

//            if ( check(i,3) )
//            {
//                printf("b:%d  x:%d\n",b,i);//debug
//                show_inbase(i,3);show_inbase(i,9);
//            }
        }
    }

int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    int cas;
    char str[100];
    scanf("%d",&cas);gets(str);
    for (int i=1;i<=cas;i++)
    {
        inputing();
        printf("Case #%d: ",i);
        work();
    }

    return 0;
}

