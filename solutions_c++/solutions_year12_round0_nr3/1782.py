#include <iostream>
#include <cstdio>
#include <map>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

vector<int>  lists[700000];

int a[2000001];
int pow10[8] = {1,10,100,1000,10000,100000,1000000,10000000};
int c[8] = {0,0,1,3,6,10,15,21};
int listSize = 0;

int calcLen(int n)
{
	int len = 1;
	while(n/=10) {
		len++;
	}
	return len;
}

vector<int> createList(int n) {
	int len = calcLen(n);
	vector<int> list;
	for(int i = 0; i < len; i++) {
		int r = n % 10;
		n = n / 10;
		n = n + r * pow10[len-1];
		if(n < 2000001 && a[n] == 0) {
			a[n] = 1;
			list.push_back(n);
		}
	}
	return list;
}

void preProcess()
{	
	int index = 0;
	for(int i = 12; i <= 1999999; i++) {
		if(a[i] == 0) {
			vector<int> list = createList(i);
			if(list.size() > 1) {
				lists[index++] = list;
			}
		}
	}
	listSize = index;
}

int calc(int a, int b) 
{
	int answer = 0;
	for(int i = 0; i < listSize; i++) {
		int l = lists[i].size();
		int count = 0;
		for(int j = 0; j < l; j++) {
			if(lists[i][j] >= a && lists[i][j] <= b) {
				count++;
			}
		}
		answer = answer + c[count];
	}
	return answer;
}

int main()
{
	for(int i = 0; i <= 2000000; i++) a[i] = 0;
	preProcess();
	int test;
	scanf("%d", &test);
	for(int z = 1; z <= test; z++) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", z, calc(a,b));
	}
	return 0;
}
