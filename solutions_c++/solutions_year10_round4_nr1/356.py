
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <vector>

using namespace std;

int k;
int d[100][100];
int dcheck[1000][1000];

inline bool check_array(const vector <int>& arr) {
	for(int i = 0; i < arr.size() / 2; i++)
		if(arr[arr.size()-1-i] != arr[i]
			&& arr[i] != -1 && arr[arr.size()-1-i] != -1)
			return false;
	return true;
}

bool check(int s, int x, int y) {
	memset(dcheck, -1, sizeof(dcheck));
	for(int i = 0; i < k; i++)
		for(int j = 0; j < k; j++)
			dcheck[i+x][j+y] = d[i][j];

	/*
	if(s==4&&x==1&&y==0) {
		printf("here\n");
		for(int j = 0; j < s; j++)
			for(int l = 0; l < s; l++)
				printf("%d%c", dcheck[j][l], l==s-1 ? '\n' : ' ');
	}
	*/
			
	for(int i = 0; i < s; i++) {
		vector <int> arr;
		for(int j = 0; j <= i; j++)
			arr.push_back(dcheck[s-i-1+j][j]);
		if(!check_array(arr))
			return false;
		
		arr.clear();
		for(int j = 0; j <= i; j++)
			arr.push_back(dcheck[j][s-i-1+j]);
		if(!check_array(arr))
			return false;	

		arr.clear();
		for(int j = 0; j <= i; j++)
			arr.push_back(dcheck[s-1-j][s-i-1+j]);
		if(!check_array(arr))
			return false;	
		
		arr.clear();
		for(int j = 0; j <= i; j++) // check
			arr.push_back(dcheck[i-j][j]);
		if(!check_array(arr))
			return false;	
	}
	return true;
}

bool check_all(int s) {
	for(int x = 0; x <= s-k; x++)
		for(int y = 0; y <= s-k; y++)
			if(check(s, x, y)) {
				//printf("%d %d %d\n", s, x, y);
				return true;
			}
	return false;
}

int solve() {
	for(int s = k; s <= 4*k; s++) {
		if(check_all(s))
			return s*s - k*k;
	}
	return -1;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d", &k);
		for(int j = 0; j < k; j++) {
			int total = j;
			for(int l = 0; l <= total; l++)
				scanf("%d", &d[total-l][l]);
		}
		for(int j = k; j < 2*k-1; j++) {
			int total = 2*k-j-2;
			for(int l = 0; l <= total; l++)
				scanf("%d", &d[k-1-l][k-1-total+l]);
		}
		/*
		for(int j = 0; j < k; j++)
			for(int l = 0; l < k; l++)
				printf("%d%c", d[j][l], l==k-1 ? '\n' : ' ');
		*/
		printf("Case #%d: %d\n", i+1, solve());
	}
	
	return 0;
}