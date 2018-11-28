#include <iostream>

using namespace std;

int main(int argc, char ** argv, char ** env)
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		int N;
		cin >> N;
		uint32_t sum=0, x=0, min=4294967295u, c;
		for(int n=0; n<N; ++n)
		{
			cin >> c;
			if(c<min)
				min = c;
			sum+=c;
			x^=c;
		}
		cout << "Case #" << t << ": ";
		if(x)
			cout << "NO";
		else
			cout << sum-min;
		cout << endl;
	}
	return 0;
}
