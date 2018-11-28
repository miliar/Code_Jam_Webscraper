/*
	A. Minimum Scalar Product
	Google Code Jam '08 - Round 1A
	- n@p [ 26 Jul 2008 ]
 */

#include<iostream.h>
#include<vector>
#include<algorithm>

using namespace std;

void main()
{
	int cases, n, N, i, x;
	long int prod;
	cin>>cases;
	for(n=1;n<=cases;n++)
	{
		vector<int> V1, V2;

		cin>>N;

		//input V1...
		for(i=0;i<N;i++)
		{
			cin>>x;
			V1.push_back(x);
		}
		//copy(istream_iterator<int>(cin), istream_iterator<int>(), back_inserter(V));
		//copy(V.begin(), V.end(), ostream_iterator<int>(cout, " ")); //output

		//input V2...
		for(i=0;i<N;i++)
		{
			cin>>x;
			V2.push_back(x);
		}

		//sort 'em...
		sort(V1.begin(), V1.end());
		sort(V2.begin(), V2.end());
		reverse(V2.begin(), V2.end());
		
		//debug output...
		//for(i=0;i<N;i++)	cout<<V1[i]<<" ";		cout<<endl;
		//for(i=0;i<N;i++)	cout<<V2[i]<<" ";		cout<<endl;

		//scalar product...
		prod=0;
		for(i=0;i<N;i++)
			prod+=V1[i]*V2[i];

		//output...
		cout<<"Case #"<<n<<": "<<prod<<endl;
	}
}