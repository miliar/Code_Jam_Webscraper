#include <iostream>
#include <vector>

using namespace std;

int main()
{
	long long t;
	long long R,K,N,x;

	vector <long long > v;
	vector <long long> Move;
	vector <long long> Tot;

	long long j, tot;
	cin >> t;

	for(int k=1; k<=t; k++) {
		cin >> R >> K >> N ;

		for(int i=0;i<N;i++){
			cin >> x;
			v.push_back(x);
		}
		j=0;

		for(int i=0;i<N;i++){
			x = 0;
			j = 0;
			while(v[(i+j)%N]+x <=  K && j<N){
				x = v[(i+j)%N] + x;
				j++;	
			}
			Tot.push_back(x);
			Move.push_back(j);
		}
		tot = 0;
		int index = 0;
		
		for(int i=0;i<R; i++){
			tot = tot + Tot[index] ;
			index = (index + Move[index])%N;
		}

		cout <<"Case #" << k <<":" << " "<< tot << endl;
		Move.clear();
		v.clear();
		Tot.clear();
	}


	
	return 0;

}
