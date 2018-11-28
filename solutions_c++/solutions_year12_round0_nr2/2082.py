#include <iostream>
#include <algorithm>

int main()
{
  unsigned nCase;
  std::cin >> nCase;
  for (unsigned iCase = 1; iCase <= nCase; ++iCase) {
    unsigned N, S, p;
    std::cin >> N >> S >> p;

    unsigned y = 0, t = 0, n = 0;
    for (unsigned i = 0; i < N; ++i) {
      unsigned ti;
      std::cin >> ti;
      unsigned x = ti/3;
      
      switch (ti) {
      case 0:
	if (0 >= p)
	  ++y;
	else
	  ++n;
	break;

      case 1:
	if (1 >= p)
	  ++y;
	else
	  ++n;
	break;

      case 29:
      case 30:
	++y;
	break;

      default:

	switch (ti % 3) {
	case 0:
	  if (x >= p)
	    ++y;
	  else if ((x+1) >= p)
	    ++t;
	  else
	    ++n;
	  break;
	case 1:
	  if ((x+1) >= p)
	    ++y;
	  else
	    ++n;
	  break;
	default: // case 2
	  if ((x+1) >= p)
	    ++y;
	  else if ((x+2) >= p)
	    ++t;
	  else
	    ++n;
	  break;
	}
      }
    }

    std::cout << "Case #" << iCase << ": " << (y + std::min(t, S)) << std::endl;
  }
  
  return 0;
}
