//...
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <iostream>
#include <list>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int main (){
	//freopen("in.txt", "r", stdin);//freopen("out.txt", "w", stdout);
	int n;
	char a[200];
	char b[]={'-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-',' ','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d\n", &n);
	for(int k=1;k<=n;++k){
		gets(a);
		printf("Case #%d: ", k);
		for(int i=0;a[i];++i){
			printf("%c", b[a[i]]);
		}
		
		printf("\n");
	}
	
	return 0;
}
