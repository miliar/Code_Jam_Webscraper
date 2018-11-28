#define _USE_MATH_DEFINES
#define INF 10000000
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>

using namespace std;

typedef long long ll;
typedef pair <int,int> P;
typedef pair <P,P> PP;
typedef pair <int,PP> PPP;

static const double eps = 1e-8;



int main(){
	int T;
	while(~scanf("%d",&T)){
		for(int t=0;t<T;t++){
			int N,S,p;
			scanf("%d",&N);
			scanf("%d",&S);
			scanf("%d",&p);



			int* status = new int[N]();
			for(int i=0;i<N;i++){
				int ggl;
				scanf("%d",&ggl);

				for(int x=0;x<=10;x++){
					for(int y=0;y<=10;y++){
						for(int z=0;z<=10;z++){
							if(x+y+z == ggl){
								if(max(x,max(y,z)) - min(x,min(y,z)) == 2){
									if(p <= max(x,max(y,z))) status[i] |= 1;
								}
								else if(max(x,max(y,z)) - min(x,min(y,z)) < 2){
									if(p <= max(x,max(y,z))) status[i] |= (1<<1);
								}
							}
						}
					}
				}
			}

			int sum=0;

			int sup_only=0;
			for(int i=0;i<N;i++){
				if(status[i] & 1 && (status[i]>>1) == 0){
					sup_only++;
				}

				else if((status[i]>>1) & 1){
					sum++;
				}
			}


			sum += sup_only <= S ? sup_only : S;

			printf("Case #%d: %d\n",t+1,sum);
			delete[] status;
		}
	}
}