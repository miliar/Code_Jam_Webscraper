#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int a[32] = {0,5,27,143,751,935,
			607,903,991,335,47,
			943,471,55,447,463,
			991,95,607,263,151,
			855,527,743,351,135,
			407,903,791,135,647};

int main()
{
	int nca,ca,n;
	long long m;
	double ans,tmp;
 	freopen("C-small-attempt3.in","r",stdin);
 	freopen("12.out","w",stdout);
	scanf("%d",&nca);
	for(ca=1;ca<=nca;ca++)
	{
		scanf("%d",&n);
		printf("Case #%d: %03d\n",ca,a[n]);
	}
	return 0;
}