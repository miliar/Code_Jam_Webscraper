#include <iostream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

map<int, bool> IsHappyMem[11];
int Bases[10000];
int Count;

bool IsHappy( int Number, int Base )
{
  map<int, bool>::iterator it = IsHappyMem[Base].find( Number );
  if (it != IsHappyMem[Base].end())
    return it -> second;

  IsHappyMem[Base].insert( pair<int, bool>( Number, false ) );
  bool Result;
  int NewNumber = 0;
  int a = Number;
  while (a > 0)
  {
    int Digit = a % Base;
    NewNumber += Digit * Digit;
    a /= Base;
  }

  if (NewNumber == 1)
    Result = true;
  else
    Result = IsHappy( NewNumber, Base );

  IsHappyMem[Base][Number] = Result;
}

int Solve()
{
  int i = 2;

  while (true)
  {
    bool test = true;
    for (int j = 0; j < Count; j++)
      if (!IsHappy( i, Bases[j] ))
      {
        test = false;
        break;
      }

    if (test)
      return i;

    i++;
  }
}

int main()
{
  int T;
  cin >> T;
  string EmptyLine;
  getline( cin, EmptyLine );
  for (int i = 0; i < T; i++)
  {
    string S;

    getline( cin, S );

    stringstream ss( stringstream::in | stringstream::out );
    ss << S;
    int Base;
    Count = 0;
    while (ss >> Base)
    {
      Bases[Count] = Base;
      Count++;
    }

    cout << "Case #" << i + 1 << ": " << Solve() << endl;
  }
}

