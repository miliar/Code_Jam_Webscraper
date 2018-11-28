#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
bool is(vector<int> a,int n){
	for(int i=0;i < a.size();i++)
		if(a[i] != 0 && a[i]%n != 0 && n%a[i] != 0) return false;

	return true;
}
int main()
{
	freopen("output.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testero = 1; testero <= testcase;testero++)
	{
		printf("Case #%d: ",testero);
		int l, r, n;
		bool fl= false;
		scanf("%d%d%d",&n,&l,&r);
		vector<int> a(n);
		for(int i =0; i< n;i++){
			scanf("%d",&a[i]);
		}
		for(int i = l; i <= r; i++){
			if(is(a,i))
			{
				printf("%d\n",i);
				fl = true;
				break;
			}
		}
		if(!fl) puts("NO");
	}

	
	return 0;
} 