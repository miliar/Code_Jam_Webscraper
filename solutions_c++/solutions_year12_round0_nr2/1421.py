#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#define MEX 101
using namespace std;

int store[MEX];

int main() {

	int test=0, i=0, count=1, N=0, s=0, p=0;
	int surprised=0, result=0, ann=0;;	
		
	scanf("%d",&test);
	while(count <= test) {
		scanf("%d %d %d",&N,&s,&p);
		for(i=0; i<N; ++i) {
			scanf("%d",&store[i]);
		}
		for(i=0, result=0, surprised=0; i<N; ++i) {
			if(store[i]%3 == 1) {
				ann = (store[i]-1)/3;
				if(ann+1 >= p) {
					++result;
				}
			}
			else if(store[i]%3 == 2) {
				ann = (store[i]-2)/3;
				if(ann+1 >= p) {
					++result;
				}
				else if(ann+2 >= p) {
					if(store[i]!=29)
						++surprised;
				}
			}
			else {
				ann = store[i]/3;
				if(ann >= p) {
					++result;
				}
				else if(ann+1 >= p) {
					if(store[i]!= 30 && store[i]!= 0) {
						++surprised;
					}
				}
			}
		}
		if(surprised > s) {
			result += s;
		}
		else {
			result += surprised;		
		}
		printf("Case #%d: %d\n",count, result);
		++count;
	}

	return 0;
}
