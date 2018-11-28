using namespace std;
#include<fstream>
int main()
{
	long long N, T, K, rez;
	int i;
	ifstream in("jam1.in"); ofstream out("jam1.out");
	in>>T;
	for(i = 1; i <= T; ++i)
	{
		in>>N>>K;
		rez = (K + 1) / (1<<N);
		out<<"Case #"<<i<<": ";
		if( rez * (1<<N) == K + 1) out<<"ON\n";
		else out<<"OFF\n";
	}
	return 0;
}
