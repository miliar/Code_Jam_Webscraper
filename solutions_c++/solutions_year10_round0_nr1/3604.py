#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    int t,i=0;
    scanf("%d", &t);
    while(++i <= t)
    {
	int N,K;
	std::string res("OFF");
	scanf("%d %d", &N, &K);
	int nthpw = pow(2,N);
	if (K == nthpw - 1) res = "ON";
	else
	{
	    K -= nthpw - 1;
	    if (K > -1 && K % nthpw == 0 ) res = "ON";
	}

	printf("Case #%d: %s\n", i, res.c_str());
    }

    return 0;
}
