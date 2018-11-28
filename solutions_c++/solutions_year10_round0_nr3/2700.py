// Jeff McGlynn
// Google Codejam 2010.

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

/*****************************************************************************/

static uint solveThemePark(uint R, uint k, const std::vector<uint>& groups) {
	uint income = 0;
	uint groupIdx = 0;
	
	for (uint i = 0; i < R; ++i) {
		uint startIdx = groupIdx;
		uint accum = groups[groupIdx];
				
		// Try to fit as many groups into the cart as possible.
		while (accum) {
			uint nextGroup = (groupIdx + 1);
			if (nextGroup >= groups.size()) nextGroup = 0;
			
			groupIdx = nextGroup;
			
			if (nextGroup != startIdx) {
				uint nextSize = groups[nextGroup];
				
				if (accum + nextSize <= k) {
					accum += nextSize;
					continue;
				}
			}
			
			// No more groups fit, run the ride.
			income += accum;
			accum = 0;
		}
	}
	
	return income;
}

int main (int argc, char * const argv[]) {
	uint numCases;
	std::cin >> numCases;
	
	for (uint i = 0; i < numCases; ++i) {
		// Read metadata line.
		uint R, k, N;
		std::cin >> R >> k >> N;
		
		// Now read the N groups.
		std::vector<uint> groups(N);
		for (uint j = 0; j < N; ++j) {
			std::cin >> groups[j];
		}
		
		// Solve.
		std::cout << "Case #" << (i + 1) << ": " << solveThemePark(R, k, groups) << std::endl;
	}
	
    return 0;
}
