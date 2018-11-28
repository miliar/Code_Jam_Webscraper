#include <iostream>
#include <string>

using namespace std;

enum Etat {EN_COURS, NUL, X, O};

Etat verifLigne (const string ligne, size_t indice)
{
  char check = ligne[indice * 4];

  for (int i = 1; i < 4; ++i) {
    if (check == '.') {
      return EN_COURS;
    }
    else if (check == 'T') {
      check = ligne[indice * 4 + i];
    }
    else if (check != ligne[indice * 4 + i] && ligne[indice * 4 + i] != 'T'){
      return EN_COURS;
    }
    
  }

  if (check == 'O') {
    return O;
  } else {
    return X;
  }
  
}

Etat verifColonne (const string ligne, size_t indice)
{
  char check = ligne[indice];

  for (int i = 1; i < 4; ++i) {
    if (check == '.') {
      return EN_COURS;
    } 
    else if (check == 'T') {
      check = ligne[i * 4 + indice];
    }
    else if (check != ligne[i * 4 + indice] && ligne[i * 4 + indice] != 'T'){
      return EN_COURS;
    }
  }

  if (check == 'O') {
    return O;
  } else {
    return X;
  }
}

Etat verifDiagonale (const string ligne)
{
  char check = ligne[0];

  for (int i = 1; i < 4; ++i) {
    if (check == '.') {
      break;
    } 
    else if (check == 'T') {
      check = ligne[i * 4 + i];
    }
    else {
      if (check != ligne[i * 4 + i] && ligne[i * 4 + i] != 'T'){
	check = '.';
	break;
      }
    }
  }

  if (check == 'O') {
    return O;
  }
  else if (check == 'X') {
    return X;
  }

  check = ligne[3];

  for (int i = 1; i < 4; ++i) {
    if (check == '.') {
      return EN_COURS;
    } 
    else if (check == 'T') {
      check = ligne[(i + 1) * 3];
    }
    else {
      if (check != ligne[(i + 1) * 3] && ligne[(i + 1) * 3] != 'T'){
	return EN_COURS;
      }
    }
  }

  if (check == 'O') {
    return O;
  } else {
    return X;
  }
}

Etat partieFinie (string ligne)
{
  if (ligne.find('.') != ligne.npos) {
    return EN_COURS;
  } else {
    return NUL;
  }
}

Etat determinerEtat (const string ligne)
{
  for (int i = 0; i < 4; ++i){
    Etat temp = verifLigne(ligne, i);

    if (temp != EN_COURS) {
      return temp;
    }
  }

  for (int i = 0; i < 4; ++i){
    Etat temp = verifColonne(ligne, i);

    if (temp != EN_COURS) {
      return temp;
    }
  }

  Etat temp = verifDiagonale(ligne);

  if (temp != EN_COURS) {
    return temp;
  }

  return partieFinie(ligne);
}

int main (int argc, char** argv)
{
  int nbTests;

  cin >> nbTests;

  for(int i = 0; i < nbTests; i++){
    string ligne;

    for (int i = 0; i < 4; ++i) {
      string temp;
      cin >> temp;
      ligne += temp;
    }

    Etat etat = determinerEtat(ligne);

    cout << "Case #" << i + 1 << ": ";
    switch (etat) {
    case NUL :
      cout << "Draw";
      break;
    case X :
      cout << "X won";
      break;
    case O :
      cout << "O won";
      break;
    case EN_COURS :
      cout << "Game has not completed";
      break;
    default :
      break;
    }
    cout << endl;
  }

  return 0;
}
