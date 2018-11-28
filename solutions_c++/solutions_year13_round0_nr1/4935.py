#include <string>
#include <iostream>


using namespace std;

const int DOT = 0;
const int iX = 1;
const int iO = 1<<5;
const int iT = iX + iO;

char table[4][4];
bool hasDot;

void readTable()
{
  hasDot = false;
  string line;
  for (int i = 0; i < 4; i++)
  {
    cin >> line;
    for (int j = 0; j < 4; j++) {
      if (line[j]=='.') hasDot=true;
      table[i][j] = line[j];
    }
  }
}
bool isDone;

void won(char c) { cout << c << " won"; isDone = true;}
void draw() { cout << "Draw"; }
void incp() { cout << "Game has not completed"; }

bool check (char c, char p)
{
  if (p==c || p=='T') return true;
  return false;
}

void processTable(char c)
{
  int sum;
  for (int j = 0; j < 4; j++) {
    bool col = true;
    bool row = true;
    bool diag1 = true;
    bool diag2 = true;
    for (int i = 0; i < 4; i++)
    {
      row &= check(c, table[i][j]);
      col &= check(c, table[j][i]);
      diag1 &= check(c, table[i][i]);
      diag2 &= check(c, table[3-i][i]);
    }
    if (row || col ||diag1 || diag2)
    {
      won(c);
      return;
    }
  }
}

int main(int argc, const char *argv[])
{

  int T;
  cin >> T;
  for(int it=1; it <=T ; it++ )
  {
    isDone = false;
    cout << "Case #"<<it <<": ";
    readTable();
    processTable('X');
    processTable('O');
    if (!isDone)
    {
    if (hasDot)
    {
      incp();
    }
    else
    {
      draw();
    }
    }
    cout << std::endl;
  }
  return 0;
}

