#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

// first direction is Y, second is X
int DIRECTIONS[8][2] = {
  {-1, 0},
  {1, -1},
  {0, 1},
  {1, 1},
  {1, 0},
  {-1, -1},
  {0, -1},
  {-1, -1}
};

string lower(const string& str)
{
  string result;
  for (size_t k = 0; k < str.size(); k++) {
    if (str[k] >= 'A' && str[k] <= 'Z') {
      result += (str[k] + 32);
    } else {
      result += str[k];
    }
  }
  return result;
}

int string_match(int direction,
                 const size_t y,
                 const size_t x,
                 const vector<vector<char> >& grid,
                 const string& pattern1,
                 const string& pattern2)
{
  int dx = DIRECTIONS[direction][0];
  int dy = DIRECTIONS[direction][1];

  int x_correction = 0;
  int y_correction = 0;
  if (dx > 0) {
    x_correction = -1;
  }
  if (dy > 0) {
    y_correction = -1;
  }
  int final_x = dx * pattern1.size() + x + x_correction;
  int final_y = dy * pattern1.size() + y + y_correction;
  /*
  cout << "Looking for pattern: " << pattern1
       << " at (y=" << y << ", x=" << x << ")"
       << " moving at (dy=" << dy << ", dx=" << dx << ")."
       << " end coordinates at (y=" << final_y << ", x=" << final_x << ")" << endl;
  print_grid(grid);
  */
  if (final_x >= grid[0].size() ||
      final_x < 0) {
    //cout << "x out of bounds." << endl;
    return -1;
  }

  if (final_y >= grid.size() ||
      final_y < 0) {
    //cout << "grid y = " << grid.size() << endl;
    //cout << "y out of bounds." << endl;
    return -1;
  }

  int current_x = x, current_y = y;

  for (size_t k = 0; k < pattern1.size(); k++) {
    char current_letter = grid[current_y + k * dy][current_x + k * dx];
    /*
    cout << "position (y=" << (current_y + k * dy)
         << ", x=" << current_x + k * dx << ")" << endl;
    cout << current_letter << " vs " << pattern1[k] << endl;
    */
    if (current_letter != pattern1[k]) {
      //cout << "no match" << endl;
      return -1;
    }
  }
  //cout << "match found!" << endl;
  return 1;
}

int rotate(const vector<vector<char> >& GRID1, vector<vector<char> >& GRID2)
{
  GRID2.clear();
  GRID2.resize(GRID1.size());
  for (unsigned int i = 0; i < GRID1.size(); i++) {
    GRID2[i].resize(GRID1.size());
  }
  for (unsigned int y = 0; y < GRID1.size(); y++) {
    for (unsigned int x = 0; x < GRID1[0].size(); x++) {
      GRID2[x][GRID2.size() - y - 1] = GRID1[y][x];
    }
  }
}

int gravity(vector<vector<char> >& GRID)
{
  char *tmp = new char[GRID.size()];
  for (int x = 0; x < GRID.size(); x++) {
    memset(tmp, 0, GRID.size());

    int z = 0;
    int ptr = 0;
    while (z < GRID.size()) {
      if (GRID[z][x] != '.') {
        tmp[ptr] = GRID[z][x];
        ptr++;
      } 
      z++;
    }

    int ptr2 = 0;
    for (unsigned int k = 0; k < GRID.size(); k++) {
      if (k < (GRID.size() - ptr))
        GRID[k][x] = '.';
      else {
        GRID[k][x] = tmp[ptr2];
        ptr2++;
      }
    }
    
  }
  delete [] tmp;
}

void print_grid(const vector<vector<char> >& grid)
{
  for (unsigned int i = 0; i < grid[0].size(); i++) {
    cout << "\t" << i;
  }
  cout << endl;
  for (unsigned int y = 0; y < grid.size(); y++) {
    cout << y;
    for (unsigned int x = 0; x < grid[0].size(); x++) {
      cout << "\t" << grid[y][x];
    }
    cout << endl;
  }
}


int main()
{
  unsigned int NCASES;

  cin >> NCASES;

  for (unsigned int CASE = 0; CASE < NCASES; ++CASE) {
    unsigned int N, K;

    cin >> N >> K;
    vector<vector<char> > BOARD1(N);

    string line;
    getline(cin, line);

    for (unsigned int n = 0; n < N; n++) {
      getline(cin, line);
      for (unsigned int n2 = 0; n2 < N; n2++) {
        BOARD1[n].push_back(line[n2]);
        //cout << BOARD1[n][n2];
      }
      //cout << endl;
    }

    vector<vector<char> > BOARD2;
    rotate(BOARD1, BOARD2);
    //print_grid(BOARD2);
    gravity(BOARD2);
    //cout << endl;
    //print_grid(BOARD2);

    string match_1(K, 'R');
    string match_2(K, 'B');

    bool red = false;
    bool blue = false;
    for (unsigned int x = 0; x < N; ++x) {
      for (unsigned int y = 0; y < N; y++) {
        for (unsigned int j = 0; j < match_1.size();j++) {
          for (unsigned int dir = 0; dir < 8; dir++) {
            if (string_match(dir, y, x, BOARD2, match_1, match_2) == 1) {
              red = true;
            }
            if (string_match(dir, y, x, BOARD2, match_2, match_1) == 1) {
              blue = true;
            }
          }
        }
      }
    }

    cout << "Case #" << (CASE + 1) << ": ";
    if (red && blue) {
      cout << "Both";
    } else if (!red && !blue) {
      cout << "Neither";
    } else if (red) {
      cout << "Red";
    } else {
      cout << "Blue";
    }
    cout << endl;
  }
}
