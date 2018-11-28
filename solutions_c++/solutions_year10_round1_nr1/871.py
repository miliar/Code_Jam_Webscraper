#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;

char game[51][51];

void clear_game() {
  for(int i = 0; i < 51; i++) for(int j = 0; j < 51; j++) game[i][j] = 0;
}

void transpose(int N) {
  char tmp;
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < i; j++) {
      tmp = game[i][j];
      game[i][j] = game[j][i];
      game[j][i] = tmp;
    }
  }
}

void mirror(int N) {
  char tmp;
  for(int j = 0; j < N/2; j++) {
    for(int i = 0; i < N; i++) {
      tmp = game[i][N-j-1];
      game[i][N-j-1] = game[i][j];
      game[i][j] = tmp;
    }
  }

}

void gravity(int N) {
  for(int j = 0; j < N; j++) {
    
    string str = "";
    for(int i = N-1; i >= 0; i--) {
      if(game[i][j] != '.') str += game[i][j];
    }
    for(int i = 0; i < N; i++) game[i][j] = '.';
    for(int i = 0; i < str.size(); i++) {
      game[N-1-i][j] = str[i];
    }
  }
}

void showgame(int N) {
  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      cout << game[i][j];
    }
    cout << endl;
  }
}

int main(int argc, char *argv[])
{
  if(argc < 2) return -1;
  ifstream infile(argv[1]);
  
  int numtests = 0;
  infile >> numtests;
  char inputstring[501];
  string dummy = "";
  for(int test_idx = 0; test_idx < numtests; test_idx++) {

    /*******************/
    int N;
    infile >> N;
    int K;
    infile >> K;
    clear_game();
    // The following ensures that the \n is captured from the line containing the previous integer.
    infile.getline(inputstring, 501);

    for(int i = 0; i < N; i++) {
      memset(inputstring, 0, 51);
      infile.getline(inputstring, 51);
      for(int j = 0; j < N; j++) game[i][j] = inputstring[j];
    }

    /*******************/
    // Process data
    //showgame(N);
    transpose(N);
    mirror(N);
    gravity(N);
    //cout << endl;
    //showgame(N);
    int nred = 0, nblue = 0;
    string testred = "";
    string testblue = "";
    size_t found = 0;
    
    for(int i = 0; i < K; i++) {testred += "R"; testblue += "B";}
    //cout << testred << "," << testblue << endl;
    for(int i = 0; i < N; i++) {
      string teststr(game[i]);
      if(nred == 0) {
	found=teststr.find(testred);
	if (found!=string::npos) {
	  nred++;
	  if(nblue > 0) {
	    break;
	  }
	}
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if (found!=string::npos) {
	  nblue++;
	  if(nred > 0) {
	    break;
	  }
	}
      }
    }
    //cout << nred << "," << nblue << endl;

    // Vertical test:
    for(int j = 0; j < N; j++) {
      string teststr = "";
      for(int i = 0; i < N; i++) teststr += game[i][j];
      if(nred == 0) {
	found=teststr.find(testred);
	if(found != string::npos) nred++;
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if(found != string::npos) nblue++;
      }
      
    }
    // Diagonal data: forward slash, top left to diagonal
    int drow = -1, dcol = 1;
    int row, col;
    for(int i = 0; i < N; i++) {
      if(nred > 0 && nblue > 0) break;
      row = i;
      col = 0;
      string teststr = "";
      while(row >= 0 && col < N) {
	teststr += game[row][col];
	row += drow;
	col += dcol;
      }
      if(nred == 0) {
	found=teststr.find(testred);
	if(found != string::npos) nred++;
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if(found != string::npos) nblue++;
      }

    }
    //cout << nred << "," << nblue << endl;
    // Diagonal data: forward slash, diagonal, to bottom right.
    for(int j = 0; j < N; j++) {
      if(nred > 0 && nblue > 0) break;
      row = N-1;
      col = j;
      string teststr = "";
      while(row >= 0 && col < N) {
	teststr += game[row][col];
	row += drow;
	col += dcol;
      }
      if(nred == 0) {
	found=teststr.find(testred);
	if(found != string::npos) nred++;
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if(found != string::npos) nblue++;
      }

    }
    //cout << nred << "," << nblue << endl;
    // Diagonal data: back slash, bottom left, to diagonal.
    drow = +1; dcol = +1;
    for(int i = 0; i < N; i++) {
      if(nred > 0 && nblue > 0) break;
      row = i;
      col = 0;
      string teststr = "";
      while(row < N && col < N) {
	teststr += game[row][col];
	row += drow;
	col += dcol;
      }
      //if(i == 1) cout << "TEST STRING: " << teststr << "," << nred << endl;
      if(nred == 0) {
	found=teststr.find(testred);
	if(found != string::npos) nred++;
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if(found != string::npos) nblue++;
      }

    }
    //cout << nred << "," << nblue << endl;
    // Diagonal data: back slash, bottom left, to diagonal.
    drow = +1; dcol = +1;
    for(int j = 0; j < N; j++) {
      if(nred > 0 && nblue > 0) break;
      row = 0;
      col = j;
      string teststr = "";
      while(row < N && col < N) {
	teststr += game[row][col];
	row += drow;
	col += dcol;
      }
      if(nred == 0) {
	found=teststr.find(testred);
	if(found != string::npos) nred++;
      }
      if(nblue == 0) {
	found=teststr.find(testblue);
	if(found != string::npos) nblue++;
      }

    }
    //cout << nred << "," << nblue << endl;
    
    string outstring = "Neither";
    if(nred > 0 && nblue > 0) {
      outstring = "Both";
    } else if(nred > 0) {
      outstring = "Red";
    } else if(nblue > 0) {
      outstring = "Blue";
    }
    cout << "Case #" << (test_idx+1) << ": " << outstring;
    
    // Output relevant data.

    // Terminate output properly.
    cout << endl;
  }

  return 0;
}


template<class T> 
void ShowVector(vector<T> showme, string startstr = "", string endstr = "")
{
  cout << startstr << endl;
  for(int i = 0; i < showme.size(); i++) {
    cout << showme[i] << endl;
  }
  cout << endstr << endl;
}
