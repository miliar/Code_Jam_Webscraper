#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int nCasos;
	cin>>nCasos;

	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		int N;
		cin>>N;
		
		vector <int> A(N), B(N);
		for(int i=0; i<N; i++)
			cin>>A[i]>>B[i];
		
		int x = 0;
		for(int i=0; i<N; i++)
		{
			for(int j=i+1; j<N; j++)
			{
				if((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j])) x++;
			}
		}
		cout<<x<<endl;
	}
	
	return 0;
}
