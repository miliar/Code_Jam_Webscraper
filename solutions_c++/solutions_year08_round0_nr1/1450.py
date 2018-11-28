#include<iostream>
#include<map>
#include<vector>
#include<string>

using namespace std;

main(){
  int z, n, m;
  string S;
  scanf("%d", &z);

  int A[1000];

  for(int j=0; j<z; j++){

    scanf("%d\n", &n);

    map <string, int> M;
    M.clear();

    vector <int> V;

    for(int i=0; i<n; i++){
      getline(cin, S);
      M[S]=i+1;
      A[i+1] = 0;
    }

    scanf("%d\n", &m);
    for(int i=0; i<m; i++){
      getline(cin, S);
      V.push_back(M[S]);
    }

    int nr = 1;
    int akt = 0;
    int res = 0;
   
    for(int i=0; i<m; i++){
       
	if(A[V[i]] != nr){
		if(akt == n-1){
			nr++;
			akt = 0;
			res++;
		}

	  	A[V[i]] = nr;
          	akt++;
       	}
     }
     printf("Case #%d: %d\n", j+1, res); 
    
  }

}

