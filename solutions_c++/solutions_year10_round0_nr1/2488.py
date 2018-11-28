#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int pow2(int x ,int y)
{
    int temp=1;
    for (int i=0;i<y;i++)
    temp=temp*x;
    return temp;
    }

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N, K;
	int temp;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d", &N);
		scanf("%d", &K);
		temp=pow2(2,N);
		if (K==0)
		    printf("Case #%d: OFF\n",t+1);
		else if ((K+1)%temp==0) 
			printf("Case #%d: ON\n",t+1);
		else
			printf("Case #%d: OFF\n",t+1);
	}
}
