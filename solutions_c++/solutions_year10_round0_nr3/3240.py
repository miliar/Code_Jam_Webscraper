#include <cstdio>
#include <cstdlib>
#include <list>

using namespace std;
int main(){
	int c = 0, cases = 0;
	FILE *file = fopen("smallpark.txt", "r"), *out = fopen("smallparkout.txt", "w");
	fscanf(file, "%d", &cases);
	while(c++ < cases){
		int r = 0, k = 0, g = 0, gs = 0, sum = 0;
		fscanf(file, "%d %d %d", &r, &k, &g);
		list<int> gsize;
		for(int i = 0; i < g; i++){
			fscanf(file, "%d", &gs);
			gsize.push_back(gs);
		}
		while(r--){
			list<int> requeue;
			int kride = 0, size = gsize.size();
			while(size-- && (kride+gsize.front()) <= k){
				kride += gsize.front();
				requeue.push_back(gsize.front());
				gsize.pop_front();
			}
			size = requeue.size();
			while(size--){
				gsize.push_back(requeue.front());
				requeue.pop_front();
			}
			sum += kride;
		}
		fprintf(out, "Case #%d: %d\n", c, sum);
	}
	return 0;
}