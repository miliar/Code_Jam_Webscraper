#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

int T, N, arr[10005];

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		int ans = 999999;
		memset(arr, 0, sizeof arr);
		fscanf(fin, "%d", &N);
		if (N == 0) {
            //printf("Case #%d: 0\n", z); 
            fprintf(fout, "Case #%d: 0\n", z); 
            continue;
        }
		for (int i = 1; i <= N; i++) {
			int temp;
			fscanf(fin, "%d", &temp);
			arr[temp]++;
		}
		int cur = 1;
		while (true) {
			if (cur == 10001) break;
			if (arr[cur] == 0) {
				cur++; continue;
			}
			//printf("%d\n", cur);
			int temp = cur;
			while (arr[temp+1] >= arr[temp]) temp++;
			ans = min(ans, temp-cur+1);
			int k = arr[cur];
			for (int i = cur; i <= temp; i++) {
				arr[i] -= 1;
			}
		}
		//printf("Case #%d: %d\n", z, ans);
		fprintf(fout, "Case #%d: %d\n", z, ans);
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

