#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int flip(int x, int sh){
	//printf("%d %d: ", x, sh);
	int ten = 1;
	for(int i = 0; i < sh; i++){
		ten *= 10;
		if(ten >= x)
			return -1;
		}
	
	int more = 1;
	for(int i = 0; more < x; i++)
		more *= 10;
		
	int rem = x % ten;
	if(rem < ten/10)
		return -2;
	//printf("%d\n", (rem * more / ten) + (x / ten));
	return (rem * more / ten) + (x / ten);
	}

int main(){
	int testcases;
	scanf("%d", &testcases);
	
	for(int testnum = 0; testnum < testcases; testnum++){
		printf("Case #%d: ", testnum+1);
		int a, b, f = 0, ans = 0;
		scanf("%d %d", &a, &b);
		//printf("(%d %d)\n", a, b);
		map<int, bool> buvo;
		
		int last = 0;
		for(int i = a; i <= b; i++){
			for(int j = 1; ((f = flip(i, j)) || true) && (f != -1); j++){
				//if(testnum == 2)
					//printf("(%d %d) %d\n", i, j, f);
				if(a <= f && f <= b && f >= 0 && i < f && !buvo[f]){
					//if(testnum == 3){
					//	printf("Success: %d %d: %d\n", i, j, f);
					//	if(last == f)
					//		cout << "ULTRA GAY" << endl;
					//	}
					ans++;
					buvo[f] = true;
					}
			}
			buvo.clear();
		}
		
		printf("%d\n", ans);	
		}
	
	return 0;
	}
