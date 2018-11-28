#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>

using namespace std ;

#define NUM_TRAINS	205
#define NUM_TOTAL		2 * NUM_TRAINS
#define	FILE_IN			"B-large.in"
#define	FILE_OUT		"B-large.out"
#define	INF					1000000
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define ch2int(c) ((c) - '0')

int num_tests, num_engines, num_queries ;

struct timetable {
	int begin, end ;	
} ;

ifstream in(FILE_IN) ;
ofstream out(FILE_OUT) ;

int n, na, nb, timewait ;
bool useda [NUM_TOTAL], usedb [NUM_TOTAL] ; // e [NUM_TOTAL] [NUM_TOTAL], vis [NUM_TOTAL] ;
int outd [NUM_TOTAL], ind [NUM_TOTAL] ;
timetable ta [NUM_TRAINS], tb [NUM_TRAINS], tmpt ;

int str2time(string s) {
	int hour = 10 * ch2int(s [0]) + ch2int(s [1]) ;
	int min = 10 * ch2int(s [3]) + ch2int(s [4]) ;
	return 60 * hour + min ;
}

bool can(timetable a, timetable b) {
	return (b.begin >= a.end + timewait) ;
}

bool smaller(timetable a, timetable b) {
	return a.begin < b.begin || (a.begin == b.begin && a.end <= b.end) ;
}

bool better(timetable a, timetable b) {
	return a.end > b.end || (a.end == b.end && a.begin >= b.begin) ;
}


void getinput(int n, timetable *t) {
	string s ;
	for (int i = 0 ; i < n ; i ++) {
		in >> s ;
		t [i].begin = str2time(s) ;
		in >> s ;
		t [i].end = str2time(s) ;
	}
	for (int i = 0 ; i < n ; i ++) {
		for (int j = i + 1 ; j < n ; j ++) {
			if (!smaller(t [i], t [j])) {
				tmpt = t [i] ;
				t [i] = t [j] ;
				t [j] = tmpt ;
			}
		}
	}
}

int main(int argc, char **argv) {
	int best ;
	string s ;
	
	in >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		in >> timewait ;
		
		in >> na >> nb ;
		getinput(na, ta) ;
		getinput(nb, tb) ;
				
		for (int ia = 0 ; ia < na ; ia ++) {
			useda [ia] = false ;
		}
		for (int ib = 0 ; ib < nb ; ib ++) {
			usedb [ib] = false ;
		}
		int ia = na - 1, ib = nb - 1 ;
		int cnta = 0, cntb = 0 ;
		while (ia >= 0 && ib >= 0) {
			if (smaller(ta [ia], tb [ib])) {
				int best = -1 ;
				for (int ca = 0 ; ca < na ; ca ++) {
					if (!useda [ca]) {
						if (can(ta [ca], tb [ib])) {
							if (best == -1 || better(ta [ca], ta [best])) {
								best = ca ;
							}							
						}
					}					
				}
				if (best == -1) {
					cntb ++ ;
				}
				else {
					useda [best] = true ;
				}
				ib -- ;
			}
			else {
				int best = -1 ;
				for (int cb = 0 ; cb < nb ; cb ++) {
					if (!usedb [cb]) {
						if (can(tb [cb], ta [ia])) {
							if (best == -1 || better(tb [cb], tb [best])) {
								best = cb ;
							}							
						}
					}					
				}
				if (best == -1) {
					cnta ++ ;
				}
				else {
					usedb [best] = true ;
				}
				ia -- ;
			}
		}
		cnta += ia + 1 ;
		cntb += ib + 1 ;
		
		out << "Case #" << test << ": " << cnta << " " << cntb << endl ;
	
	}
	out.flush() ;
	out.close() ;
	return 0 ;
}


