#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <vector>
#include <utility>

using namespace std;

class Solver {
  private:
#if 0
    typedef pair <char, char>        mpair_t;
    typedef map <mpair_t>            mapping_t;
    mapping_t map_m;

    void construct_mapping(void) {
        map_m.insert(mpair_t('a', 'y'));
        map_m.insert(mpair_t('b', 'n'));
        map_m.insert(mpair_t('c', 'f'));
        map_m.insert(mpair_t('d', 'i'));
        map_m.insert(mpair_t('e', 'c'));
        map_m.insert(mpair_t('f', 'w'));
        map_m.insert(mpair_t('g', 'l'));
        map_m.insert(mpair_t('h', 'b'));
        map_m.insert(mpair_t('j', 'u'));
        map_m.insert(mpair_t('k', 'o'));
        map_m.insert(mpair_t('l', 'm'));
        map_m.insert(mpair_t('m', 'x'));
        map_m.insert(mpair_t('n', 's'));
        map_m.insert(mpair_t('o', 'e'));
        map_m.insert(mpair_t('p', 'v'));
        map_m.insert(mpair_t('q', '1'));
        map_m.insert(mpair_t('r', 'p'));
        map_m.insert(mpair_t('s', 'd'));
        map_m.insert(mpair_t('t', 'r'));
        map_m.insert(mpair_t('u', 'j'));
        map_m.insert(mpair_t('v', 'g'));
        map_m.insert(mpair_t('w', 't'));
        map_m.insert(mpair_t('x', 'h'));
        map_m.insert(mpair_t('y', 'a'));
        map_m.insert(mpair_t('z', '2'));
        map_m.insert(mpair_t(' ', ' '));
        map_m.insert(pair<char, char>('a', 'b'))
    }
#endif

    typedef unsigned int             intu;

    vector<string>  cases;
    intu           t_m;


    char get_map(char c) {
        switch (c) {
            case 'a':
              return 'y';
            case 'b':
              return 'h';
            case 'c':
              return 'e';
            case 'd':
              return 's';
            case 'e':
              return 'o';
            case 'f':
              return 'c';
            case 'g':
              return 'v';
            case 'h':
              return 'x';
            case 'i':
              return 'd';
            case 'j':
              return 'u';
            case 'k':
              return 'i';
            case 'l':
              return 'g';
            case 'm':
              return 'l';
            case 'n':
              return 'b';
            case 'o':
              return 'k';
            case 'p':
              return 'r';
            case 'q':
              return 'z';
            case 'r':
              return 't';
            case 's':
              return 'n';
            case 't':
              return 'w';
            case 'u':
              return 'j';
            case 'v':
              return 'p';
            case 'w':
              return 'f';
            case 'x':
              return 'm';
            case 'y':
              return 'a';
            case 'z':
              return 'q';

            case ' ':
              return ' ';
            default:
              cerr << "Unknown character " << c << endl;
              exit(-1);
              return '-';
        }
    }

  public:

    Solver(void) : t_m(0) {};

    void read_data(void) {
        cin >> t_m;

        cin.ignore();
        for (intu i = 0; i < t_m; i++) {
          string tmp;
            getline(std :: cin, tmp);
            cases.push_back(tmp);
        }
    }

    string parse_string(string s) {
      string ret;
      intu length = s.length();

        for (int i = 0; i < length; i++) {
          char cm = get_map(s[i]);// map_m.find(s[i])->second;
            ret.push_back(cm);
#ifdef DEBUG
            fprintf(stdout, "%c", cm);
#endif // DEBUG
        }
#ifdef DEBUG
        fprintf(stdout, "\n");
#endif // DEBUG

      return ret;
    }

    void parse_data(void) {
      vector<string> :: iterator it;
      int32_t i = 1;

        for (it = cases.begin(); it < cases.end(); it++) {
          string parsed = parse_string(*it);
            cout << "Case #" << i++ << ": "<< parsed << endl;
        }
    }

    ~Solver(void) {};
};

int main(int argc, char **argv) {
  Solver s;

    s.read_data();
    s.parse_data();

  return 0;
}
