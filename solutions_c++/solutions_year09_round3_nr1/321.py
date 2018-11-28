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

const int N = 1000;

char str[N];
int len ;

int v[N];

    void cal(LL z)
    {
        LL sum = 0;
        int i;
        for ( i=0;i<len;i++ )
        {
            sum = sum *z + v[(int)str[i]];
        }
        cout<<sum<<endl;
    }

    void work()
    {
        gets(str);
        len = strlen(str);
        int i,j;
        int z =0 ;
        memset(v,-1,sizeof(v));

        for ( i=0;i<len;i++ )
        if ( v[ (int)str[ i ]  ]  == -1 )
            v[(int)str[ i ]] = 1,z++;
        if (z == 1) z++;
//        printf("jinzhi = %d\n",z);//debug

        memset(v,-1,sizeof(v));
        v[ (int)str[0] ] = 1;
        j = 0;
        for ( i=0;i<len;i++ )
        if ( -1 == v[ (int)str[i] ] )
        {
            v[ (int)str[i] ] = j;
//            printf("%c = %d\n",str[i],v[ (int)str[i] ]);//debug
            j ++;
            if ( j == 1 ) j++;
        }
        cal((LL)z);
    }

int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    int cas;
    scanf("%d",&cas);getchar();
    for ( int i= 1;i<=cas;i++ )
    {
        cout<<"Case #"<<i<<": ";
        work();
    }
    return 0;
}

