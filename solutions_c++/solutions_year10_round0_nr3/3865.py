#include <iostream>
#include <vector>

using namespace std;

int T,R,K,N;
int money;
vector<int> line;
vector<int> ride;

int main(){
	freopen ("out","w",stdout);
	freopen ("in","r",stdin);

	cin>>T;

	//for each test case...
	for (int t=0;t<T;t++){
		
		//initial input/inits
		cin>>R>>K>>N;
		money=0;

		//set up the initial line of groups
		line.clear();
		for (int n=0;n<N;n++){
			int g;
			cin>>g;
			line.push_back(g);
		}

		//for each run of the rollercoaster...
		for (int r=0;r<R;r++){
			//at first, no people are on:
			int curSize=0;

			//until the ride is full...
			while (1)
				//add groups to the ride:
				if (line.size()>0 && curSize+line[0]<=K){
					curSize+=line[0];
					ride.push_back(line[0]);
					line.erase(line.begin());
				}else
					break;

			//run the ride, and make some money!
			money+=curSize;

			//make the riders get off the ride, and push them to the back of the line:
			while (ride.size()!=0){
				line.push_back(ride[0]);
				ride.erase(ride.begin());
			}
		}

		//output the money made:
		cout<<"Case #"<<t+1<<": "<<money<<"\n";
	}

	return 0;
}