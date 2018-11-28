#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define BROKEN printf("Broken\n");continue;
#define SIZE 1000

#define IN freopen("C-small-attempt0.in","r",stdin);
#define OUT freopen("C-small-attempt0.out","w",stdout);

int T,A,B;

int main()
{
	IN
	OUT
	int i,j,k,t,count,num;
	char temp[SIZE+10];

	scanf("%d",&T);
	for(t=1;t<=T;t++){
        count = 0;
        scanf("%d %d",&A, &B);

        for(num=A;num<B;num++){

            int nd = ceil( log(num) / log(10) );

            map<int, int> freq;

            for(j=1;j<nd;j++){
                int p = pow(10, j);
                int nn = (num % p) * pow(10, nd - j) + (num / p);

                if(freq[nn] == 1) continue;

                if(nn > num && nn <= B){
                    count++;
                    freq[nn]++;
                    //printf("%d %d\n",num, nn);
                }

            }
        }

        printf("Case #%d: %d\n",t,count);
	}
	return 0;
}
