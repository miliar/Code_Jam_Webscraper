#include <cstdio>

char M [10][10];

bool check_horizontal (char &winner) {
  for (int i = 0; i < 4; ++i) {
    bool completed = true;
    winner = '.';
    for (int j = 0; j < 4; ++j) {
      if (M[i][j] == 'T')
	continue;
      else if (M[i][j] == '.') {
	completed = false;
	break;
      }
      else {
	if (winner == '.')
	  winner = M[i][j];
	else
	  if (winner != M[i][j]) {
	    completed = false;
	    break;
	  }
      }
    }
    if (completed)
      return true;
  }
  return false;
}


bool check_vertical (char &winner) {
  for (int j = 0; j < 4; ++j) {
    bool completed = true;
    winner = '.';
    for (int i = 0; i < 4; ++i) {
      if (M[i][j] == 'T')
	continue;
      else if (M[i][j] == '.') {
	completed = false;
	break;
      }
      else {
	if (winner == '.')
	  winner = M[i][j];
	else
	  if (winner != M[i][j]) {
	    completed = false;
	    break;
	  }
      }
    }
    if (completed)
      return true;
  }
  return false;
}

bool check_diagonal (char &winner) {

  // Main diagonal
  winner = '.';
  bool completed = true;
  for (int i = 0; i < 4; ++i) {
    if (M[i][i] == 'T')
      continue;
    if (M[i][i] == '.') {
      completed = false;
      break;
    }
    else {
      if (winner == '.')
	winner = M[i][i];
      else
	if (winner != M[i][i]) {
	  completed = false;
	  break;
	}
    }
  }

  if (completed) 
    return true;

  // The other diagonal

  winner = '.';
  completed = true;
  for (int i = 0; i < 4; ++i) {
    if (M[i][3-i] == 'T')
      continue;
    if (M[i][3-i] == '.') {
      completed = false;
      break;
    }
    else {
      if (winner == '.')
	winner = M[i][3-i];
      else
	if (winner != M[i][3-i]) {
	  completed = false;
	  break;
	}
    }
  }

  if (completed)
    return true;
  return false;
}

bool check_tie (void) {
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
      if (M[i][j] == '.')
	return false;
  return true;
}

int main () {

  int nc;
  scanf ("%d", &nc);
  
  for (int i = 1; i <= nc; ++i) {
    for (int j = 0; j < 4; ++j) {
      scanf ("%s", M[j]);
    }
    
    char won;
    if (check_horizontal (won))
      printf ("Case #%d: %c won\n", i, won);
    else if (check_vertical (won))
      printf ("Case #%d: %c won\n", i, won);
    else if (check_diagonal (won))
      printf ("Case #%d: %c won\n", i, won);
    else if (check_tie ())
      printf ("Case #%d: Draw\n", i);
    else
      printf ("Case #%d: Game has not completed\n", i);
  }

  return 0;
}
