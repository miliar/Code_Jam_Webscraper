#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;

int main(){

	int N;
	cin>>N;


	for ( int n=1; n<=N; n++){

		int T;
		cin>>T;

		vector<unsigned long> candies;
		unsigned long mask = 0;

		unsigned long current;

		for ( int i=0; i<T; i++) {
			cin>>current;
			candies.push_back( current );
			mask ^= current;
		}

		if ( mask != 0){
			cout<<"Case #"<<n<<": NO"<<endl;
			continue;
		}

		sort ( candies.begin(), candies.end() );

		/*unsigned long firskMask = candies[0];
		unsigned long lastMask = mask ^ candies[0];

		int i = 1;
		while ( firskMask != lastMask && i<candies.size() ){
			firskMask ^= candies[i];
			lastMask  ^= candies[i];
			i++;
		}*/

		unsigned long total = 0;
		for ( int i=1; i<candies.size() ; i++){
			total += candies[i];
		}

		cout<<"Case #"<<n<<": "<<total<<endl;

	}

	return 0;
}
