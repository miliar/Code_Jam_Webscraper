#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#define CONST 1000000
#define INPUT fin
#define OUTPUT fout
#define ABS(a) (((a)>0)?(a):(-(a)))
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;
/*
int toint(string s)
{
	istringstream ss(s);
	int k;
	ss>>k;
	return k;
}

int sz(int k)
{
	int res=0;
	while(k)
	{
		res++;
		k/=10;
	}
	return res;
}

struct BigInt
{
	vector<int> vi;
	int sign;
	BigInt(string str)
	{
		if(str[0] == '-')
		{
			sign = -1;
			str = str.substr(1);
		}
		vi = vector<int>( MAX(1,(str.size() + 5) / 6), 0);
		vi[vi.size()-1] = toint(str.substr(0,str.size() % 6));
		str = str.substr(str.size() % 6);
		for(int i=vi.size()-2; i>=0; i--)
		{
			vi[i] = toint(str.substr(0,6));
			if(str.size() > 6)
			{
				str = str.substr(6);
			}
		}
	}
	BigInt(int k)
	{
		sign = (k>0) ? 1 : -1;
		vi.push_back(ABS(k));
	}
	BigInt operator *(int k)
	{
		BigInt result = (*this);
		if(k < 0)
		{
			result.sign *= -1;
			k = -k;
		}
		for(int i=0;i<result.vi.size(); i++)
			result.vi[i] *= k;
		for(int i=0;i<result.vi.size(); i++)	if(result.vi[i] > CONST)
		{
			if(i+1 < vi.size())
			{
				result.vi[i+1] += result.vi[i] / CONST;
			}
			else
			{
				result.vi.push_back(result.vi[i] / CONST);
			}
			result.vi[i] %= CONST;
		}
		return result;
	}
	BigInt operator +(BigInt other)
	{
		BigInt result = (*this);
		for(int i=0; i<result.vi.size(); i++)
		{
			result.vi[i] += other.vi[i];
		}
		for(int i=0;i<result.vi.size(); i++)
		{
			if(result.vi[i] > CONST)
			{
				if(i+1 < result.vi.size())
				{
					result.vi[i+1] += result.vi[i] / CONST;
				}
				else
				{
					vi.push_back(result.vi[i] / CONST);
				}
				result.vi[i] %= CONST;
			}
			if(result.vi[i] < CONST)
			{
				if(i+1<result.vi.size())
				{
					result.vi[i+1] -= 1;
					result.vi[i] += CONST;
				}
				else
				{
					
				}
			}
		}
		return result;
	}
	BigInt diff(BigInt other)
	{
		if((*this) > other)
		{
			return (*this) + (other * -1);
		}
	}
	BigInt operator >(BigInt other)
	{
		if(vi.size() != other.vi.size())
		{
			return vi.size() > other.vi.size();
		}
		return vi[vi.size()-1] > other.vi[other.vi.size() - 1];
	}
	BigInt operator <(BigInt other)
	{
		if(vi.size() != other.vi.size())
		{
			return vi.size() < other.vi.size();
		}
		return vi[vi.size()-1] < other.vi[other.vi.size() - 1];
	}
	string tostr(void)
	{
		ostringstream out;
		out<<vi[vi.size() - 1];
		for(int i=vi.size()-2;i>=0;i--)
		{
			out<<string(6-sz(vi[i]),'0')<<vi[i];
		}
		return out.str();
	}
};
*/

long long gcd(long long a, long long b)
{
	if(b == 0)	return a;
	return gcd(b,a%b);
}

int main()
{
	int C;
	ifstream fin("b.in");
	ofstream fout("b.out");
	INPUT>>C;
	for(int c=1;c<=C;c++)
	{
		int N;
		long long T;
		INPUT>>N;
		vector<long long> vi(N,0);
		for(int j=0;j<N;j++)
		{
			INPUT>>vi[j];
			
			if(1 == j)	T = ABS(vi[1] - vi[0]);
			
			for(int k=0;k<j;k++)
				T = gcd(T,ABS(vi[j] - vi[k]));
		}
		long long y = (T - (vi[0] % T)) % T;
		OUTPUT<<"Case #"<<c<<": "<<y<<"\n";
	}
	return 0;
}
