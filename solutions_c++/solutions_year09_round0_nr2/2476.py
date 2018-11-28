#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

bool next(int a, int b, int matrix[100][100], int & i, int & j, int H, int W) {
  int north, west, east, south;
  int anorth, awest, aeast, asouth;
  int myself=matrix[a][b];
  north=a-1; if(north<0) {north=0; anorth=10999;} else anorth=matrix[north][b]; 
  west=b-1; if(west<0) {west=0; awest=10999;} else awest=matrix[a][west];
  east=b+1; if(east==W) {east=W-1; aeast=10999;} else aeast=matrix[a][east];
  south=a+1; if(south==H) {south=H-1; asouth=10999;} else asouth=matrix[south][b];
  //  cout << "east " << east << " " << a << endl;
  //  cout << myself << " " << anorth << " " << awest << " " << aeast << " " << asouth << endl;
  if(myself<=anorth && myself<=awest && myself<=aeast && myself<=asouth) {
    i=a; j=b;
    return true; // if can not move any longer, true;
  }
  int min=anorth; i=north; j=b;
  if(min>awest) {min=awest; i=a; j=west;}
  if(min>aeast) {min=aeast; i=a; j=east;}
  if(min>asouth) {min=asouth; i=south; j=b;}
  return false;
}


int main(int argc, char** argv) {
  if(argc!=2) {
    cout << "Usage: " << argv[0] << " DATAFILE" << endl;
    exit(1);
  }
  
  ifstream infile(argv[1]);
  if(!infile.good()) {
    cout << "Error: could not open " << argv[1] << endl;
    exit(2);
  }
  
  int T;
  int H;
  int W; // total cases
  int atitude[100][100];
  char aChar[100][100];
  char basin[27]="abcdefghijklmnopqrstuvwxyz";
  int index=0;
  string aForward, aBackward;
  infile >> T;
  //  cout << T << endl;
  for(int iT=0; iT<T; iT++){
    for(int i=0; i<100; i++)for(int j=0; j<100; j++) aChar[i][j]='0';
    infile >> H >> W;
    index=1;
    //    cout << H << " " << W << endl;
    for(int iH=0; iH<H; iH++) {
      for(int iW=0; iW<W; iW++) infile >> atitude[iH][iW]; 
    }
    cout << "Case #" << iT+1 << ": " << endl;
    aChar[0][0]='a';
    int i1=0;
    int j1=0;
    int i=0;
    int j=0;
    bool end;
    do {
      char aC=aChar[i1][j1];
      //      cout << i1 << " " << j1 << endl;
      end=next(i1, j1, atitude, i, j, H, W);
      i1=i;
      j1=j;
      aChar[i][j]=aC; // now i, j is the next 0f i1, j1
      //      cout << i << " " << j << endl;
      //      cout << endl;
    } while(!end);
    
    for(int i1=0; i1<H; i1++){  
      for(int j1=0; j1<W; j1++) {
	if(j1==0 && i1==0) continue;
	vector<int> vi;
	vector<int> vj;
	vi.push_back(i1);
	vj.push_back(j1);
	bool end;
	int i2=i1;
	int j2=j1;
	do {
	  end=next(i2, j2, atitude, i, j, H, W);
	  i2=i;
	  j2=j;
	  vi.push_back(i2);
	  vj.push_back(j2);
	} while(!end);
	if(aChar[i][j]!='0') {
	  for(int aa=0; aa<vi.size(); aa++) aChar[vi.at(aa)][vj.at(aa)]=aChar[i][j];
	} else {
	  for(int aa=0; aa<vi.size(); aa++) aChar[vi.at(aa)][vj.at(aa)]=basin[index];
	  //	  cout << "yingj " << index << endl;
	  index++;
	}
      }
    }

    for(int iH=0; iH<H; iH++) {
      for(int iW=0; iW<W; iW++) cout << aChar[iH][iW] << " ";
      cout << endl;
    }
  }
  
  return 0;
}
