#include <cmath>

#include <iomanip>
#include <iostream>

using namespace std;

void output_result(double probability)
{
	static int case_id = 0;
	cout << "Case #" << ++case_id << ": " << probability << endl;
}

struct data_set
{
	double f, R, t, r, g;
};

istream &operator>>(istream &in, data_set &data)
{
	return in >> data.f >> data.R >> data.t >> data.r >> data.g;
}

void solve(data_set &data)
{
	// Exceptions.
	data.t += data.f;
	data.r += data.f;
	data.g -= data.f * 2.0;
	if (data.g <= 0.0 || data.r >= data.R - data.t)
	{
		output_result(1.0);
		return;
	}

	double total_area = M_PI * data.R * data.R;
	double inner_r = data.R - data.t;
	double inner_area = M_PI * inner_r * inner_r;

	double g_and_r = data.g + (data.r * 2.0);
	double rev_g_and_r = 1.0 / g_and_r;
	double r_ratio = data.r / g_and_r;
	double square_inner_r = inner_r * inner_r;

	int num_steps = 1 << 24;
	double step = inner_r / num_steps;
	double sum = 0.0;
	for (int i = 0; i < num_steps; ++i)
	{
		double x = step * i;
		double y = sqrt(square_inner_r - x * x);

		double x_ratio = x * rev_g_and_r;
		x_ratio -= floor(x_ratio);
		if (x_ratio > 0.5)
			x_ratio = 1.0 - x_ratio;
		if (x_ratio < r_ratio)
		{
			sum += y;
			continue;
		}

		double y_ratio = y * rev_g_and_r;
		double y_floor = floor(y_ratio);
		sum += (data.r * 2.0) * y_floor;
		y_ratio -= y_floor;

		if (y_ratio > r_ratio)
		{
			sum += data.r;
			y_ratio = 1.0 - y_ratio;
			if (y_ratio < r_ratio)
				sum += (r_ratio - y_ratio) * g_and_r;
		}
		else
			sum += y_ratio * g_and_r;
	}
	sum /= (num_steps + 1);
	sum *= inner_r;

	double hit_area = total_area - inner_area + sum * 4;
	output_result(hit_area / total_area);

//	hit_area = total_area - inner_area;
//	output_result(hit_area / total_area);
}

int main()
{
	cout << setprecision(6);
	cout << setiosflags(ios::fixed);

	int num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		data_set data;
		cin >> data;

		solve(data);
	}

	return 0;
}
