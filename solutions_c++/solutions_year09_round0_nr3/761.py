#include <iostream>
#include <string>
#include <iomanip>

const std::string wcj = "welcome to code jam";
std::string word;

int mas[50][501];

const int MOD=10000;

int Do()
{
  if (word.length()<wcj.length())
    return 0;
  for (int i = 0; i < 501;++i)
    mas[0][i] = 1;
  for (int i = 0; i < 501;++i)
    for (int j = 1; j < 50;++j)
    mas[j][i] = 0;
  mas[0][0] = word[0]==wcj[0];
  for (int i = 0; i < wcj.length(); ++i)
  {
    int ch = wcj[i];
    for (int j = i; j < word.length();++j)
    {
      if (ch != word[j])
      {
	mas[i+1][j+1] = mas[i+1][j];
      }else
      {
	mas[i+1][j+1] = (mas[i+1][j]+mas[i][j])%MOD;
      }
      //      std::cerr << i << " " << j << " " << mas[i+1][j+1] << std::endl;
    }
  }
  return mas[wcj.length()][word.length()];
}


int main()
{
  int N;
  std::cin >> N;
  std::getline(std::cin, word);
  for (int i = 0; i < N; ++i)
  {
    std::getline(std::cin, word);
    //    std::cerr << word << std::endl;
    int n = Do();
    std::cout << "Case #" << (i+1) << ": ";
    std::cout.fill('0');
    std::cout << std::setw(4) << n << std::endl;
  }
}
