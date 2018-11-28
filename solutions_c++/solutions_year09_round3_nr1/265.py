/*
 *  AllYourBase.cpp
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
#include <Dispatch/Dispatch.h>
typedef long long ll;
using namespace std;

int main()
{
	
	dispatch_queue_t queue = dispatch_get_global_queue(0,0);
	dispatch_group_t group = dispatch_group_create();

	int N;
	cin >> N;
	__block ll answers[100];
	for (int i=0; i<N; ++i)
	{
		string k;
		cin >> k;
		dispatch_group_async(group, queue, ^{
			answers[i]=0;
			map<char,int> val;
			for(int j=0; j<k.length(); ++j) val[k[j]] = -1;
			int base = max(int(val.size()),2), zig=1;
			for(int j=0; j<k.length(); ++j) 
			{
				int &t=val[k[j]];
				if (t==-1) {
					t=zig;
					if (zig==1) zig=0;
					else if (zig==0) zig=2;
					else zig++;
				}
				answers[i]*=base;
				answers[i]+=t;
			}
			
		});

	}
	
	dispatch_group_wait(group,DISPATCH_TIME_FOREVER);
	
	for (int i=0; i<N; ++i)
	{
		cout << "Case #" << (i+1) << ": " << answers[i] << endl;
	}
	
	return 0;
}

