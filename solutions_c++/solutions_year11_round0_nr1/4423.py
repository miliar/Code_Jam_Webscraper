#include<iostream>


using namespace std;


int deal (int N)
{
	
	char robot;
	int nextPosi;

	int currentPosiOrange	= 1;
	int currentPosiBlue		= 1;
	int overSecondsOrange	= 0;
	int overSecondsBlue		= 0;
	int sum	= 0;

	for (int i = 0; i < N; i ++) 
	{
		cin>>robot;
		int tmp;
		if(robot == 'O') {
			cin>>nextPosi;
			tmp = nextPosi - currentPosiOrange;
			if(tmp < 0) { tmp = 0 - tmp; }
			currentPosiOrange = nextPosi;

			tmp = tmp - overSecondsBlue;
			if(tmp < 0) { tmp = 0; }
			
			overSecondsBlue = 0;
			overSecondsOrange += tmp + 1;
			sum += tmp + 1;
		} else if(robot == 'B') {
			cin>>nextPosi;
			tmp = nextPosi - currentPosiBlue;
			if(tmp < 0) { tmp = 0 - tmp; }
			currentPosiBlue = nextPosi;

			tmp = tmp - overSecondsOrange;
			if(tmp < 0) { tmp = 0; }

			overSecondsOrange = 0;
			overSecondsBlue += tmp + 1;
			sum += tmp + 1;
		}
	}

	return sum;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("AOut.txt", "w", stdout);
	
	int cases	= 0;
	int N		= 0;
	cin>>cases;

	for (int i = 1; i <= cases; i ++)
	{
		cin>>N;
		cout<<"Case #"<<i<<": "<<deal(N)<<endl;
	}

	cin>>N;
	return 0;
}
