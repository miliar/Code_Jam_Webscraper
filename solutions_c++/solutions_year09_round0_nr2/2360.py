#include <iostream>
#include <ext/hash_map>

using namespace std;

int colors[100][100];
int altitude[100][100];

int num_cols, num_rows;

void change_color(int row, int col, int new_color) {
  int old_color = colors[row][col];
  colors[row][col] = new_color;
  if (old_color == 0)
    return;
  if (row > 0 && colors[row - 1][col] == old_color) // N
    change_color(row - 1, col, new_color);
  if (col > 0 && colors[row][col - 1] == old_color) // W
    change_color(row, col - 1, new_color);
  if (col != num_cols - 1 && colors[row][col + 1] == old_color) // E
    change_color(row, col + 1, new_color);
  if (row != num_rows - 1 && colors[row + 1][col] == old_color) // W
    change_color(row + 1, col, new_color);
}

int main() {
  int next_color = 1, num_maps;

  cin >> num_maps;
  
  for (int test_case = 1; test_case <= num_maps; test_case++) {
    cin >> num_rows >> num_cols;
    for (int row = 0; row < num_rows; row++)
      for (int col = 0; col < num_cols; col++) {
        cin  >> altitude[row][col];
        colors[row][col] = 0;
      }
    for (int row = 0; row < num_rows; row++)
      for (int col = 0; col < num_cols; col++) {
        int min_alt = altitude[row][col];
        int min_row = row, min_col = col;

        if (row > 0 && altitude[row - 1][col] < min_alt) {    // N
          min_row = row - 1; min_col = col; min_alt = altitude[row-1][col];
        }
        if (col > 0 && altitude[row][col - 1] < min_alt) {    // W
          min_row = row; min_col = col - 1; min_alt = altitude[row][col - 1];
        }
        if (col !=  num_cols - 1 && altitude[row][col + 1] < min_alt) {    // E
          min_row = row; min_col = col + 1; min_alt = altitude[row][col + 1];
        }
        if (row !=  num_rows - 1 && altitude[row + 1][col] < min_alt) {    // E
          min_row = row + 1; min_col = col; min_alt = altitude[row + 1][col];
        }


        if (colors[row][col] == 0 && colors[min_row][min_col] == 0) {
            colors[row][col] = next_color;
            colors[min_row][min_col] = next_color++;
        } else if (colors[row][col] == 0 && colors[min_row][min_col] != 0) {
            colors[row][col] = colors[min_row][min_col];
        } else if (colors[row][col] != colors[min_row][min_col])
          change_color(min_row, min_col, colors[row][col]);
      }
    cout << "Case #" << test_case << ":" << endl;
    char current_character = 'a';
    __gnu_cxx::hash_map<int, char> output_hash;
    for (int row = 0; row < num_rows; row++) {
      for (int col = 0; col < num_cols; col++) {
        if (output_hash.find(colors[row][col]) == output_hash.end())
          output_hash[colors[row][col]] = current_character++;
        if (col != 0)
          cout << ' ';
        cout << output_hash[colors[row][col]];
      }
      cout << endl;
    }
  }
}
