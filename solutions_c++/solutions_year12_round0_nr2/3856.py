#include <iostream>
#include <vector>
#include <map>
#include <fstream>
using namespace std;


int check(int a)
{

	

}




int main()
{
	map < char,char> m;

	

	fstream fout("out_a.out",ios::out);
	int t;
	cin >> t;
	int k = 0;
	
	while ( t-- ) {
		k++;	
		int n,s,p,d;
		int count = 0;
		cin >> n >> s >> p;
		int min;
		
		 min = p + p - 1 + p -1;
		vector < int > v;
		for ( int i = 0; i < n; i++) {
			cin >> d;
			v.push_back(d);
		}	
		for ( int i = 0; i < n; i++) {
			if ( v[i] >= min) {
				count++;
			}
			else if ( v[i] >= min-2 && v[i]>=p  && s > 0    ) {
				count++;
				s--;
			}
		}


	fout << "Case #" << k <<": "<< count << "\n";
	}
	
	return 0;
}



