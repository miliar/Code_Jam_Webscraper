#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <set>
#include <list>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("file.out");

#ifdef _DEBUG
#define fin cin
#define fout cout
#endif

int main() {
  int T = 0;
  fin >> T;
  for(int t = 0; t < T; t++) {
    list<string> cur;
    list<int> cols; //Список колонок
    int N = 0;
    fin >> N;
    for(int i = 0; i < N; i++) {
      string str;
      fin >> str;
      cur.push_back(str);
      size_t tmp = str.find_last_of('1');
      cols.push_back(tmp == string::npos ? 0 : tmp+1);
    }
    //Массив введен
    int res = 0;
    for(int i = 0; i < N; i++) {
      list<int>::iterator iter = cols.begin();
      for(int k = 0; k < i; k++) iter++;
      //Цикл по строчкам
      //Ищем первую строчку, которая подходит стоять на первой строке
      list<int>::iterator j = cols.begin();
      int num = 0;
      for(int k = 0; k < i; k++) j++;
      for(; j != cols.end(); j++, num++) {
        if(*j <= i+1)
          break;
      }
      /*if(j == cols.end())
        continue;*/
      if(num == 0)
        continue;
      res += num;
      cols.insert(iter, *j);
      cols.erase(j);
    }
    fout << "Case #" << t+1 << ": " << res << endl;
  }
}
