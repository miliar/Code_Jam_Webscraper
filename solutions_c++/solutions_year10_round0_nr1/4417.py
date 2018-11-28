#include <iostream>
#include <vector>

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef unsigned long long u64;

#define ct_assert(x) typedef char ct ## __LINE__[(x) ? 1 : -1]

ct_assert(sizeof(u8) == 1);
ct_assert(sizeof(u16) == 2);
ct_assert(sizeof(u32) == 4);
ct_assert(sizeof(u64) == 8);

int main(int argc, char**argv)
{
  int nlines = 0;
  std::cin >> nlines;

  for (int i = 0; i < nlines; i++)
  {
    int N, K;
    std::cin >> N >> K;

    u32 snappers = 0;
    u32 power = 0;

    for (int j = 0; j <= K; j++)
    {
      power = 1;

      for (int k = 0; k < 31; k++)
      {
        power |= ((power & snappers) << 1);
      }

      snappers ^= power;
    }

    bool on = (power & (1 << N));

    std::cout << "Case #" << i + 1 << ": " << (on ? "ON" : "OFF") << std::endl;
  }

  return 0;
}
