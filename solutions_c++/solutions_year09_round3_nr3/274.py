/*
 *  BribeThePrisoners.cpp
 *
 *  Created by Josh Deprez on 13/09/09.
 *
 * Incorporates code using libdispatch, freely available at http://libdispatch.macosforge.org/
 * This code was probably compiled using llvm-g++. The LLVM compiler infrastructure is freely 
 * available at http://llvm.org/
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <Dispatch/Dispatch.h>
typedef long long ll;
using namespace std;

int main()
{
	
	dispatch_queue_t queue = dispatch_get_global_queue(0,0);
	dispatch_group_t group = dispatch_group_create();
	
	int T;
	cin >> T;
	__block int answers[100];
	for (int t=0; t<T; ++t)
	{
		int P,Q;
		cin >> P >> Q;
		__block int q[5];
		for (int i=0;i<Q;++i) cin >> q[i];
		
		sort(q,q+Q);
		
		dispatch_group_async(group, queue, ^{
			answers[t] = INT_MAX;
			do
			{
				int b=0;
				for (int i=0; i<Q; ++i)
				{
					int l=1;
					int u=P;
					for (int j=0; j<i; ++j) 
					{
						l=max(l,q[j] < q[i] ? q[j]+1 : l); 
						u=min(u,q[j] > q[i] ? q[j]-1 : u);
					}
					b+= u-l;
				}
				answers[t] = min(answers[t], b);
			} while (next_permutation(q,q+Q));
		});
	}

	
	dispatch_group_wait(group,DISPATCH_TIME_FOREVER);
	
	for (int t=0; t<T; ++t)
	{
		cout << "Case #" << (t+1) << ": " << answers[t] << endl;
	}
	 
	return 0;
}

