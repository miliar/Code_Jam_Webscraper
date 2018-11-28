#include <iostream>
#include <fstream>
#include <vector>

std::string process_line(std::ifstream &ifs)
{
  int n;
  int pd;
  int pg;

  ifs >> n;
  ifs >> pd;
  ifs >> pg;

  //if (n == 8 && pd == 100 && pg == 100)
  //  std::cout << n << " " << pd << " " << pg << std::endl;
  bool possible = false;
  for (int j = 0; j <= n; ++j)
  {
  for (int i = 0; i <= j; ++i)
  {
    //if (n == 8 && pd == 100 && pg == 100)
    //    std::cout << ((float)i / n) << std::endl;
    if (((float)i / j) * 100 == pd)
    {
        possible = true;
        break;
    }
  }
  }
  if (!possible)
      return "Broken";
  if (pg == 100 && pd != 100)
      return "Broken";
  if (pg == 0 && pd > 0)
      return "Broken";
  return "Possible";
}

int main()
{
    std::ifstream ifs("../A-small-attempt3.in");
    std::ofstream ofs("output.txt");
    std::string res;

    if (ifs.is_open() && ofs.is_open())
    {
        int nb_lines;

        ifs >> nb_lines;
        for (int i = 0; i < nb_lines; ++i)
        {
            res = process_line(ifs);
            ofs << "Case #" << i+1 << ": " << res.c_str() << std::endl;
            std::cout << "Case #" << i+1 << ": " << res.c_str() << std::endl;
        }
    }
    else
    {
        std::cerr << "Couldn't open input.txt file" << std::endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
