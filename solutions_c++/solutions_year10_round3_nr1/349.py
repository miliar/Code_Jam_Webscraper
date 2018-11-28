#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

class wire{
	public:
		int a;
		int b;
};

bool operator<(wire A, wire B){
	return (A.a<B.a);
} 



int main(){

	int numCases;
	cin>>numCases;
	for (int c=1; c<= numCases; c++){
		long long answer=0;
		int numwires;
		cin>>numwires;
		vector<wire> wires(numwires);		
		for (int i=0; i<numwires; i++)
			cin>>wires[i].a>>wires[i].b;
		sort(wires.begin(), wires.end());

			
		for (int i=0; i<numwires; i++){
			for (int j=i+1; j<numwires; j++)
				if (wires[j].b<wires[i].b) answer++;
		}

		
		cout<<"Case #"<<c<<": "<<answer<<endl;
	}
	return 0;
}