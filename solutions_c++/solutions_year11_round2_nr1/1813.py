#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<iostream>
#include<algorithm>
#include<list>

using namespace std;

char arr[101][101];
double wp[101],owp[101],oowp[101];

double wwp[101][101];
int main(void){
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    char a = '0',b = '1', c = '.';
    for(int t = 0; t<T; t++)
    {
        int n;
        scanf("%d",&n);
        for(int i = 0; i<n; i++)
        {
            scanf("%s",arr[i]);
            
            double tot = 0.0, w = 0.0;
            for(int j = 0; j<n; j++)
            {
                if(arr[i][j] == b)
                    w += 1.0;
                if(arr[i][j] != c)
                    tot += 1.0;
            }
            wp[i] = w / tot;
        }
        
        for(int i = 0; i<n; i++)
        {
            for(int j = 0; j<n; j++)
            {
                if(arr[i][j] != c)
                {
                    double sum = 0.0, tot = 0.0;
                    for(int k = 0; k<n; k++)
                    {
                        if(k != i && arr[j][k] != c)
                        {
                            if(arr[j][k] == b)
                                sum+= 1.0;
                            tot += 1.0;
                        }
                    }
                    wwp[i][j] = sum / tot;
                }
            }
        }
        for(int i = 0; i<n; i++)
        {
            double tot = 0.0, sum = 0.0;
            for(int j = 0; j<n; j++)
            {
                if(arr[i][j] != c)
                {
                    sum += wwp[i][j];
                    tot += 1.0;
                }
            }
            owp[i] = sum / tot;
            //printf("***%lf\n",owp[i]);
        }
        
        for(int i = 0; i<n; i++)
        {
            double tot = 0.0, sum = 0.0;
            for(int j = 0; j<n; j++)
            {
                if(arr[i][j] != c)
                {
                    sum += owp[j];
                    tot += 1.0;
                }
            }
            oowp[i] = sum / tot;
        }
        
        printf("Case #%d:\n",t+1);
        for(int i = 0; i<n; i++)
        {
            printf("%lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
