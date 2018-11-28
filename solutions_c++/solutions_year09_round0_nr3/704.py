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

const int N = 1000;

struct node
{
    int a,b;
};

char str[N];
int data[30];
vector<node> vx[300];//char to pos ->pos
char orginal[]="welcome to code jam";

    void init()
    {
        strcpy(str,"welcome to code jam");
        int i;
        node temp;
        for (i=0;i<(int)strlen(str);i++)
        {
            temp.a = i;
            temp.b = i+1;
            vx[ (int)str[i] ].PB(temp);
        }



        //for debug
//        for ( i=0;i<300;i++ )
//        if (vx[i].size() > 0)
//        {
//            for (int j=0;j<(int)vx[i].size();j++ )
//            printf("%c -> %c  at pos %d\n",str[vx[i][j].a],str[vx[i][j].b],vx[i][j].a);
//        }

    }

    void work()
    {
        memset(str,0,sizeof(str));
        gets(str);
        memset(data,0,sizeof(data));
        data[0] = 1;//w
        int i,j;
        for ( i=0;i<(int)strlen(str);i++ )
        {
            char ch = str[i];
            for ( j=0;j<(int)vx[(int)ch].size();j++ )
            {
                data[ vx[(int)ch][j].b ] += data[vx[(int)ch][j].a];
                data[ vx[(int)ch][j].b ] %= 10000;
//                printf("at str %d %c  data[ %d ]  + data[ %d ]: %d   = %d  by %c -> %c\n",i,str[i],vx[(int)ch][j].b,vx[(int)ch][j].a,data[vx[(int)ch][j].a],data[ vx[(int)ch][j].b ],orginal[vx[(int)ch][j].a],orginal[vx[(int)ch][j].b]);
            }
        }
        printf("%04d\n",data[strlen(orginal)]);

    }

int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    init();

    int cas;
    scanf("%d",&cas);gets(str);
    for (int i=1;i<=cas;i++)
    {
        printf("Case #%d: ",i);
        work();
    }
//    gets(str);

    return 0;
}


