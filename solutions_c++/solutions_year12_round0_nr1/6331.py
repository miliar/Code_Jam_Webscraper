#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>

#define LINE_SZ (101)

namespace
{
   std::string printOutput(int itest, std::string line)
   {
      std::stringstream ss;
      ss << "Case #" << itest << ": " << line;
      return ss.str();
   }

} // anonymous



// a b c d e f g h i j k l m n o p q r s t u v w x y z
// y h e s o c v x d u i g l b k r z t n w j p f m a q

char dico[26] = {
   'y', 'h', 'e', 's', 'o', 'c', 'v', 'x',
   'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
   'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
};

void translate(char* line)
{
   for (unsigned int i = 0; line[i]; ++i)
   {
      if (line[i] != ' ')
      {
         int idx = line[i] - 'a';
         line[i] = dico[idx];
      }
   }
}

int main(int argc, const char* argv[])
{
   if (argc != 3)
      return 1;
   
   std::cout << argv[1] << " " << argv[2] << std::endl;

   std::ifstream fin(argv[1], std::ios::in);
   std::ofstream fout(argv[2], std::ios::out);
   if (!fin.is_open())
      return 1;
   if (!fout.is_open())
   {
      fin.close();
      return 1;
   }

   int ntests = 0;
   char line[LINE_SZ];
   
   fin >> ntests;
   fin.getline(line, LINE_SZ);
   for (int itest = 1; itest <= ntests; ++itest)
   {   
      fin.getline(line, LINE_SZ);

      translate(line);

      fout << printOutput(itest, line) << std::endl;
   }

}



// a b c d e f g h i j k l m n o p q r s t u v w x y z
// y h e s o c v x d u i g l b k r z t n w j p f m a q
