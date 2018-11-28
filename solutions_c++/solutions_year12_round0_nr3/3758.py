#include <cstdio>
#include <vector>
#include <set>

using namespace std;
int main(){
	int TC;
	scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++){
		set<pair<int, int> > s;
		int a, b;
		scanf("%d %d", &a, &b);
		for(int i=a; i<=b; i++){
			vector<int> v, bv;
			int tmp = i;
			while(tmp){
				bv.push_back(tmp%10);
				tmp/=10;
			}
			int size = (int)bv.size();
			for(int j=0; j<size; j++) v.push_back(bv[size-1-j]);
			for(int j=0; j<size; j++){
				int num = 0;
				for(int k=0; k<size; k++){
					num *= 10;
					num += v[(j+k)%size];
				}
				if(i<num && num <=b) {
					s.insert(make_pair(i, num));
				}
			}
			bv.clear();
			v.clear();
		}
		printf("Case #%d: %d\n", tc, s.size());
	}
	return 0;
}
