//============================================================================
// Name        : c.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int A,B;
		cin>>A>>B;
		int N=0, a=A, count=0;
		while(a>=10) {N++; a/=10;}

		int p=pow(10.0,N);

		for (int k=A;k<B;k++)
		{ int t=k;

		int n=N;
		vector<int> numb;
		while(n){
			t= ((t%p)*10+t/p);

			n--;
			if(t>k && t<=B) { numb.push_back(t);
				 count++;}
		}
		sort(numb.begin(), numb.end());
		int ss=numb.size();
		numb.erase(std::unique(numb.begin(), numb.end()), numb.end());
		int diff=ss-numb.size();
		count-=diff;
		}
	cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
