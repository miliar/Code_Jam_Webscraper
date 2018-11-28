#include<iostream>
#include<fstream>
#include<bitset>
using namespace std;

class Patrick
{
	bitset<1002> num;
	long realNum;
public:
	Patrick()
	{
		reset();
	}
	
	void reset()
	{
		set(0);
	}
	
	void set(long n)
	{
		bitset<1002> buf(n);
		num = buf;
		realNum = n;
	}
	
	void add(long n)
	{
		bitset<1002> buf(n);
		
		num = num ^ buf;
		realNum += n;
	}
	
	long value()
	{
		return num.to_ulong();
	}
	
	long realValue()
	{
		return realNum;
	}
	
	static long comp(Patrick& p1, Patrick& p2)
	{
		return p1.realNum > p2.realNum ? p1.realNum : p2.realNum;
	}
};

class Divider
{
	bitset<1002> d;
public:
	Divider()
	{
		reset();
	}
	
	void reset()
	{
		bitset<1002> buf(1);
		d = buf;
	}
	
	long i(long j)
	{
		return d[j - 1];
	}
	
	void inc()
	{
		bitset<1002> buf(d.to_ulong() + 1);
		d = buf;
	}
};

long times(long n)
{
	long i, s = 1;
	for(i = 1; i <= n - 1; i++)
		s = s * 2;
	return s - 1;
}

int main()
{
	ifstream fin("q2.in");
	ofstream fout("q2.out");
	long T; // cases
	long N; // numbers
	long data[1000]; // bags
	long i, j, k, n, buf; // counter
	long max;
	Patrick pat[2];
	Divider div;
	
	fin >> T;
	
	for(i = 1; i <= T; i++)
	{
		fin >> N;

		for(j = 1; j <= N; j++)
		{
			fin >> data[j];
		}
		
		max = -1;
		n = times(N);
		div.reset();
		for(k = 1; k <= n; k++)
		{
			pat[0].reset();
			pat[1].reset();

			for(j = 1; j <= N; j++)
			{
				pat[div.i(j)].add(data[j]);
			}
			
			div.inc();
			
			if(pat[0].value() == pat[1].value())
			{
				buf = Patrick::comp(pat[0], pat[1]);
				if(buf > max) max = buf;
			}
		}
		
		fout << "Case #" << i << ": ";
		if(max == -1) fout << "NO"; else fout << max;
		fout << "\n";
	}
}