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

/*****************************************************************************/

static bool solveSnapper(uint x, uint k) {
	uint mask = (1 << x) - 1;
	return (k & mask) == mask;
}

int main (int argc, char * const argv[]) {
	uint numCases;
	std::cin >> numCases;
	
	for (int i = 0; i < numCases; ++i) {
		uint x, k;
		std::cin >> x >> k;
		
		std::cout << "Case #" << (i + 1) << ": " << (solveSnapper(x, k) ? "ON" : "OFF") << std::endl;
	}
	
    return 0;
}
