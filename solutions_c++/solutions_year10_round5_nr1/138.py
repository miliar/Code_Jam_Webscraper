#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <climits>

using namespace std;

double PI = 3.14159265358979323846264338328;
double EPS = 1e-10;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define MSG(a) cout << #a << " = " << a << endl;
#define ITOA(a) char c[500];  sprintf(c,"%d",a);  string s(c);
#define SORT(a) sort(a.begin(),a.end())
#define REV(a) reverse(a.begin(),a.end())

long long inv(long long x, long long p)
{
	long long ans = 1;
	long long n = p-2;
	while(n > 0)
	{
		if(n%2 == 1) ans *= x, ans %= p;
		x *= x, x %= p;
		n /= 2;
	}
	return ans%p;
}

bool primes[1000000];

int main(int argc, char** argv)
{	
	FOR(p,0,1000000)
		primes[p] = 1;
	primes[0] = primes[1] = 0;
	FOR(p,2,1000000)
	if(primes[p] == 1)
	{
		int tmp = p+p;
		while(tmp < 1000000)
			primes[tmp] = 0, tmp += p;
	}
	
	
	string name(argv[1]);
	ifstream fin((name+".in").c_str());
	ofstream fout((name+".out").c_str());
	
	int T;
	fin >> T;

	for(int tt = 0; tt < T; tt++)
	{
		fout << "Case #" << tt+1 << ": ";
		
		int D,K;
		fin >> D >> K;
		long long nums[15];
		FOR(i,0,K)
			fin >> nums[i];
		FOR(i,0,K)
			cout << nums[i] << " ";
		cout << endl;
	
		
		long long lower = 2;
		FOR(i,0,K)
			lower = max(lower, nums[i]);
		
		
		if(K == 1)
		{
			fout << "I don't know." << endl;
			continue;
		}
	
		if(nums[0] == nums[1])
		{
			fout << nums[0] << endl;
			continue;
		}
		
		if(K == 2)
		{
			fout << "I don't know." << endl;
			continue;
		}
	
		if(K >= 3)
		{
			long long upper = 1;
			FOR(x,0,D)
				upper *= 10;
			
			set<int> ans;
			int cnter = 0;	
			
			if(nums[0] == nums[1])
			{
				if(nums[2] != nums[1]) fout << "ERROR\n";
				fout << nums[0] << endl;
				continue;
			}
			
			
			FOR(P,lower+1,upper)
			if(primes[P])
			{	
				long long A = (nums[2]-nums[1])*inv(nums[1]-nums[0],P);
				
				A %= P, A += P, A %= P;
				long long B = nums[1] - nums[0]*A;
				
				B %= P, B += P, B %= P;
				
				int bad = 0;
				FOR(t,0,K-1)
					if((A*nums[t]+B)%P != nums[t+1])
					{
						bad = 1;
					}
				if(bad == 0)
				{
					ans.insert((A*nums[K-1]+B)%P);
					cout << P << " " << A << " " << B << " " << (A*nums[K-1]+B)%P << endl;
				}
				if(ans.size() > 1) break;
			}
			if(ans.size() > 1)
			{
				fout << "I don't know.\n";
				vector<int> V(ans.begin(),ans.end());
			}
			else if(ans.size() == 1)
				fout << *ans.begin() << endl;
			else fout << "ERROR\n";
			
			continue;
		}
		
	}
	
	return 0;
}