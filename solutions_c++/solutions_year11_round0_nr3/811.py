#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for (int t=1;t<=test;t++){
		int n;
		scanf("%d",&n);
		vector<int> mas(n);
		int xor=0;
		for (int i=0;i<n;i++){
			scanf("%d",&mas[i]);
			xor^=mas[i];
		}
		printf("Case #%d: ",t);
		if (xor!=0){
			printf("NO\n");
			continue;
		}
		sort(mas.begin(),mas.end());
		int sum=0;
		for (int i=1;i<mas.size();i++)
			sum+=mas[i];
		printf("%d\n",sum);
	}
	return 0;
}