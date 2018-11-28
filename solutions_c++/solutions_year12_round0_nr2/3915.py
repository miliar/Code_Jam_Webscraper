#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int T, N, S, pmin;
	int score, rem, quot, pmax;
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>N>>S>>pmin;
		int *p_ns = new int[N];		// flag set to 1 if non-surprising score > pmin is possible
		int *p_s = new int[N];		// flag set to 1 if a surprising score > pmin is possible
		pmax = 0;
		for(int i=0; i<N; i++)
		{
			p_ns[i] = 0;
			p_s[i] = 0;
			cin>>score;
			// figure out p_ns and p_s
			rem = score % 3;
			quot = (score - rem)/3;
			switch (rem)
			{
			case 0:
				if(quot<=10 && quot>=pmin)
					p_ns[i] = 1;
				if(quot>=1 && quot<=9 && quot+1>=pmin)
					p_s[i] = 1;
				break;
			case 1:
				if(quot<=9 && quot+1>=pmin)
					p_ns[i] = 1;
				if(quot>=1 && quot<=9 && quot+1>=pmin)
					p_s[i] = 1;
				break;
			case 2:
				if(quot<=9 && quot+1>=pmin)
					p_ns[i] = 1;
				if(quot<=8 && quot+2>=pmin)
					p_s[i] = 1;
				break;
			}
			//cout<<score<<" "<<quot<<" "<<rem<<" "<<p_ns[i]<<" "<<p_s[i]<<endl;
			// Goal is to reduce S down to 0 using up entries in the following order of preference:
			// 1) p_ns = 0 and p_s = 1
			// 2) p_ns = 1 and p_s = 1
			// 3) p_ns = 0 and p_s = 0
			// 4) p_ns = 1 and p_s = 0	// MVP - we try our best not to include in S
			// I do this in 3 more passes outside this loop.
			// At any time S reduces to 0, we simply count the remaining non-surprising score > pmin's
			if(S == 0)
			{
				if(p_ns[i] == 1)
					pmax++;
				p_ns[i] = -1;
				p_s[i] = -1;
			}
			else
			{
				if(p_ns[i] == 0 && p_s[i] == 1)
				{
					pmax++;
					S--;
					p_ns[i] = -1;
					p_s[i] = -1;
				}
			}
		}
		for(int i=0; i<N; i++)
		{
			if(S == 0)
			{
				if(p_ns[i] == 1)
					pmax++;
				p_ns[i] = -1;
				p_s[i] = -1;
			}
			else
			{
				if(p_s[i] == 1)
				{
					pmax++;
					S--;
					p_ns[i] = -1;
					p_s[i] = -1;
				}
			}
		}
		for(int i=0; i<N; i++)
		{
			if(S == 0)
			{
				if(p_ns[i] == 1)
					pmax++;
				p_ns[i] = -1;
				p_s[i] = -1;
			}
			else
			{
				if(p_ns[i] == 0 && p_s[i] == 0)
				{
					S--;
					p_ns[i] = -1;
					p_s[i] = -1;
				}
			}
		}
		for(int i=0; i<N; i++)
		{
			if(S == 0)
			{
				if(p_ns[i] == 1)
					pmax++;
				p_ns[i] = -1;
				p_s[i] = -1;
			}
			else
			{
				if(p_ns[i] == 1 && p_s[i] == 0)
				{
					S--;
					p_ns[i] = -1;
					p_s[i] = -1;
				}
			}
		}
		for(int i=0; i<N; i++)
		{
			if(S == 0 && p_ns[i] == 1)
			{
				pmax ++;
				p_ns[i] = -1;
				p_s[i] = -1;
			}
		}
		cout<<"Case #"<<i+1<<": "<<pmax<<endl;

		delete[] p_ns;
		delete[] p_s;
	}
}

