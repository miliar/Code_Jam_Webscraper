
#include <iostream>
	using namespace std;

#include <vector>
	using std::vector;

#include <algorithm>
	using std::find;

#include <tuple>
	using std::tuple;
	using std::tr1::make_tuple;

			typedef  tuple<int,int> 	sink_t;

		const int max_T = 100;	// 
		const int max_W = 100;	//
		const int max_H = 100;	//
		const char alphabet[27] =	"abcdefghijklm" "nopqrstuvwxyz";

		int	A[max_H+1][max_W+1] = {{-1}};		// altitudes
		char	B[max_H+1][max_W+1] = {{'-'}};		// basins
		int	H,W;

sink_t   get_sink(int h, int w)  {

	int prev_a = 20000;
	int l_h = h;
	int l_w = w;

	while ( prev_a > A[h][w]) {

		prev_a = A[h][w];	// lowest so far

		// one step
		if ( 1<h  &&  A[l_h][l_w] > A[h-1][w])		{ l_h = h-1;  l_w = w  ; }
		if ( 1<w  &&  A[l_h][l_w] > A[h][w-1])		{ l_h = h  ;  l_w = w-1; }
		if ( w<W  &&  A[l_h][l_w] > A[h][w+1])		{ l_h = h  ;  l_w = w+1; }
		if ( h<H  &&  A[l_h][l_w] > A[h+1][w])		{ l_h = h+1;  l_w = w  ; }
		h = l_h; w = l_w; // new center
	}

	return  make_tuple(l_h, l_w);
}

int main() {

/////////////////////////////////////////////////////////////////////////////////////

		int	T;

		char	s[1000];
		#define NEXT_LINE  	cin.getline(s,1000);
	cin  >> T; 			NEXT_LINE
	
	
	// read maps
	for (int t=1;  t<=T && cin;  t++)  {

		cout << "Case #" << t << ":" << endl;

		cin  >> H >> W;		NEXT_LINE
									cerr << "*** t,H,W:  " << std::tr1::make_tuple(t, H, W) << endl;	

		// read map
		for (int h=1;  h<=H;  h++) {
			for (int w=1;  w<=W;  w++) {
				cin >> A[h][w];				
									cerr << A[h][w] << " ";
			}
			NEXT_LINE
									cerr << endl;
		}

									cerr << "----\n";
		// assing basins
		std::vector<sink_t>   S;
		for (int h=1;  h<=H;  h++) {
			for (int w=1;  w<=W;  w++) {
				sink_t   s = get_sink(h,w);
				auto  mapped_sp =  find (S.begin(), S.end(), s); 				
				if ( mapped_sp == S.end()) {
					S.push_back(s);
					mapped_sp = S.end()-1;
				}
				char c = 'a' + (mapped_sp - S.begin());
				B[h][w] = c;
				cout << B[h][w] << " ";
			}
			cout << endl;
		}

	}
	


}
