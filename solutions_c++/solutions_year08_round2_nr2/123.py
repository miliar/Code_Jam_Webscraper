#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath> 
#include <queue>
#include <fstream>
#include <map>

using namespace std;

bool isprime(int n)
{
	for(int i=2; i*i<=n; i++)
	{
		if(n%i==0) return false;
	}
	return true;
}

int main()
{
	ifstream in("B-small.in");
	ofstream out("B-small.out");
	int testCases; string temporary; getline(in,temporary); stringstream sinple(temporary); sinple>>testCases;
	for(int tst=0; tst<testCases; tst++)
	{
	
		int A, B, P; in >> A >> B >> P;
		vector <int> label(B-A+1,0);
		vector <int> primes; primes.push_back(2);
		for(int i=3; i<=1000; i++) { if(isprime(i)) primes.push_back(i); }
		for(int i=0; i<label.size(); i++)
		{
			label[i]=i;
		}
		
		for(int i=A; i<=B; i++)
		{
			for(int j=i+1; j<=B; j++)
			{
				for(int k=0; k < primes.size(); k++)
				{	
					if(i%primes[k]==0&&j%primes[k]==0&&primes[k]>=P)
					{
						//cout << "here" << endl;
						int lab = label[j-A]; int toLab = label[i-A];
						for(int l=0; l<label.size(); l++)
						{
							if(label[l]==lab)
							{
								label[l]=toLab;
							}
						}
					}
				}
			}
		}
		//for(int i=0; i<label.size(); i++) { cout << A+i << " " << label[i] << endl; }
		vector <int> endLab;
		for(int i=0; i<label.size(); i++)
		{
			bool found = false;
			for(int j=0; j<endLab.size(); j++)
			{
				if(endLab[j]==label[i]) 
				{ found=true; break; }
			}
			if(!found) endLab.push_back(label[i]);
		}
		
		
	
	out << "Case #" << tst+1 << ": " << endLab.size() << endl;; //complete here
	}
	
	return -1;
}
