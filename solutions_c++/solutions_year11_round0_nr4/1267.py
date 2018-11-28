#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;

double Change(int i)
{
	if(i == 1)
		return 0;
	if(i == 2)
		return 1;
	else if(i == 3)
		return 2;
	else if(i == 4)
		return 9;
	else if(i == 5)
		return 44;
	else
		return (i - 1)*(Change(i - 1) + Change(i - 2));
}


double Select(int i, int j)
{
	if(j == 0)
		return 0;
	else if(j == i)
		return 0;
	if(i - j < j)
		return Select(i, i - j);
	double ans1 = 1;
	double ans2 = 1;
	for(int k = 1; k <= j; k++ )
		ans2 *= k;
	for(int k = i - j + 1; k <= i; k++)
		ans1 = ans1*k;
	return ans1/ans2;
}

double Product(int i)
{
	double ans = 1;
	for(int j = 1; j <= i; j++)
		ans *= j;
	return ans;
}

double Expectation(int i)
{
	if(i == 0)
		return 0;
	if(i == 1)
		return 0;
	if(i == 2)
		return 2;
	else
	{
		double ans = 0;
		double temp;
		temp = Product(i);
		ans = 1.0;
		for(int j = 1; j < i; j++)
		{
			ans += Select(i,j)*Change(i - j)*Expectation(i - j)/temp;
		}
		ans = ans*temp/(temp - Change(i));
		return ans;
	}
}

bool check(bool * flag, int N)
{
	for(int i = 0 ;i < N; i++)
	{
		if(flag[i] == false)
			return false;
	}
	return true;
}

double solve(std::vector<int> & V)
{
	double ans = 0;
	int * Combine = new int[V.size()];
	bool * flag = new bool[V.size()];
	int temp;
	for(int i = 0; i < V.size(); i++)
	{
		Combine[i] = 0;
		flag[i] = false;
	}
	std::vector<int> ball;
	std::vector<int> box;
	while(!check(flag,V.size()))
	{
		ball.clear();
		box.clear();
		for(int i = 0; i < V.size(); i++)
		{
			if(flag[i] == true)
				continue;
			ball.push_back(V[i]);
			box.push_back(i+1);
			flag[i] = true;
			break;
		}
		while(ball[ball.size() - 1] != box[0])
		{
			temp = ball[ball.size() - 1];
			flag[temp - 1] = true;
			box.push_back(temp);
			ball.push_back(V[temp - 1]);
		}
		Combine[ball.size() - 1]++;
	}
	for(int i = 0; i < V.size(); i++)
	{
		if(Combine[i] != 0 && i != 0)
		{
			ans += Expectation(i+1)*Combine[i];
		}
	}
	return ans;
}

int main()
{
	int T;
	int N;
	ifstream fin("D-small.in");
	fin>>T;
	ofstream fout("D-small-ans.out");
	std::vector<int> V;
	int temp;
	double ans;
	for(int i = 1; i <= T; i++)
	{
		V.clear();
		fin>>N;
		for(int j = 0; j < N; j++)
		{
			fin>>temp;
			V.push_back(temp);
		}
		ans = solve(V);
		fout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}