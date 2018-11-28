// Jeff McGlynn
// Google Codejam 2010.
// Round 1A

/*****************************************************************************/
// Types.h

#include <stdint.h>

// Helper typedefs.
typedef uint8_t u8;		/// 8 bit unsigned variable.
typedef int8_t s8;		/// 8 bit signed variable.
typedef uint16_t u16;	/// 16 bit unsigned variable.
typedef int16_t s16;	/// 16 bit signed variable.
typedef uint32_t u32;	/// 32 bit unsigned variable.
typedef int32_t s32;	/// 32 bit signed variable.
typedef uint64_t u64;	/// 64 bit unsigned variable.
typedef int64_t s64;	/// 64 bit signed variable.

typedef char c8;		/// 8 bit character variable.
typedef float f32;		/// 32 bit floating point variable.
typedef double f64;		/// 64 bit floating point variable.

/// Shorthand typedefs.
typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char uchar;

/*****************************************************************************/
// STL.

#include <iostream>
#include <vector>
#include <list>
using namespace std;

#define loop(i,start,n) for (int i = start; i < n; ++i)

/*****************************************************************************/

struct connection {
	int a;
	int b;
};

ostream& caseout() {
	static int casenum = 1;
	return cout << "Case #" << casenum++ << ": ";
}

void solveRope() {
	uint N;
	cin >> N;
	
	vector<connection> conns;
	
	loop(i, 0, N) {
		connection c;
		cin >> c.a >> c.b;
		conns.push_back(c);
	}
	
	int res = 0;
	
	// Find intersections.
	loop(i, 0, conns.size()) {
		connection cur = conns[i];
		
		loop(j, i+1, conns.size()) {
			connection other = conns[j];
			int d1 = cur.a - other.a;
			int d2 = cur.b - other.b;
			
			if (d1 * d2 < 0) {
				// Intersection.
				++res;
			}
		}
	}
	
	caseout() << res << endl;
}

int main(int argc, char * const argv[]) {
	uint numCases;
	cin >> numCases;
	
	for (uint i = 0; i < numCases; ++i) {
		solveRope();
	}
	
    return 0;
}
