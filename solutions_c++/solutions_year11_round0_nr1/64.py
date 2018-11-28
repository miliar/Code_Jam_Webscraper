#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int testCases, n, oIndex, bIndex, oCount, bCount;

int main(){
	scanf("%d", &testCases);
	for(int testCase = 1; testCase <= testCases; ++ testCase){
		scanf("%d", &n);
		oIndex = bIndex = 1;
		oCount = bCount = 0;
		for(int i = 1; i <= n; ++ i){
			char newSide;
			while(1){
				scanf("%c", &newSide);
				if(newSide == 'O' || newSide == 'B')
					break;
			}
			int newIndex;
			scanf("%d", &newIndex);
			if(newSide == 'O'){
				oCount = max(bCount, oCount + abs(oIndex - newIndex)) + 1;
				oIndex = newIndex;
			}else{
				bCount = max(oCount, bCount + abs(bIndex - newIndex)) + 1;
				bIndex = newIndex;
			}
		}
		printf("Case #%d: %d\n", testCase, max(oCount, bCount));
	}
	return 0;
}
