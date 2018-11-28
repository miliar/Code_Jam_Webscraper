#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>

using std::cout;
using std::cin;
using std::cerr;
using std::endl;
using std::vector;
using std::string;

bool check_player_win(vector < string > table, char player)
{
  for (int first_index = 0; first_index < 4; ++first_index)
    for (int second_index = 0; second_index < 4; ++second_index)
      if (table[first_index][second_index] == 'T')
        table[first_index][second_index] = player;


  for (int column = 0; column < 4; ++column)
  {
    bool local_result = true;
    for (int row = 0; row < 4; ++row)
      if (table[column][row] != player)
        local_result = false;

    if (local_result)
      return true;
  }

  for (int row = 0; row < 4; ++row)
  {
    bool local_result = true;
    for (int column = 0; column < 4; ++column)
      if (table[column][row] != player)
        local_result = false;

    if (local_result)
      return true;
  }

  bool local_result = true;
  for (int index = 0; index < 4; ++index)
    if (table[index][index] != player)
      local_result = false;

  if (local_result)
    return true;
  
  local_result = true;
  for (int index = 0; index < 4; ++index)
    if (table[index][3 - index] != player)
      local_result = false;

  if (local_result)
    return true;

  return false;
}

bool is_game_finished(const vector < string > &table)
{
  for (int first_index = 0; first_index < 4; ++first_index)
    for (int second_index = 0; second_index < 4; ++second_index)
      if (table[first_index][second_index] == '.')
        return false;

  return true;
}

string solve()
{
  vector < string > table (4);
  for (int index = 0; index < 4; ++index)
    cin >> table[index];

  if (check_player_win(table, 'X'))
    return "X won";
  if (check_player_win(table, 'O'))
    return "O won";
  if (is_game_finished(table))
    return "Draw";

  return "Game has not completed";
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests_count;
  scanf("%d\n", &tests_count);
  for (int test = 0; test < tests_count; ++test)
  {
    cout << "Case #" << test + 1 << ": " << solve() << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}

