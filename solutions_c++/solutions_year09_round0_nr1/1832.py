#include <cstring>
	using std::strchr;
#include <cctype>
	using std::islower;
#include <iostream>
	using namespace std;
#include <tuple>
	using std::tr1::tuple;
	using std::tr1::make_tuple;


int main() {

		const int max_L = 15;	// word lenght
		const int max_D = 5000;	// dic size
		const int max_P = 500;	// patterNs
		const int max_A = 37;	// max letters in alphabet
		char  DD[max_D][max_L+10];
		int L, D, P;
		char  PP[max_P][max_L][max_A];

	cin  >> L >> D >> P;
	cerr << "*** L,D,P (P==N):  " << make_tuple(L, D, P) << endl;

	cin.getline(DD[0], max_L+10); // ignore NL on 1st line
	
	
	// read words
	for (int line=0;  line<D;  line++)  {
		cin.getline(DD[line], max_L+10);
		cerr << "*** dic-word-" << line<<":  \t" <<  DD[line] << endl;
	}
	

	// read patterns
	cerr << endl << endl;
	for (int p=0;  p<P;  p++)  {
		char s[1000];
		char* sp = s;
		cin.getline(s, 1000);
		cerr << "*** pat-" << p <<":  \t" <<  s << endl;

		
		for (int g=0;  g<L;  g++)  {
			int dst_i = 0;

			if		((*sp)=='(')		while ( (*++sp) != ')' )	PP[p][g][dst_i++]  =  *sp;
			else if		(islower(*sp))						PP[p][g][dst_i++]  =  *sp;
			else		goto next_line;						// must be EOL or EOS
			
			PP[p][g][dst_i]  = '\0';
			sp++;

			cerr << "\t  group-" << g << ":  \t" <<  PP[p][g] << endl;
		}

		next_line:;
	}

	int count[max_P] = {0};
									//cerr << boolalpha;
	char* pp;

	// for pattern
	for (int p=0;  p<P;  p++)  {					//cerr << "p:" << p<< endl;
		// dic-word
		for (int d=0;  d<D;  d++)  {				//cerr << "\t d:" << d<< "-" << DD[d] << endl;
			// for word-letter
			for ( int li = 0;  li<L;  li++) {		
				int c = DD[d][li];			//cerr << "\t\t li:" << li<< "-" << char(c) << endl;
				int g = li; 
				//for (int g=0;  g<L;  g++)  {		// group
				pp=strchr(PP[p][g], c);			//cerr << "\t\t\t g:" << g<< "(" << PP[p][g] << ")-" << bool(pp) << " " << (void*)pp << endl;
				if (pp) {
					goto next_letter; 
				}
				//}
				goto next_word; // failed: all groups tried
				next_letter:;
			}
			// all letters were matched
			count[p] +=1; 					//cerr << "count[" << p<< "]= " << count[p] << endl;
			next_word:;
		}
	}

	// Result
	for (int p;  p<P;  p++)  {	
		cout << "Case #" << p+1 << ": " << count[p] << endl;	
	}

}
