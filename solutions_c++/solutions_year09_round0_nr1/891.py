#include <iostream>
#include <vector>

using namespace std;

int L, D, N;
vector<string> Alph;
vector<string> Tests;

bool debug = false;
//bool debug = true;

int calcVariants(string & test)
{
    vector<string> groups(L);
    size_t s1 = -1, s2 = -1; // индексы начала и окончания группы

    // вычисляем группы
    for(int i = 0; i < L; i++)
    {
        if (test[s2+1] == '(')
        {
            s1 = s2+1;
            s2 = test.find(')', s1);
            //if (debug) cout << "s1:" << s1 << " s2:" << s2 << endl;
            groups[i] = test.substr(s1+1, s2-s1-1);
        }
        else
        {
            groups[i] = test[s2+1];
            s1 = s2+1;
            s2 = s2+1;
        }
        if (debug) cout << groups[i] << " ";
    }
    if (debug) cout << endl;

    int res = 0;


    // нам на вход пришел тест
    // для этого теста перебираем все слова в алфавите
    for (int alph_ind = 0; alph_ind < Alph.size(); alph_ind++)
    {
        bool word_is_ok = true;
        if(debug) cout << "  alph:" << Alph[alph_ind] << endl;
        // для каждого слова в алфавите (и теста) перебираем все буквы
        for (int letter = 0; letter < L; letter++)
        {
            // буква слова алфавита
            char c = Alph[alph_ind].at(letter);
            if(debug) cout << letter << " : " << c << "  in " << groups[letter] << endl;
            // если эта буква содержится в группе номер letter теста случая - все ок
            // если нет - тогда данное слово алфавита не подходит для данного тестового случая
            if(groups[letter].find(c) == string::npos)
            {
                if(debug) cout << "FAIL" << endl;
                word_is_ok = false;
                break;
            }
        }
        if (word_is_ok)
        {
            // если слово подошло, увеличиваем на единицу результат
            res++;
        }
    }

    return res;
}

int main(void)
{
  /*Getting data*/
  cin >> L >> D >> N;
  Alph.resize(D);
  Tests.resize(N);
  for(int i = 0; i < D; i++)
  {
      string tmp;
      cin >> tmp;
      Alph[i] = tmp;
  }
  for (int i = 0; i < N; i++)
  {
      string tmp;
      cin >> tmp;
      Tests[i] = tmp;
  }

  /*
  cout << "Alphabet:" << endl;
  for(int i = 0; i < Alph.size(); i++)
  {
      cout << Alph[i] << endl;
  }
  cout << "Tests:" << endl;
  for(int i = 0; i < Tests.size(); i++)
  {
      cout << Tests[i] << endl;
  }
  */
  cout << endl;
  for (int i = 0; i < Tests.size(); i++)
  {
      cout << "Case #" << i+1 << ": ";
      cout << calcVariants(Tests[i]) << endl;
  }
  return 0;
}
