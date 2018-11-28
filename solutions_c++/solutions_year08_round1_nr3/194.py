#include<iostream>
using namespace std;
int a[]={005,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cas,n;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		scanf("%d",&n);
		printf("Case #%d: %03d\n",ca,a[n-1]);
	}
}