#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int NN = 1; NN <= T; NN++)
	{
		int N;
		cin >> N;
		double cm[3] = {0}, cv[3] = {0};
		for(int i = 0; i < N; i++)
		{
			int pos[3], vel[3];
			for(int j = 0; j < 3; j++)
			{
				cin >> pos[j];
				cm[j] += pos[j];
			}
			for(int j = 0; j < 3; j++)
			{
				cin >> vel[j];
				cv[j] += vel[j];
			}
		}
		for(int j = 0; j < 3; j++)
		{
			cm[j] /= N;
			cv[j] /= N;
		}
		double cp[3], dp = 0;
		cp[0] = cv[1] * cm[2] - cv[2] * cm[1];
		cp[1] = cv[2] * cm[0] - cv[0] * cm[2];
		cp[2] = cv[0] * cm[1] - cv[1] * cm[0];
		for(int j = 0; j < 3; j++)
		{
			dp += cv[j] * cm[j];
		}
		double ans, time;
		double velocity = 0;
		for(int j = 0; j < 3; j++)
		{
			velocity += cv[j] * cv[j];
		}
		if(dp > 0 || fabs(velocity) < 1e-12)
		{
			ans = 0;
			for(int j = 0; j < 3; j++)
			{
				ans += cm[j] * cm[j];
			}
			ans = sqrt(ans);
			time = 0;
		}
		else
		{
			time = (-dp) / velocity;
			ans = 0;
			for(int j = 0; j < 3; j++)
			{
				ans += cp[j] * cp[j];
			}
			ans = sqrt(ans / velocity);
		}
		printf("Case #%d: %0.9lf %0.9lf\n", NN, ans, time);
	}

	return 0;
}
