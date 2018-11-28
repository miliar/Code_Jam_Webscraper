/*

 E-Mail : mayank.ry@gmail.com
 Just For You :)

 */

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;


#define SMALL
//#define LARGE
int main()
{
    int d1,d2,N,arr[6][6],i,j,k,status,sum;
    char mark;

    #ifdef SMALL
	       freopen("A-small-attempt0.in","rt",stdin);
	       freopen("A-small.out","wt",stdout);
    #endif
    #ifdef LARGE
	       freopen("A-large.in","rt",stdin);
	       freopen("A-large.out","wt",stdout);
    #endif
    cin>>N;
    for(k =1;k<=N;k++)
    {
          printf("Case #%d: ",k);
          for(i=1;i<5;i++)
            {
                sum = 0;
                for(j=1;j<5;j++)
                {
                    cin>>mark;
                    //cout<<mark;
                    arr[i][j] = int(mark);
                    sum=sum+arr[i][j];
                    //printf("\n %c \n", (mark));
                }
                arr[i][5]=sum;

            }

            d1=0;
            d2=0;

            for(i=1;i<5;i++)
            {
                sum = 0;
                for(j=1;j<5;j++)
                {
                    sum=sum+arr[j][i];

                }
                d1=d1+arr[i][i];
                d2=d2+arr[i][5-i];
                arr[5][i]=sum;
            }

            status = 0;

            for(i=1;i<5;i++)
            {
                if (arr[i][5]<300 || arr[5][i]<300)
                {
                    status=1;
                }
                if (arr[i][5]==352 || arr[i][5]==348 || arr[5][i]==352 || arr[5][i]==348 || d1==352 || d1==348|| d2==352 || d2==348)
                {
                    status=2;
                    break;
                }

                if (arr[i][5]==316 || arr[i][5]==321 || arr[5][i]==316 || arr[5][i]==321 || d1==316 || d1==321|| d2==316 || d2==321)
                {
                    status=3;
                    break;
                }

            }
            if (status==0)
            printf("Draw \n");
            if (status==1)
            printf("Game has not completed\n");
            if (status==2)
            printf("X won \n");
            if (status==3)
            printf("O won\n");

    }

//              for(i =0;i<128;i++)
//           {
//                    printf("char %c code %d \n",char(i),i);
//
//           }
//           cout<<"\n";

	return 0;

}
