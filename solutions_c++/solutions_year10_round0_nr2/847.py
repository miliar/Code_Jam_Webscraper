// warning.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

class Bignum
{
public:
	vector<char> data;
	void absplus(const Bignum& rhs)
	{
		int e = 0;
		int n = rhs.data.size() > data.size()? rhs.data.size():data.size();
		for(int i = 0; i < n; i++)
		{
			int tmp;
			if((data.size() - 1) < i)
			{
				data.push_back(rhs.data[i]);
				tmp = rhs.data[i] + e;
			}else{
				if(rhs.data.size() > i)
				{
					tmp = data[i] + rhs.data[i] + e;
				}else{
					tmp = data[i] + e;
				}
			}

			if(tmp > 9)
			{
				data[i] = tmp%10;
				e = 1;
			}else{
				data[i] = tmp;
				e = 0;
			}
		}

		if(e == 1)
		{
			data.push_back(1);
		}
	}

	void absminus(const Bignum& rhs)
	{
		int e = 0;
		for(int i = 0; i < data.size(); i++)
		{
			if((rhs.data.size() - 1) < i)
			{
				if(data[i] >= e)
				{
					data[i] -= e;
					e = 0;
				}else{
					int tmp = data[i] + 10;
					tmp -= e;
					data[i] = tmp;
					e = 1;
				}
			}else{

				if(data[i] >= (rhs.data[i]+e))
				{
					data[i] = data[i] - rhs.data[i] - e;
					e = 0;
				}else{
					int tmp = data[i] + 10;
					tmp -= (rhs.data[i] + e);
					data[i] = tmp;
					e = 1;
				}
			}
		}

		while(data.back() == 0)
		{
			data.pop_back();
			if(data.empty())
			{
				data.push_back(0);
				break;
			}
		}
	}

	void mod(const Bignum& rhs)
	{
		while(rhs < (*this) || rhs == (*this))
		{
			absminus(rhs);
		}
	}

	bool operator<(const Bignum& rhs) const
	{
		if(rhs.data.size() != data.size()){
			return data.size() < rhs.data.size();
		}else{
			for(int i = 0; i < data.size(); i++)
			{
				int index = data.size() - i - 1;
				if(data[index] != rhs.data[index])
					return data[index] < rhs.data[index];
			}
		}
		return false;
	}

	bool operator==(const Bignum& rhs) const
	{
		if(rhs.data.size() != data.size()){
			return false;
		}else{
			for(int i = 0; i < data.size(); i++)
			{
				if(data[i] != rhs.data[i])
					return false;
			}
		}
		return true;
	}

	const Bignum& operator=(const Bignum& rhs)
	{
		data.clear();
		for(int i = 0; i < rhs.data.size(); i++)
		{
			data.push_back(rhs.data[i]);
		}
		return *this;
	}

	char* c_str() const
	{
		char* res = new char[data.size()+1];
		for(int i = 0; i < data.size(); i++)
		{
			res[i] = data[data.size() - i - 1] + '0';
		}
		res[data.size()] = 0;
		return res;
	}
};


Bignum gcd(Bignum x,Bignum y)
{
	while(!(x == y))
	{
		if(y < x)
			x.absminus(y);
		else
			y.absminus(x);
	}
	return x;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin = fopen("b.in","r");
	FILE* fout = fopen("b.out","w");
	int line;
	fscanf(fin,"%d\n",&line);
	for(int i = 0; i < line; i++)
	{
		printf("case %d\n",i+1);
		int n;
		fscanf(fin,"%d ",&n);
		vector<Bignum> T;
		for(int j = 0; j < n; j++)
		{
			char ch = fgetc(fin);
			vector<char> tmp;
			while(ch != ' ' && ch != '\n')
			{
				tmp.push_back(ch);
				ch = fgetc(fin);
			}
			Bignum t;
			while(!tmp.empty())
			{
				t.data.push_back(tmp.back() - '0');
				tmp.pop_back();
			}
			T.push_back(t);
		}
		sort(T.begin(), T.end());

		while(1)
		{
			bool unique = true;
			for(vector<Bignum>::iterator it = T.begin() + 1; it != T.end(); it++)
			{
				if(*it == *(it-1))
				{
					T.erase(it);
					unique = false;
					break;
				}
			}
			if(unique)
				break;
		}

		Bignum q = T[1];
		q.absminus(T[0]);
		for(int j = 0; j < T.size() - 1; j++)
		{
			Bignum p = T[j+1];
			p.absminus(T[j]);
			q = gcd(q,p);
		}
		
		Bignum one;
		one.data.push_back(1);
		if(q == one)
		{
			fprintf(fout, "Case #%d: %d\n",i+1,0);
		}else{
			Bignum t = T[0];
			t.mod(q);
			Bignum zero;
			zero.data.push_back(0);
			if(t == zero)
			{
				fprintf(fout,"Case #%d: 0\n",i+1);
			}else{
				q.absminus(t);
				char* p = q.c_str();
				fprintf(fout,"Case #%d: %s\n",i+1,p);
				delete [] p;
			}
		}
	}
	fclose(fout);
	fclose(fin);
	return 0;
}

