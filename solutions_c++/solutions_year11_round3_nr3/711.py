#include<cstdio>
#include<iostream>
using namespace std;
int num[200000];
void work(int x)
{
	int n, a, b;

        printf("Case #%d: ",x);
		cin >> n >> a >> b;
		for(int i = 0; i < n; i++)cin >> num[i];
		for(int i = a; i <=b; i++){
			bool can = true;
			for(int j = 0; j <n; j++)if(i % num[j] != 0 && num[j] %i != 0){
					can = false;
					break;
				}
			if(can){
				cout << i << endl;
				return;
			}
		}
		cout << "NO" << endl;
}
int main()
{
        int t;
        scanf("%d",&t);
        for(int i = 1; i <= t; i++)work(i);
}
