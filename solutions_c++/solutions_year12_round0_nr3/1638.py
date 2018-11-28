#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>

using namespace std;

bool visited[2000001];
int a,b;


int count(int num) {

	if (visited[num]) return 0;
	visited[num]=true;
	int t=1;
	while (t<=num) t*=10;
	
	int ret=1;
	int tmp=num;
	while (1) {
		num=num*10;
		num=num%t+num/t;
		
		if (num<a||num>b) continue;
		
		if (!visited[num]) {
			ret++;
			visited[num]=true;
		}
		if (tmp==num) break;
	}
	return ret;
}

int main() {
	int n;
	
	cin>>n;
	int k=0;
	
	
	
	while (k++<n) {
		cin>>a>>b;
		memset(visited, 0, sizeof(visited));
		
		long long res=0;
		for (int i=a;i<b;i++) {
			int c=count(i);
			res+=c*(c-1)/2;
		}
		
		cout<<"Case #"<<k<<": "<<res<<endl;
	}
	
	
	
	return 0;
}


