#include <vector>
#include <list>
#include <algorithm>
#include <stdio.h>
using namespace std;

class set
{
public:
	bool merged;
	list<unsigned long> elems;
	list<unsigned long> primes;
	void merge(set& s)
	{
		//TODO: unique primes
		elems.merge(s.elems);
		primes.merge(s.primes);
	}
	set():merged(false) {}
	void print()
	{
		list<unsigned long>::iterator it=primes.begin();
		for(int i=0;i<primes.size();i++)
		{
			printf("%lu\n",*it);
			it++;
		}
		printf("\n");
	}

};

bool is_prime(unsigned long p)
{
	for(unsigned long i=2;i<p;i++)
		if(p%i==0)
			return false;
	return true;
}

void add_primes(set& s,unsigned long e,unsigned int P)
{
	for(unsigned int i=P;i<=e;i++)
	{
		if(e%i==0)
		{
			if(find(s.primes.begin(),s.primes.end(),i)==s.primes.end())
			{
				if(is_prime(i))
					s.primes.push_back(i);
			}
		}
	}
}

vector<set> v;

int main(int argc, char* argv[])
{
	FILE* f=fopen(argv[1],"r");
	int cases;
	fscanf(f,"%u\n",&cases);
	for(int h=0;h<cases;h++)
	{
		v.clear();
		unsigned int A,B,P;
		fscanf(f,"%u %u %u\n",&A,&B,&P);

		for(unsigned int i=A;i<=B;i++)
		{
			set a;
			a.elems.push_back(i);
			add_primes(a,i,P);
			v.push_back(a);
			//a.print();
		}
		for(unsigned int i=0;i<v.size();i++)
		{
			for(unsigned int j=0;j<v.size();j++)
			{
				if(i==j)
					continue;
				if(v[j].merged)
					continue;
				list<unsigned long>::iterator it=v[j].primes.begin();
				for(unsigned int k=0;k<v[j].primes.size();k++)
				{
					if(find(v[i].primes.begin(),v[i].primes.end(),*it)!=v[i].primes.end())
					{
						v[i].merge(v[j]);
						v[j].merged=true;
						continue;
					}
					it++;

				}

			}

		}
		int ret=0;
		for(unsigned int i=0;i<v.size();i++)
		{
			if(v[i].merged==false)
				ret++;
		}
		printf("Case #%u: %u\n",h+1,ret);
	}
	return 0;
}
