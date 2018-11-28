#include <iostream>

using namespace std;

void process(void)
{
	int n;
	long long k;
	cin >> n >> k;
	if( ((k+1) % (1<<n)) == 0 )
		cout << "ON" << endl;
	else
		cout << "OFF" << endl;
}

int main(void)
{
	int N;
	cin >> N;
	for(int i=1;i<=N;i++)
	{
		cout << "Case #" << i << ": ";
		process();
	}
	return 0;
}