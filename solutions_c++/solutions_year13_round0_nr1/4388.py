#include <iostream>
#include <string>

bool not_win_elem(char c, char t)
{
   return t != c && t != 'T';
}

bool win_raw(char c, std::string const & s)
{
   for (size_t l = 0; l != 4; ++l)
      if (not_win_elem(c, s[l]))
         return false;

   return true;
}

bool win_col(char c, std::string s[4], size_t cl)
{
   for (size_t l = 0; l != 4; ++l)
      if (not_win_elem(c, s[l][cl]))
         return false;

   return true;
}

bool win_diag_s(char c, std::string s[4])
{
   for (size_t l = 0; l != 4; ++l)
      if (not_win_elem(c, s[l][l]))
         return false;

   return true;
}

bool win_diag_b(char c, std::string s[4])
{
   for (size_t l = 0; l != 4; ++l)
      if (not_win_elem(c, s[l][3 - l]))
         return false;

   return true;
}

bool win(char c, std::string s[4])
{
   for (size_t l = 0; l != 4; ++l)
   {
      if (win_raw(c, s[l])) return true;
      if (win_col(c, s, l)) return true;
   }

   return win_diag_s(c, s) || win_diag_b(c, s);
}

bool not_finished(std::string s[4])
{
   for (size_t l = 0; l != 4; ++l)
      if (s[l].find('.') != std::string::npos)
         return true;

   return false;
}

std::string process(std::string s[4])
{
   if (win('X', s)) return "X won";
   if (win('O', s)) return "O won";

   if (not_finished(s)) return "Game has not completed";

   return "Draw";
}

int main(int argc, char * argv[])
{
   size_t N = 0;
   std::cin >> N;

   for (size_t l = 0; l != N; ++l)
   {
      std::string s[4];
      std::getline(std::cin, s[0]);

      for (size_t k = 0; k != 4; ++k)
         std::getline(std::cin, s[k]);

      std::cout << "Case #" << l + 1 << ": " << process(s) << std::endl;
   }
}

