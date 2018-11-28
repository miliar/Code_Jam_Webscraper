#include<iostream>


#include<vector>
#include<algorithm>


using namespace std;

int main(){
	int numcases;
	cin>>numcases;
	for (int c=1; c<=numcases; c++){
		long long total_euros=0;


		long long num_runs, capacity, n;

		cin>>num_runs>>capacity>>n;

		vector<long long> groups(n);
		vector<long long> total(n,0);
		vector<long long> rides(n,0);
		vector<bool> visited(n, false);

		long long people=0;
		for(int i=0; i<n; i++){
		 cin>>groups[i];
		 people+=groups[i];
		}

		if (people<capacity) total_euros=num_runs*people;
		else{

		long long r=0;
		int s=0;
		while(r<num_runs){
			if (visited[s]) break;

			total[s]=total_euros;
			rides[s]=r;

			visited[s]=true;
			r++;
			long long num_passengers=0; int i=0;
			while (num_passengers+groups[(s+i)%n]<=capacity){ 
				num_passengers+=groups[(s+i)%n]; i=(i+1) %n;
			}
			//cout<<r<<' '<<i<<' '<<num_passengers<<endl;
			s=(s+i)%n; total_euros+=num_passengers; 
		}

		long long euros_in_cycle=total_euros-total[s];
		long long rides_in_cycle=r-rides[s];

		if (rides_in_cycle+r<num_runs){
			total_euros+=euros_in_cycle*((num_runs-r)/rides_in_cycle);
			r=num_runs-((num_runs-r)%rides_in_cycle);
		}
		while(r<num_runs){
			//if (visited[s]) break;

			//total[s]=total_euros;
			//rides[s]=r;

			//visited[s]=true;
			r++;
			long long num_passengers=0; int i=0;
			while (num_passengers+groups[(s+i)%n]<=capacity){ 
				num_passengers+=groups[(s+i)%n]; i=(i+1) %n;
			}
			//cout<<r<<' '<<i<<' '<<num_passengers<<endl;
			s=(s+i)%n; total_euros+=num_passengers; 
		}
		
		}
		cout<<"Case #"<<c<<": "<<total_euros<<endl;
		
	}
	return 0;
}