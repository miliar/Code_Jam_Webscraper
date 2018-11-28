/*
 *  1.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 08/07/25.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

class joint_set
{
	public:
		joint_set(long long size)
		:id(size), rank(size)
		{
			for(long long i=0; i<size; ++i) id[i] = i;
		}
		
		void unify(long long a, long long b);
		long long find(long long index);
		bool same(long long a, long long b);

		vector<long long> id, rank;

};

void joint_set::unify(long long a, long long b)
{
	long long a_root = find(a);
	long long b_root = find(b);
	
	if(rank[a_root] < rank[b_root])
		id[a_root] = b_root;
	else if(rank[a_root] > rank[b_root])
		id[b_root] = a_root;
	else
	{
		++rank[a_root];
		id[b_root] = a_root;
	}
}

long long joint_set::find(long long index)
{
	long long parent = id[index];
	
	if(parent == index)
		return parent;
	else
	{
		long long root = find(parent);
		return root;
	}
}

bool joint_set::same(long long a, long long b)
{
	return (find(a)==find(b));
}



int main()
{
	//code from http://www2.roguewave.com/support/docs/sourcepro/edition9/html/stdlibug/5-4.html
	
	const long long sievesize = 1000000;
  vector<bool>
    sieve (sievesize, true);

  // At positions that are multiples of i, set value to zero.
  for (long long i = 2; i * i < sievesize; i++)
    if (sieve[i])
      for (long long j = i + i; j < sievesize; j += i)
        sieve[j] = false;

  // Now output all the values that are still set.
/*  for (long long j = 2; j < sievesize; j++)
    if (sieve[j]) 
      std::cout << j << " ";
*/

	long long N_of_cases=0;
	cin >> N_of_cases;
	
	for(long long LOOP=0; LOOP<N_of_cases; ++LOOP)
	{
		long long A, B, P;
		cin >> A >> B >> P;
		
		long long size = B-A+1;
		
		joint_set sets(B-A+1);
		
		long long diff = B-A;
		
		for(long long i=P; i<=diff; ++i)
		{
			if(sieve[i])
			{
				//cout<<i<<": "<<endl;
			
				long long prev = (A/i)*i;
				if(prev < A) prev += i;
				
				long long target = prev + i;
				
				while(target <= B)
				{
					//cout<<prev<<' '<<target<<endl;
				
					sets.unify(prev-A, target-A);
					prev += i;
					target+= i;
				}
			}
		}
		
		long long ans = 0;
		
		vector<bool> exist(size, false);
		
		for(long long i=0; i<size; ++i)
		{
			long long id = sets.find(i);//cout<<sets.id[i]<<endl;
			
			if(!exist[id])
			{
				++ans;
				exist[id]=true;
			}
		}
		
		cout<<"Case #"<<LOOP+1<<": "<<ans<<endl;	
	}
}

