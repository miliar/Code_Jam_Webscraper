#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

int main (){
	ofstream out;
	out.open("out");	

	int n;
	cin >> n;
	string c;
	getline(cin,c);
	
	for(int ii=0; ii<n; ++ii){
		int N, S, p, t, a=0, b=0;
    cin >> N >> S >> p;
		for(int jj=0; jj<N; ++jj){
      cin >> t;
      if(p>t) continue;
      if((t-1)/3+1 >= p) a++;
      else if((t-2)/3+2 >= p) b++;
		}

		out << "Case #" << ii+1 << ": " << a+min(S,b) << endl;
	} 
	
	out.close();
	return 0;
}

 
