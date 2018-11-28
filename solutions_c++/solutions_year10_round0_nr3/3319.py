#include <cstdio>
#include <deque>
using namespace std;

int t,r,k,n;
int tmp, sum, earnings;
deque<int> roller;

int main() {
	scanf("%d",&t);
	for(int i=0;i<t;++i) {
		scanf("%d %d %d",&r,&k,&n);
		for(int j=0;j<n;++j) {
			scanf("%d",&tmp);
			roller.push_back(tmp);
		}
		for(int j=0;j<r;++j) {
			sum = 0;
			if(n>1) {
				for(deque<int>::iterator iter=roller.begin();iter!=roller.end();iter++) {
					sum+=(*iter);
					if(sum>k) {
						sum-=(*iter);
						earnings+=sum;
						for(deque<int>::iterator iter2=roller.begin();iter2!=iter;iter2++) {
							roller.push_back(*iter2);
							roller.pop_front();
						}
						sum=0;
						break;
					}
				}
				earnings+=sum;
			} else {
				if(roller[0]<=k) {
					earnings = r*roller[0];
				} else {
					earnings = 0;
				}
			}
		}
		printf("Case #%d: %d\n",(i+1),earnings);
		earnings=0;
		roller.clear();
	}
	return 0;
}
