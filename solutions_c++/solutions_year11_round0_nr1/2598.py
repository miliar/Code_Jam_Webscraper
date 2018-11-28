
#include <vector>
#include <iostream>
#include <string> 

using namespace std;

int main()
{
	int T;
	cin>>T;

	for (int t = 0; t < T; ++t) {
		int N;
		cin>>N;

		int posorange = 1;
		int posblue = 1;
		int timeorange = 0;
		int timeblue = 0;

		for (int i = 0; i < N; ++i) {
			char R;
			int P;
			cin>>R>>P;
			if (R == 'O') {
				timeorange = max(timeblue, abs(P-posorange)+timeorange)+1;
				posorange = P;
			}
			else
			{
				timeblue = max(timeorange, abs(P-posblue)+timeblue)+1;
				posblue = P;
			}
		}
		cout<<"Case #"<<t+1<<": "<<max(timeorange, timeblue)<<std::endl;
	}




	char t;
	cin>>t;
}
