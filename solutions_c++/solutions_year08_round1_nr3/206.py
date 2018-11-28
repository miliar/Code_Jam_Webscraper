#include <cstdio>
#include <cmath>

// APFloat - http://www.apfloat.org/apfloat/
#include <apfloat.h>
#include <ap.h>

#include <iostream>
#include <sstream>
#include <string>

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)

apfloat FP3;

int calc(int n)
{
	apfloat res=pow(FP3,n);

	res = floor(res);
	res = fmod(res,1000);

	std::stringstream ss;
	ss << pretty << res;

	std::string s;
	s=ss.str();
	while (s.length()<3) s="0"+s;
	printf("%s",s.c_str());

	return 0;
}

void main()
{
	apinit();
	int N,n;
	scanf("%d", &N);

	apfloat FF = 5;
	FF.prec(200000);
	
	FP3 = sqrt(FF);
	FP3 +=3;

	FOR(nCase,1,N)
	{
		scanf("%d",&n);
		printf("Case #%d: ",nCase);
		calc(n);
		printf("\n");
	}
	apdeinit();
}
