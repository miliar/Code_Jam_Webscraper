#include <fstream>
using namespace std;

int main(){
	ifstream file;
	ofstream output;

	file.open("C-large.in");
	output.open("C-large.out");

	int i, cases, next, ride, R, k,N, ammount;
	int* people;
	int  next_group, first_aboard;
	bool full_queue;

	file >> cases;
	for(i=1;i<=cases;i++){
		file >> R;
		file >> k;
		file >> N;

		ammount = 0;
		people = new int[N];
		for(next=0;next<N;next++){
			file >> people[next];
		}

		next=0;
		for(ride=0;ride<R;ride++){
			next_group=0;
			first_aboard=next;
			full_queue=false;
			while(next_group + people[next] <= k && !full_queue ){ //there's still room on the ride
				next_group += people[next];
				next++;
				if (next == N){
					next = 0;
					full_queue = first_aboard==next; //border case: full queue enters in the ride
				 }
			}
			ammount += next_group;
		}
		output << "Case #" << i << ": " << ammount << endl;
		delete people;
	}
	file.close();
	output.close();

	return 0;
}

