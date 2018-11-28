#include <iostream>
#include <vector>

using namespace std;

/** FOR LARGE INPUT */

int main()
{
	int T, N;
	vector< pair<int,int> > v;
	int num1, num2, inter;
	scanf("%d", &T);

	for(int test = 0; test < T; test++) {
		//Init
		v.clear();
		inter = 0;

		//Input
		scanf("%d", &N);
		for(int i=0; i<N; i++) {
			scanf("%d", &num1);
			scanf("%d", &num2);
			v.push_back(pair<int,int>(num1,num2));
		}

		//Processing
		if(v.size() == 1) {
			inter = 0;
		} else {
			//Now, loop!
			for(int i=0; i<v.size(); i++) {
				for(int j = i+1; j < v.size(); j++) {
					if((v[i].first > v[j].first && v[i].second > v[j].second) || (v[i].first < v[j].first && v[i].second < v[j].second)) {
						;
					} else {
						inter += 1;
					}
				}
			}
		}

		//Output
		printf("Case #%d: %d\n", test+1, inter);
	}

	return 0;
}


