#include <iostream>
#include <cstdlib>
const int MAX = 100;

int targeting(char* R, int* P, int max, int index, char which_hallway) {
  for(int i = index + 1; i < max; i++) {
    if ( R[i] == which_hallway ) return P[i];
  }
  return -1;
}

int main(){

  int T, N, P[MAX] = {0,};
  char R[MAX] = {0,};
  std::cin>>T;

  for(int count = 1; count <= T; count++) {
    int time = 0;
    std::cin>>N;
    for(int i = 0; i < N; i++) {
      std::cin>>R[i]>>P[i];
    }

    int O_curr = 1, B_curr = 1;
    for(int i = 0; i < N; i++) {
      if ( R[i] == 'O' ) {
	int B_next = targeting(R, P, N, i, 'B');
	int dist = P[i] - O_curr;
	
	O_curr = P[i];
	time += abs(dist) + 1;

	if ( B_next != -1 ) {
	  if ( abs(B_next - B_curr) <= abs(dist) + 1 ) B_curr = B_next;
	  else if ( B_next > B_curr ) B_curr += abs(dist) + 1;
	  else if ( B_next < B_curr ) B_curr -= (abs(dist) + 1);
	}
	
      }
      else if ( R[i] == 'B') {
	int O_next = targeting(R, P, N, i, 'O');
	int dist = P[i] - B_curr;
	
	B_curr = P[i];
	time += abs(dist) + 1;

	if ( O_next != -1 ) {
	  if ( abs(O_next - O_curr) <= abs(dist) + 1 ) O_curr = O_next;
	  else if ( O_next > O_curr ) O_curr += abs(dist) + 1;
	  else if ( O_next < O_curr ) O_curr -= (abs(dist) + 1);
	}

      }

    }   




    std::cout<<"Case #"<<count<<": "<<time<<std::endl;
  }

  return 0;
}
