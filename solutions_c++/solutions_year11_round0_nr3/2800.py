#ifndef CandyH
#define CandyH

#include <list>

// ----------------------------------------------------------------------------
// Candy
// ----------------------------------------------------------------------------
class Candy
{
public:
  static void calc(std::list<int>& candyList, int bitMask, int* sean, int* patrix, bool* ok); // 0-Sean(add) / 1-Patrix(xor)
};

#endif // CandyH