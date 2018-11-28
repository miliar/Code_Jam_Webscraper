#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
#define all(i) (i).begin(), (i).end()

int main()
{
/*
   freopen("inputB2.txt","r",stdin);
   freopen("outputB2.txt","w",stdout);
*/
    int test,i,j,n,s,p,min_surp,min_notsurp,cnt_surp,aux,c;
    scanf("%d",&test);
    REP(i,test)
    {
        scanf("%d %d %d ",&n,&s,&p);
        //n=number of googlers
        //s=number of surprise triplets scores
        if(p!=1 && p!=0)
        {
            min_surp=p+2*(p-2);
            min_notsurp=p+2*(p-1);
        }
        else
            min_surp=min_notsurp=p;

        cnt_surp=s;
        aux=0;
        REP(j,n)
        {
            scanf("%d",&c);
            if(c>=min_notsurp)
            {
                aux++;
            }
            else if(c>=min_surp && c<min_notsurp && cnt_surp)
            {
                aux++;
                cnt_surp--;
            }
        }
        printf("Case #%d: %d\n",i+1,aux);
    }

/*
	fclose(stdin);
	fclose(stdout);
*/
   return 0;
}
