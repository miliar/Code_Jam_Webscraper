#include <iostream>


using namespace std;

static const char X_WON[] = "X won";
static const char O_WON[] = "O won";
static const char DRAW[] = "Draw";
static const char NO_COMP[] = "Game has not completed";

    bool  xwons = false,
          owons = false;

int check(int line) {
    if(line == 352 || line == 348)
      xwons = true;
    if(line == 316 || line == 321)
      owons = true;

    return line < 300 ? 0 : 1;
}

void makeTest(int number) {
  int l1 = 0,
      l2 = 0,
      l3 = 0,
      l4 = 0,
      d1 = 0,
      d2 = 0,
      v1 = 0,
      v2 = 0,
      v3 = 0,
      v4 = 0;

  xwons = false;
  owons = false;

  char tmp;

  /* FIRST LINE */
  cin >> tmp; 
    l1 += tmp;
    d1 += tmp;
    v1 += tmp;

  cin >> tmp;
    l1 += tmp;
    v2 += tmp;

  cin >> tmp;
    l1 += tmp;
    v3 += tmp;

  cin >> tmp;
    l1 += tmp;
    d2 += tmp;
    v4 == tmp;

  /* SECOND LINE */
  cin >> tmp; 
    l2 += tmp;
    v1 += tmp;

  cin >> tmp;
    l2 += tmp;
    d1 += tmp;
    v2 += tmp;

  cin >> tmp;
    l2 += tmp;
    d2 += tmp;
    v3 += tmp;

  cin >> tmp;
    l2 += tmp;
    v4 += tmp;

  /* THIRD LINE */

  cin >> tmp; 
    l3 += tmp;
    v1 += tmp;

  cin >> tmp;
    l3 += tmp;
    d2 += tmp;
    v2 += tmp;

  cin >> tmp;
    l3 += tmp;
    d1 += tmp;
    v3 += tmp;

  cin >> tmp;
    l3 += tmp;
    v4 += tmp;

  /* FORTH LINE */

  cin >> tmp; 
    l4 += tmp;
    d2 += tmp;
    v1 += tmp;

  cin >> tmp;
    l4 += tmp;
    v2 += tmp;

  cin >> tmp;
    l4 += tmp;
    v3 += tmp;

  cin >> tmp;
    l4 += tmp;
    d1 += tmp;
    v4 += tmp;

    int l1c,l2c,l3c,l4c;

    l1c = check(l1); l2c = check(l2); l3c = check(l3); l4c = check(l4);
    check(d1); check(d2);
    check(v1); check(v2); check(v3); check(v4);

    //cout << l1 << ' ' << l2 << ' ' << l3 << ' ' << l4 << ' ' << d1 << ' ' << d2 << '\n';

    cout << "Case #" << number << ": ";
    if( xwons || owons) {
      if(xwons && owons) {
        cout << DRAW << '\n';
      } else if (xwons) {
        cout << X_WON << '\n';
      } else {
        cout << O_WON << '\n';
      }
      return;
    }

    if(l1c && l2c && l3c && l4c) 
      cout << DRAW << '\n';
    else 
      cout << NO_COMP << '\n';
}

int main(int argc, char* argv[]) {

  ios::sync_with_stdio(false);

  int number_of_tests;
  cin >> number_of_tests;

  for(int i = 1; i <= number_of_tests; ++i) {
    makeTest(i);
  }

  return 0;
}