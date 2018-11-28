#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>

using namespace std ;

#define NUM_QUERIES	1005
#define	NUM_SEARCH	105
#define	FILE_IN			"A-large.in"
#define	FILE_OUT		"A-large.out"
#define	INF					1000000
#define MIN(a, b)	((a) < (b) ? (a) : (b))

int num_tests, num_engines, num_queries ;
string	engine [NUM_SEARCH] ;
int			query [NUM_QUERIES], d [NUM_SEARCH], tmp [NUM_SEARCH] ;


int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
	int best ;
	string cur_query ;
	
	in >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		in >> num_engines ;
		getline(in, cur_query) ;
		for (int i = 0 ; i < num_engines ; i ++) {
			getline(in, engine [i]) ;
		}
		
		in >> num_queries ;
		getline(in, cur_query) ;
		for (int i = 0 ; i < num_queries ; i ++) {
			getline(in, cur_query) ;
			bool found = false ;
			for (int ie = 0 ; ie < num_engines && !found ; ie ++) {
				if (cur_query == engine [ie]) {
					query [i] = ie ;
					found = true ;
				}
			}
			if (!found) {
				query [i] = -1 ;
			}
		}
		
		for (int i = 0 ; i < num_engines ; i ++) {
			d [i] = -1 ;
		} 
		for (int i = 0 ; i < num_queries ; i ++) {
			int min = -1 ;
			for (int j = 0 ; j < num_engines ; j ++) {
				if (d [j] != -1) {
                   if (min == -1 || d [j] < min) {
				      min = d [j] ;					
				      }
				}				
			}
			for (int j = 0 ; j < num_engines ; j ++) {
				if (j != query [i]) {
					if (d [j] != -1) {
						d [j] = MIN(d [j], min + 1) ;
					}
					else {
						d [j] = min + 1 ;
					}
				}
			}
			if (query [i] != -1) {
				d [query [i]] = -1 ;
			}
			
			/*cout << "min = " << min << endl ;
			for (int j = 0 ; j < num_engines ; j ++) {
                cout << d [j] << " " ;
            }
            cout << endl ;*/
		}
		best = INF ;
		for (int i = 0 ; i < num_engines ; i ++) {
			if (d [i] != -1 && d [i] < best) {
				best = d [i] ;
			}
		}
		if (best == INF) best = 0 ;
		out << "Case #" << test << ": " << best << endl ;
		
		//int n ;
		//cin >> n ;
	}
	out.flush() ;
	out.close() ;
	return 0 ;
}


