#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>

#define	EMPTY	((char)('a' - 2))
#define VISITED	((char)('a' - 1))

using namespace std;

int main () 
{

  ifstream fin("B-large.in");
  ofstream fout("Sink.out");

  int cantTest;
  fin >> cantTest;

  for (int c = 0; c < cantTest; c++)
  {
    vector< pair<int,int> > camino;
    int map[100][100];
    char out[100][100];
    int h, w;
    char curletter = 'a' - 1;
    //char nextletter = 'a';
    
    fin >> h >> w;
    for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

      fin >> map[i][j];
      out[i][j] = EMPTY;

    }
    }

    for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

      cout << map[i][j] << ' ';
      

    }
      cout << endl;
    }
/*
    for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

	int curMin = map[i][j];

	if ((i > 0) && (map[i-1][j] < curMin)) { cout << map[i-1][j] << endl; continue; }
	if ((j > 0) && (map[i][j-1] < curMin)) { cout << map[i][j-1] << endl; continue; }
	if ((j < w-1) && (map[i][j+1] < curMin)) { cout << map[i][j+1] << endl; continue; }
	if ((i < h-1) && (map[i+1][j] < curMin)) { cout << map[i+1][j] << endl; continue; }

	out[i][j] = nextletter;
	nextletter++;

      }
    }
*/
    /*for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

      cout << (char)(out[i][j]) << ' ';
      

    }
      cout << endl;
    }*/

    for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

	if (out[i][j] == EMPTY) {

	  cout << ">>>" << map[i][j] << endl;
      
	  camino.clear();

	  int fx = i, fy = j;
	  while (out[fx][fy] == EMPTY) {

	    cout << ">" << map[fx][fy] << endl;

	    int curMin = map[fx][fy];
	    int nx = fx, ny = fy;
	    
	    if ((fx > 0) && (map[fx-1][fy] < curMin)) { curMin =  map[fx-1][fy]; ny = fy; nx = fx-1; }
	    if ((fy > 0) && (map[fx][fy-1] < curMin)) { curMin =  map[fx][fy-1]; nx = fx; ny = fy-1; }
	    if ((fy < w-1) && (map[fx][fy+1] < curMin)) { curMin =  map[fx][fy+1]; nx = fx; ny = fy+1; }
	    if ((fx < h-1) && (map[fx+1][fy] < curMin)) { curMin =  map[fx+1][fy]; ny = fy; nx = fx+1; }

	    cout << nx << ' ' << ny << endl;

	    if ((nx == fx) && (ny == fy)) {
      
	      curletter++;
	      out[fx][fy] = curletter;
	      cout << "letra: " <<out[fx][fy] << endl;

	    } else {

	      out[fx][fy] = VISITED;
	      
	      camino.push_back( make_pair(fx, fy) );
  
	      fx = nx;
	      fy = ny;

	    

	    }
	  }

	  char foundletter = out[fx][fy];

	  vector< pair<int,int> >::const_reverse_iterator iter;
	  for (iter = camino.rbegin(); iter != camino.rend(); iter++)
	  {

	      out[ (*iter).first ][ (*iter).second ] = foundletter;

	      cout << (*iter).first << ' ' << (*iter).second << ' ';

	  }
	  cout << endl;


	  //bool notFinished = true;
	  //while (notFinished)
	  //{

	    //int nx = fx; ny = fy;

	    //if ((fx > 0) && (out[fx-1][fy] == VISITED)) { curMin =  map[fx-1][fy]; nx = fx-1; }
	    //if ((fy > 0) && (out[fx][fy-1] == VISITED)) { curMin =  map[fx][fy-1]; ny = fy-1; }
	    //if ((fy < w-1) && (out[fx][fy+1] == VISITED)) { curMin =  map[fx][fy+1]; ny = fy+1; }
	    //if ((fx < h-1) && (out[fx+1][fy] == VISITED)) { curMin =  map[fx+1][fy]; nx = fx+1; }
	  //}

	}
    }
    }	

    fout << "Case #" << c+1 << ":" << endl;

    for (int i = 0; i < h; i++) {
      for (int j =  0; j < w; j++) {

      cout << out[i][j] << ' ';
      fout << out[i][j] << ' ';
      

    }
      cout << endl;
      fout << endl;
    }    
    

  }

  fin.close();

  fout.close();

}