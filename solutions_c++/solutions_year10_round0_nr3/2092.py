#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	int c, t, R, K, N;
	int i, tmp, cnt, total, j;
	vector<int> nQueue, tmpQueue;

	scanf("%d", &t);	

	for(c = 0; c < t; c ++) {
		scanf("%d %d %d", &R, &K, &N);

		for(i = 0; i < N; i++) {
			scanf("%d", &tmp);
			nQueue.push_back(tmp);
		}

		total = 0;
		for(i = 0; i < R; i ++) {
			tmp = nQueue[0];

			cnt = 0;
			while(cnt + tmp <= K) {
				cnt += tmp;
				nQueue.erase(nQueue.begin());
				tmpQueue.push_back(tmp);

				if(nQueue.size() == 0) {					
					break;
				}

				tmp = nQueue[0];
			}

			for(j = 0; !tmpQueue.empty(); j ++) {
				nQueue.push_back(tmpQueue[0]);
				tmpQueue.erase(tmpQueue.begin());
			}

			total += cnt;
		}

		printf("Case #%d: %d\n", c+1, total);


		/*
		for(i = 0; i < nQueue.size(); i ++){
			printf("%d ", nQueue[i]);
		}		
		printf("\n");
		*/

		nQueue.clear();
	}	
}
//nQueue.erase(nQueue.begin());