#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime[1000000];
vector<long long> prime;
void getPrime()
{
	for(long long i = 0; i < 1000000; i++)
	{
		isPrime[i] = true;
	}

	isPrime[0] = false;
	isPrime[1] = false;

	for(long long i = 2; i < 1000000; i++)
	{
		if(isPrime[i] == true)
		{
			prime.push_back(i);
			long long test = i * 2;
			while(test < 1000000)
			{
				isPrime[test] = false;
				test += i;
			}
		}
	}

}

bool compare(int a, int b)
{
	return(a < b);
}

void compare_sample()
{
	int myints[] = {32,71,12,45,26,80,53,33};
	vector<int> myvector (myints, myints+8);        
	vector<int>::iterator it;
	sort (myvector.begin()+4, myvector.end(), compare);
}
vector<vector<long long> > PT(502, vector<long long> (502, 1));

void create_pt()
{
	for(int i = 2; i <= 500; i++)
	{
		for(int j = 1; j < i; j++)
		{
			PT[i][j] = (PT[i-1][j-1] + PT[i-1][j]) % 100003;
		}
	}
}

long long c_x_get_y(long long x, long long y)
{
	if(y == 0)
		return 1;
	long long ans = 1;
	for(int i = 0; i < y; i++)
	{
		ans *= (x - i);
		ans /= (i + 1);
	}
	return ans;
}
int main()
{
	char c;
	int data_num, case_count = 1;
	cin >> data_num;
	while(data_num != 0)
	{
		cout << "Case #" << case_count << ": ";

		long long ans = 0;
		string A, B;
		cin >> A >> B;
		long long LA = 0, LB = 0;
		long long tmp = 1;
		for(int i = 0; i < A.size(); i++)
		{
			LA += (A[A.size() - i - 1] - '0') * tmp;
			tmp *= 10;
		}

		tmp = 1;
		for(int i = 0; i < B.size(); i++)
		{
			LB += (B[B.size() - i - 1] - '0') * tmp;
			tmp *= 10;
		}
		//cout << "LA = " << LA << endl;
		//cout << "LB = " << LB << endl;

		for(long long i = LA; i <= LB; i++)
		{
			//cout  << endl << "i=" << i << " ";
			if(i < 10)
				continue;
			vector<int> vi;
			long long tmp = i;
			while(1)
			{
				vi.insert(vi.begin(), tmp % 10);
				tmp = tmp / 10;
				if(tmp == 0)
					break;
			}
			//for(int iii = 0; iii < vi.size(); iii++)
				//cout << vi[iii];
			//cout << endl;
			bool yoyoyo;
			vector<long long> already;
			for(int ker = 1; ker < vi.size(); ker++)
			{
				vi.push_back(vi[0]);
				vi.erase(vi.begin());
				if(vi[0] == 0)
					continue;
				long long tmptmptmp = 0;
				long long tmptmp = 1;
				for(int j = 0; j < vi.size(); j++)
				{
					tmptmptmp += vi[vi.size() - j - 1] * tmptmp;
					tmptmp *= 10;
				}
				if(tmptmptmp <= LB && tmptmptmp > i)
				{
					bool flag = true;
					//cout << i << "->" << tmptmptmp << endl;
					for(int alalal = 0; alalal < already.size(); alalal++)
					{
						if(tmptmptmp == already[alalal])
						{
							flag = false;
							break;
						}
					}
					if(flag)
					{
						already.push_back(tmptmptmp);
						ans++;
					}
				}
				
			}
		}
		cout << ans;
		cout << endl;
		data_num--;
		case_count++;
	}
	return 0;

}
