#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define SZ size
#define SIZE(x) (int)(x).size()

#define MAX 2000010

int A, B;
bool was[MAX];
vector<int> nums;

int anal(int x) {
	int sum = 0;
	
	char buff[20];
	itoa(x, buff, 10);
	int len = strlen(buff);	
	nums.clear();
	
	for (int i = 0; i < len; i++) {
		buff[len+i] = buff[i];
		buff[i] = '0';
		buff[len+i+1] = '\0';
		//printf("%s\n", buff);
		int y = atoi(buff);
		if (y > x && y <= B) {
			//printf("%d %d\n", x, y);
			if (!was[y]) {
				was[y] = true;
				nums.PB(y);
				sum++;
			}
		}
	}
	
	for (int i = 0; i < SIZE(nums); i++) was[nums[i]] = false;
	
	return sum;
}

int main() {
	int T;
	scanf("%d", &T);
	cin.get();
	memset(was,0,MAX*sizeof(bool));
	
	for (int q = 1; q <= T; q++) {
		scanf("%d %d", &A, &B);
		
		int num = 0;
		for (int i = A; i <= B; i++) {
			num += anal(i);
		}
		
		printf("Case #%d: %d\n", q, num);
	}	
	return 0;
}