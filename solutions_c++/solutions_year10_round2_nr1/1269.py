#include<iostream>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#define max(a,b)(a>b?a:b)
#define min(a,b)(a<b?a:b)
#define inf 100000

using namespace std;

map<string,bool>mp;

int main()
{
    //freopen("A_small.in","r",stdin);
    //freopen("A_small.out","w",stdout);
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);


    int test,i,j,c,N,M,_case=1;
    char in[101];


    scanf("%d",&test);

    while(test--)
    {
        scanf("%d %d",&N,&M);

        for(i=0;i<N;i++)
        {
            scanf("%s",in);
            mp[in]=true;
            for(j=strlen(in)-1;j>0;j--)
                if(in[j]=='/'){
                    in[j]=0;
                    mp[in]=true;
                }
        }

        for(i=c=0;i<M;i++)
        {
            scanf("%s",in);
            //printf("%s\n",in);
            if(mp[in]==false){
                mp[in]=true;
                c++;
            }

            for(j=strlen(in)-1;j>0;j--)
                if(in[j]=='/'){
                    in[j]=0;
                    if(mp[in]==false){
                        mp[in]=true;
                        c++;
                    }
                    //printf("%s\n",in);
                }
        }
        printf("Case #%d: %d\n",_case++,c);
        mp.clear();
    }

    return 0;
}
