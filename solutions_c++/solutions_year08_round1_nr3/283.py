#include <cstdio>
#include <cmath>
using namespace std;

int values[31] = {0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,607,263,
	   		      151,855,527,743,351,135,407,903,791,135,647};

int main()
{
	int T;
	scanf("%d",&T);
	double d = log10(3+sqrt(5.0));
	for(int i=0;i<T;i++)
	{
		long n;
		scanf("%ld",&n);
		if (n<=17){
			double rez = floor(pow(10.0,n*d));
			double aux = floor(rez/1000)*1000;
			printf("Case #%d: %03d\n",i+1,(int)(rez-aux));
		}else
			printf("Case #%d: %03d\n",i+1,values[n]);
	}
	return 0;
}