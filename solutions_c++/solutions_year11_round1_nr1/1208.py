#include <list>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <algorithm>

#define LEN 256

struct p1
{
  int N;
  int PD;
  int PG;
};

static std::string
get_answer(struct p1* p);

static void
parse_me(std::string filename);

static int gcd(int a, int b);

static std::string
get_answer(struct p1* p)
{
  int D = 0;
  int Dw = 0;
  int R = 0;
  int Rw = 0;
  int tmp = 0;
  int k;
  int A;

  if (p->PD != 100 && p->PG == 100)
    return "Broken";
  if (!p->PG && p->PD)
    return "Broken";

  Dw = p->PD / gcd(p->PD, 100);
  D = 100 / gcd(p->PD, 100);

  if (D > p->N)
    return "Broken";

  tmp = gcd(100, p->PG);
  A = 100 / tmp * Dw - p->PG / tmp * D;

  return "Possible";
}

static int gcd(int a, int b)
{
  int tmp;

  while (b) {
    tmp = b;
    b = a % b;
    a = tmp;
  }
  return a;
}

static void
parse_me(std::string filename)
{
  std::fstream file;
  char buf[LEN];
  unsigned int len;
  struct p1 *p;

  file.open(filename.c_str());

  file.getline(buf, LEN);
  len = atoi(buf);

  for (int i = 0; i < len; ++i)
    {
      p = new p1;
      file.getline(buf, LEN, ' ');
      p->N = atoi(buf);
      file.getline(buf, LEN, ' ');
      p->PD = atoi(buf);
      file.getline(buf, LEN);
      p->PG = atoi(buf);
      std::cout << "Case #" << i + 1 << ": " << get_answer(p) << std::endl;
    }

  file.close();
}

int
main(int argc, char** argv)
{
  if (argc < 2)
    return 1;

  parse_me(argv[1]);

  return 0;
}
