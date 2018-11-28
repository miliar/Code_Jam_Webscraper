

#include <iostream>
using namespace std;

const int
	MAXN = 1005;

typedef long long int64;

struct group{
	int64 ind , size;
};

int64 T , R , K , N;
group ord[MAXN];
int pos[MAXN] , people[MAXN];

int main(){

	cin >> T;

	for ( int tc = 1 ; tc <= T ; tc++ ){
	
		cin >> R >> K >> N;
		
		for ( int i = 0 ; i < N ; i++ ) cin >> people[i];
		
		for ( int i = 0 ; i < N ; i++ ) pos[i] = -1;
				
		int i , j , cant = 0 , rep;
		for ( i = 0 ; pos[i] == -1 ; i = j ){
		
			int64 num = people[i];
		
			for ( j = (i+1)%N ; j != i && num + people[j] <= K ; j = (j+1)%N  )
				num += people[j];
				
			
			ord[cant] = (group) { i , num };
			pos[i] = cant++;
		
		}
		
		rep = i;
		/*
		for ( i = 0 ; i < cant ; i++ )
			cout << ord[i].ind << " " << ord[i].size << "\n";
			
		cout << "repeats in " << rep << "\n";
		*/
		
		int64 sol = 0;
		
		if ( R > pos[rep] ){
			for ( i = 0 ; i < pos[rep] ; i++ ){
				sol += ord[i].size;	
				R--;
			}	
			
			int64 cycle_length = cant - pos[rep];
			
			int64 total_cycle = 0;
			
			for ( i = pos[rep] ; i < cant ; i++ )
				total_cycle += ord[i].size;
				
			int64 div , mod;
			
			div = R / cycle_length;
			mod = R % cycle_length;
			
			sol += div * total_cycle;
			
			for ( i = pos[rep] ; mod > 0 ; mod-- , i++ )
				sol += ord[i].size;
			
			
		}
		else{
			for ( i = 0 ; i < R ; i++ )
				sol += ord[i].size;
		}
		
		cout << "Case #" << tc << ": " << sol << "\n";
		
	}

	return 0;
}
