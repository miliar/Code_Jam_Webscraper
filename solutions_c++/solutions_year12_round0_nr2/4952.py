#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;

int main(void){

	freopen("traini.txt","r", stdin);
	freopen("caca.txt","w", stdout);
	
	int m, n, s, p;

	cin >> m >> ws;

  int hm;
  int sum;

	for(int i = 0; i < m; i++){


    hm = 0;
    cin >> n >> ws >> s >> ws >> p >> ws;
	
    for(int j = 0; j < n; j++){
      cin >> sum >> ws;
  
      //cout << sum << " " << p << " " << s << endl;      

      if(sum >= p-1 + p-1 + p ||( p == 0 && sum >= 0) || (p == 1 && sum >= 1)){
        hm++;
      } else if(((sum  == p-2 + p-2 + p) || (sum  == p-2 + p-1 + p)) && s > 0 && sum != 0 && sum != 1){
        hm++;
        s--;
      }
    }
  	
    cout << "Case #"<< (i + 1) << ": " << hm << endl;
	}

//	freopen("output.txt","r", stdin);
//	for(int i = 0; i < m; i++){
//		getline(cin, output[i]);
//	}


	return 0;
}
