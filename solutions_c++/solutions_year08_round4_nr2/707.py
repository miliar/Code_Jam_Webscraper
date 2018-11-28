#include <windows.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
using namespace std;

//#define PRINT_DEBUG

struct VoidStream {};
template<typename T>
inline VoidStream & operator<<(VoidStream &v, T t) {
	return v;
}

#ifdef PRINT_DEBUG
	#define OUT_DEBUG std::cout
#else
	VoidStream _vs_;
	#define OUT_DEBUG _vs_
#endif


/*
int calc(unsigned int N, unsigned int M, unsigned int A) {
	if (((N+1) * (M+1)) < A)
		return (-1);
}
*/

unsigned int getDoubleArea(int xA,int yA,int xB,int yB,int xC,int yC) {
	//Area = abs(xB*yA-xA*yB)+(xC*yB-xB*yC)+(xA*yC-xC*yA)
	int area = (xB*yA-xA*yB)+(xC*yB-xB*yC)+(xA*yC-xC*yA);
	if (area<0) area = (0 - area);
//	OUT_DEBUG << "area of " << xA<<' '<<yA<<' '<<xB<<' '<<yB<<' '<<xC<<' '<<yC<<'='<<area<<endl;
	return area;
}


void doCase(ifstream &in, int cnum) {
	 int N, M, A;
	in >> N >> M >> A;

	
//OUT_DEBUG << N<<' '<<M<<' '<<A<<endl;

	if ((N*M) < A) {
		cout << "Case #" << cnum << ": IMPOSSIBLE\n";
		return;
	}

	int x0 = 0;
	int y0 = 0;
	for (int x1 = 0; x1 <= N; x1++)
		for (int x2 = 0; x2 <= N; x2++)
			for (int y1 = 0; y1 <= M; y1++)
				for (int y2 = 0; y2 <= M; y2++) {
					if ((x1!=0 || y1 !=0) && (x2!=0 || y2!=0)) {
						if (x1!=x2 || y1!=y2) {
							if (getDoubleArea(x0,y0,x1,y1,x2,y2)==A) {
								cout << "Case #" << cnum << ": " << x0<<' '<<y0<<' '<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<' '<<endl;
								return;
							}
						}
					}
				}

	cout << "Case #" << cnum << ": IMPOSSIBLE\n";

/*
	int res = calc(N, M, A);
	cout << "Case #" << cnum << ": ";
	if (res < 0)
		cout << "IMPOSSIBLE";
	else
		cout << res;
	cout << endl;
	*/
}



int main(int agrc, char *argv[]) {
	OUT_DEBUG << "reading from file \"" << argv[1] << "\"\n";
	ifstream in(argv[1]);
	if (!in.is_open()) {
		cout << "Can't read from file\n";
		return 1;
	}

	unsigned int num_cases;
	in >> num_cases;
	OUT_DEBUG << "num of cases: " << num_cases << '\n';

	for (unsigned int i = 0; i < num_cases; i++) {
		doCase(in, i+1);
	}

	return 0;
}
