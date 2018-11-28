#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std ;
int Dancing (int &N, int &S, int &P, int *ti)
{
	int cnt =0 ;
	for (int i =0, temp[3] ; i < N ; i++) {
		switch (ti[i] %3) {
		case 0 :
			for (int j =0 ; j < 3 ; j++) 
				temp[j] =(ti[i] / 3) +(j -1) ;
			if ((temp[2] -1) >= P) cnt++ ;
			else if (S && temp[2] >= P && temp[1]) {
				cnt++ ;
				S-- ;
			}
			break ;
		case 1 :
			for (int j =0 ; j < 3 ; j++)
				if (j) temp[j] =(ti[i] /3) +1 ;
				else temp[j] =(ti[i] /3) -1 ;
				if (temp[2] >= P || (temp[2] -1) >= P) cnt++ ;
				else if (S && temp[2] >= P) {
					cnt++ ;
					S-- ;
				}
				break ;
		default :
			for (int j =0 ; j < 3 ; j++)
				if (j) temp[j] =(ti[i] /3) +1 ;
				else temp [j] =(ti[i] /3) ;
			if (temp[2] >= P || temp[0] >= P) cnt++ ;
			else if (S && (temp[2] +1) >= P) {
				cnt++ ;
				S-- ;
			}
		}
	}
	return cnt ;
}
int main ()
{
	ifstream inSt ("B-small-attempt10.in") ;
	try {
		if (inSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Input file opeing failed." << endl ;
		exit (1) ;
	}
	ofstream outSt ("output.txt") ;
	try {
		if (outSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Output file opeing failed." << endl ;
		exit (1) ;
	}

	int numT ;
	inSt >> numT ;
	inSt.ignore (1, '\n') ;
	
	for (int i =1, N, S, P ; i <= numT ; i++) {
		inSt >> N ;
		int *ti =new int[N] ;
		inSt >> S >> P ;
		for (int j =0 ; j < N ; j++)
			inSt >>ti[j] ;
		outSt << "Case #" << i << ": " << Dancing (N, S, P, ti) << endl ;
	}
}
/*void Max (int *) ;

int Dancing (int N, int S, int P, int *ti)
{
	int *temp =new int[3], cnt =0 ;

	for (int i =0 ; i < N ; i++) {

		temp[0] =temp[1] =temp[2] =0 ;
		if (ti[i] < P) continue ;
		if ((ti[i] -(P*2)) > 0) temp[0] =ti[i] -(P*2) ;
		if ((ti[i] -(P +temp[0])) > 0) temp[1] =ti[i] -(P +temp[0]) ;
		if ((ti[i] -(temp[0] +temp[1])) > 0) temp[2] =ti[i] -(temp[0] +temp[1]) ;

		Max (temp) ;

		while ((temp[0] -temp[1]) > 1) {
			temp[0]-- ; temp[1]++ ;
		}
		while ((temp[0] -temp[2]) > 1) {
			temp[0]-- ; temp[2]++ ;
		}
		while ((temp[1] -temp[2]) > 1) {
			temp[1]-- ; temp[2]++ ;
		}
		if (temp[1] > temp[0])
		while ((temp[1] -temp[0]) > 1) {
			temp[1]-- ; temp[0]++ ;
		}
		if (temp[2] > temp[0])
		while ((temp[2] -temp[0]) > 1) {
			temp[2]-- ; temp[0]++ ;
		}
		Max (temp) ;
		if (temp[0] < P && temp[1] < P && temp[2] < P && S) {
			temp[0] =temp[1] =temp[2] =0 ;
			if ((ti[i] -(P*2)) > 0) {
				temp[0] =ti[i] -(P*2) ;
			}
			if ((ti[i] -(P +temp[0])) > 0) {
				temp[1] =ti[i] -(P +temp[0]) ;
			}
			if ((ti[i] -(temp[0] +temp[1])) > 0) {
				temp[2] =ti[i] -(temp[0] +temp[1]) ;
			}
			Max (temp) ;
			S-- ;
		}
		if (temp[0] >= P) cnt++ ;
	}
	return cnt ;
}
void Max (int *temp)
{
	int t ;

	if (temp[0] < temp[1]) {
		t =temp[0] ;
		temp[0] =temp[1] ;
		temp[1] =t ;
	}
	if (temp[0] < temp[2]) {
		t =temp[0] ;
		temp[0] =temp[2] ;
		temp[2] =t ;
	}
	if (temp[1] < temp[2]) {
		t =temp[1] ;
		temp[1] =temp[2] ;
		temp[2] =t ;
	}
	if (temp[0] < temp[1]) {
		t =temp[0] ;
		temp[0] =temp[1] ;
		temp[1] =t ;
	}
}
int main ()
{
	ifstream inSt ("B-small-attempt7.in") ;
	try {
		if (inSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Input file opeing failed." << endl ;
		exit (1) ;
	}
	ofstream outSt ("output.txt") ;
	try {
		if (outSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Output file opeing failed." << endl ;
		exit (1) ;
	}

	int numT ;
	inSt >> numT ;
	inSt.ignore (1, '\n') ;
	
	for (int i =1, N, S, P ; i <= numT ; i++) {
		inSt >> N ;
		int *ti =new int[N] ;
		inSt >> S >> P ;
		for (int j =0 ; j < N ; j++)
			inSt >>ti[j] ;
		outSt << "Case #" << i << ": " << Dancing (N, S, P, ti) << endl ;
	}
	inSt.close () ;
	outSt.close () ;
	return 0 ;
}*/