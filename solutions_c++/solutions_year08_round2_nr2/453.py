#include<iostream>
#include<vector>
#include<fstream>
#include<cstdlib>
#include<algorithm>

using namespace std;


bool ae_is_prime(unsigned int n);
int main()
{
	int N;
	ifstream fin("B-small.in",ifstream::in);
	fin>>N;
	for(int i=1;i<=N;i++)
	{
		int A,B,P;
		fin>>A;
		fin>>B;
		fin>>P;

		vector<int> num;;	
		vector<int> set;	
		vector<int> prime;

		int ctr = 1;
		for(int j=A;j<=B;j++)
		{
			num.push_back(j);
			set.push_back(ctr);
			ctr++;
		}

		unsigned int j = P;

		while(j <= B)
		{
			if(ae_is_prime(j))
				prime.push_back(j);	
			j++;
		}

		for(int j=0;j<num.size()-1;j++)
		{
			for(int k=j+1;k<num.size();k++)
			{
				for(int m=0;m<prime.size();m++)
				{
					if((num[j]%prime[m] == 0)&&(num[k]%prime[m] == 0))
					{
						for(int l=0;l<set.size();l++)
						{
							if(set[l] == set[k])
								set[l] = set[j];
						}
						break;
					}
				}
			}
		}

		int noSets = 0;
		for(int j=0;j<set.size();j++)
		{
			if(set[j] != -1)
			{
				noSets++;
				for(int k=j+1;k<set.size();k++)
				{
					if(set[k] == set[j])
						set[k] = -1;
				}
				set[j] = -1;
			}
		}

		cout<<"Case #"<<i<<": "<<noSets<<endl;
	}
}

bool ae_is_prime(unsigned int n)
{
	static unsigned int primes55[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
		73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
		181,191,193,197,199,211,223,227,229,233,239,241,251,257};

	for(unsigned int i=0;i<55;i++) 
	{
		if (n%primes55[i] == 0) 
		{
			if (n == primes55[i]) 
			{
				return true;
			}
			else
			{
				return false;
			}
		}
	}

	unsigned int maxtest = n>>4;

	for(unsigned int i=259; i<maxtest; i+=2)
	{
		if (n%i == 0)
		{
			return false;
		}
	}

	return true;
}
