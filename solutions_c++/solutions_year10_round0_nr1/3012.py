#include <iostream>
#include <string>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void solve()
{
	int iCaseNum;
	int N, K;
	scanf("%d %d", &N, &K);
	
	if( ( K&( (1<<N)-1 ) ) == (1<<N)-1 ) {
		Output("ON");
	}
	else {
		Output("OFF");
	}
	/*
	int iSnapedTimes = K;
	bool bState = true;
	
	for(int i = 0; i < N; i++) {
		bState &= bool(iSnapedTimes & 1);
		iSnapedTimes >>= 1;
	}

	if( bState ) {
		Output("ON");
	}
	else {
		Output("OFF");
	}
	*/
}

void GCJ2010_RoundQ_A()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_RoundQ_A();
	return 0;
}
