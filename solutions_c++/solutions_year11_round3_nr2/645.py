#include <iostream>
#include <vector>
using namespace std;

void TestA() {
  int num_case;
  cin >> num_case;
  for (int c = 0; c < num_case; ++c) {
    int cols, rows;
    cin >> rows;
    cin >> cols;
    vector<vector<char> > board(rows);

    int num_blue = 0;
    for (int j = 0; j < rows; ++j) {
      board[j].resize(cols);
      for (int i = 0; i < cols; ++i) {
        cin >> board[j][i];
        if (board[j][i] == '#') ++num_blue;
      }
    }


//     for (int j = 0; j < rows; ++j) {
//      
//       for (int i = 0; i < cols; ++i) {
//         cout << board[j][i] << "\t";
//       }
//       cout << endl;
//     }

    for (int j = 0; j < rows; ++j) {
      for (int i = 0; i < cols; ++i) {
        if (board[j][i] == '#') {
          if (j+1<rows && i+1 < cols) {
            if (board[j][i+1] == '#' && board[j+1][i] == '#' && board[j+1][i+1] == '#') {
              board[j][i] = '/';
              board[j][i+1] = '\\';
              board[j+1][i] = '\\';
              board[j+1][i+1] = '/';
              num_blue -= 4;
            }
          }
        }
      }
    }

    if (num_blue != 0) {
      cout << "Case #" << c+1 << ":\nImpossible\n";
    } else {
      cout << "Case #" << c+1 << ":\n";
           for (int j = 0; j < rows; ++j) {
            
             for (int i = 0; i < cols; ++i) {
               cout << board[j][i];
             }
             cout << endl;
           }
    }
  }
}



void TestC() {
  int num_case;
  cin >> num_case;
  for (int c = 0; c < num_case; ++c) {

    int num_player, min_value, max_value;
    cin >> num_player;
    cin >> min_value;
    cin >> max_value;
    vector<int> player(num_player);
    int i;
    for (i = 0; i < num_player; ++i) {
      cin >> player[i];
    }

    for (i = min_value; i <= max_value; ++i) {
      int j;
      for (j = 0; j < num_player; ++j) {
        int p_value = player[j];
        if ((i%p_value != 0) && (p_value %i != 0)) {
        //if (((i % p_value) != 0) %% ((p_value % i) != 0)) {


          break;
        }
      }
      if (j == num_player) {
        cout << "Case #" << c+1 << ": " << i << endl;
        break;
      }
    }
    if (i == max_value + 1) {
    cout << "Case #" << c+1 << ": NO\n";
    }
    //     for (int j = 0; j < rows; ++j) {
    //      
    //       for (int i = 0; i < cols; ++i) {
    //         cout << board[j][i] << "\t";
    //       }
    //       cout << endl;
    //     }


  }
}


void TestB() {
  int num_case;
  cin >> num_case;
  for (int c = 0; c < num_case; ++c) {

    int num_booster;
    cin >> num_booster;
    double build_time;
    cin >> build_time;
    int num_star;
    cin >> num_star;
    int num_distance;
    cin >> num_distance;

    if (num_booster == 0) {
      build_time = 0;
    }

    vector<double> distance(num_star);
    for (int i = 0; i < num_distance; ++i) {
      cin >> distance[i];
    }

    for (int i = num_distance; i < num_star; ++i) {
      distance[i] = distance[i%num_distance];
    }
//     for (int i = 0; i < num_star; ++i) {
//       cout << distance[i];
//     }
//     cout << endl;

    double no_speed_time = build_time;
    int sum_time = 0;
    for (int i = 0; i < num_star; ++i) {
      sum_time += (distance[i] * 2);
      if (sum_time <= no_speed_time) distance[i] = 0;
      else {
        distance[i] = (sum_time - no_speed_time) / 2;
        break;

      }
    }

    for (int k = 0; k < num_booster; ++k) {
      for (int i = k; i < num_star-1; ++i) {
        if (distance[i]>distance[i+1]) {
          double temp = distance[i+1];
          distance[i+1] = distance[i];
          distance[i] = temp;
        }
      }
    }

    double total_time = 0;
    for (int k = 0; k < num_booster; ++k) {
      total_time += distance[num_star - 1 - k];
    }
    for (int i = 0; i < num_star -num_booster; ++i) {
      total_time += distance[i] * 2;
    }
    total_time+= build_time;
    cout << "Case #" << c+1 << ": " << int(total_time) << endl;
  }
}

void main() {
  TestB();
}