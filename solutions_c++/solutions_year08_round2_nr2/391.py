#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class NumberSets
{
private:
	void modES(vector<long long> divBy[1001], long long B, long long P)
	{
		bool isPrime[10001];
		memset(isPrime, 1, sizeof(isPrime));

		int count = 0;

		isPrime[0] = isPrime[1] = false;
		for(long long i=2;i<=B;i++)
		{
			if(isPrime[i])
			{
				count++;

				divBy[i].push_back(i);
				//cout<<i<<" divisible by "<<i<<endl;

				for(long long j=i+i;j<=B;j+=i)
				{
					isPrime[j] = false;
					if(i>=P)
					{
						divBy[j].push_back(i);
						//cout<<j<<" divisible by "<<i<<endl;
					}
				}
			}
		}

		//cout<<count<<" primes found."<<endl;
	}
	
	bool contains(vector<long long> &v1, vector<long long> &v2)
	{
		for(int i=0;i<v1.size();i++)
		{
			for(int j=0;j<v2.size();j++)
			{
				if(v1[i] == v2[j])
				{
					return true;
				}
			}
		}
		return false;
	}

	void doUnion(vector<long long> &v1, vector<long long> &v2)
	{
		//cout<<"doing union of ";
		//for(int i=0;i<v1.size();i++)
		//	cout<<v1[i]<<",";
		//cout<<" with ";
		//for(int i=0;i<v2.size();i++)
		//	cout<<v2[i]<<",";
		//cout<<endl;

		for(int j=0;j<v2.size();j++)
		{
			int i;
			for(i=0;i<v1.size();i++)
			{
				if(v2[j] == v1[i])
					break;
			}

			if(i==v1.size())
			{
				v1.push_back(v2[j]);
			}
		}
	}

public:
	long long TotalSets(long long A, long long B, long long P)
	{
		long long count = 0;

		vector<long long> divBy[1001];

		modES(divBy, B, P);

		bool used[1001];
		memset(used, 0, sizeof(used));

		vector< vector<long long> > sets;

		for(long long i=A;i<=B;i++)
		{
			bool found = false;
			for(long long j=0;j<count;j++)
			{
				if(contains(sets[j], divBy[i]))
				{
					//cout<<i<<" matched"<<endl;
					doUnion(sets[j], divBy[i]);
					found = true;
					break;
				}
			}

			if(!found)
			{
				sets.push_back(vector<long long>());

				doUnion(sets[count], divBy[i]);
				count++;
			}
			else
			{
				for(long long j=0;j<count;j++)
				{
					for(long long k=j+1;k<count;k++)
					{
						if(contains(sets[j], sets[k]))
						{
							//cout<<"merging sets "<<j<<" and "<<k<<endl;
							doUnion(sets[j], sets[k]);

							sets.erase(sets.begin() + k);

							count--;
						}
					}
				}
			}
		}

		return count;
	}
};

int main()
{
	int C;
	cin>>C;

	for(int i=0;i<C;i++)
	{
		int A, B, P;

		cin>>A>>B>>P;

		NumberSets ns;
		cout<<"Case #"<<i+1<<": "<<ns.TotalSets(A, B, P)<<endl;
	}

	return 0;
}