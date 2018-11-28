/*

TASK:
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<set>
#include<algorithm>
#include<iostream>
#define INF 123456789

using namespace std;
FILE *fin,*fout;

inline int MAXX(int x,int y) {return x > y ? x : y ;}
inline int MINN(int x,int y) {return x < y ? x : y ;}
int comparez(const void *x, const void *y)
{
    return (*(int*)x - *(int*)y);
}

//-----------------------------------------------------

int tl;
long long a[503][503]={0};
long long c[503][503]={0};

int main()
{
    int i,j,k,st;
    char filename[100];
    cin >> filename;
    fin = fopen(strcat(filename, ".in"),"r");
    fout = fopen(strcat(filename, ".out"),"w");
    fscanf(fin,"%d",&tl);
    
    for(i=0;i<=500;i++) {c[i][0] = 1; c[i][i] = 1;}
    for(i=1;i<=500;i++)
    {
        for(j=1;j<=i;j++)
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % 100003;
    }
    
    //for(i=2;i<=n;i++) for(j=i+1;j<=n;j++) a[i][j] = 0;
    /*
    for(j=2;j<=500;j++) a[1][j] = 1;
    for(i=1;i<=500-1;i++)
    {
        for(j=i+1;j<=500;j++)
        {
            st = 2*j-i;
            for(k=st;k<=500;k++)
            {
                a[j][k] = (a[j][k] + c[k-j-1][j-i-1]) % 100003;
            }
        }
    }
    */
    
    for(j=2;j<=501;j++) a[1][j] = 1;
    for(i=2;i<=501-1;i++)
    {
        for(j=i+1;j<=501;j++)
        {
            for(k=1;k<i;k++)
            {
                if(c[j-i-1][i-k-1] > 0)
                    a[i][j] = (a[i][j] + a[k][i]*c[j-i-1][i-k-1]) % 100003;
            }
        }
    }
    
    for(i=1;i<=25;i++) {for(j=1;j<=25;j++) cout << a[i][j] << " "; cout << endl;}
    

    for(int tt=0;tt<tl;tt++)
    {
        fprintf(fout,"Case #%d: ",tt+1);
        int n;
        fscanf(fin, "%d", &n);
        long long ans = 0;
        for(i=1;i<n;i++) ans = (ans + a[i][n]) % 100003;
        fprintf(fout, "%lld\n", ans);
    }
    system("PAUSE");
    return 0;
}
