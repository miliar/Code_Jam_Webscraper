#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

class watersheds {
  public:
    watersheds(int input);
    void readInput();
    void solve();
      void mountAdjList();
      void findTrees();
      void mountOutput();
      void mountFlowMap(); 
      void recursiveFind(int actualElement);
    
 
    int map[200][200];
    int flowMap[200][200];
    int mapNumber[200][200];
    char drainageBasins [200][200];
    char actualDrainageBasin;
    vector <int> adjacentVertices[20000];
    int found[20000];
    int actualCase;
    int sizeL, sizeC;  
  
  
};
void watersheds::mountFlowMap() {
  int lowest;
  for (int line = 1; line <= sizeL; line++) {
    for (int column = 1; column <= sizeC; column++) {
      flowMap[line][column] = mapNumber[line][column];
      lowest = map[line][column];
      //north A
      if (map[line-1][column] < lowest) {
        lowest = map[line-1][column];
        flowMap[line][column] = mapNumber[line-1][column];        
      }
      //west <-
      if (map[line][column-1] < lowest) {
        lowest = map[line][column-1];
        flowMap[line][column] = mapNumber[line][column-1];        
      }
      //east ->
      if (map[line][column+1] < lowest) {
        lowest = map[line][column+1];
        flowMap[line][column] = mapNumber[line][column+1];        
      }
      //south V
      if (map[line+1][column] < lowest) {
        lowest = map[line+1][column];
        flowMap[line][column] = mapNumber[line+1][column];        
      }
    }
  }
}


void watersheds::mountAdjList(){
  for (int line = 1; line <= sizeL; line++) {
    for (int column = 1; column <= sizeC; column++) {
      adjacentVertices[mapNumber[line][column]].push_back(flowMap[line][column]);
      adjacentVertices[flowMap[line][column]].push_back(mapNumber[line][column]);
    }
  }
  
}
void watersheds::findTrees(){
  actualDrainageBasin = 'a';
  for (int c = 0; c < sizeL*sizeC; c++) {
    found[c] = 0;    
  }
  for (int c = 0; c < sizeL*sizeC; c++) {
    if (found[c] == 0) {
      recursiveFind(c);
      actualDrainageBasin++;
    }
  }  
}
void watersheds::recursiveFind(int actualElement) {
  found[actualElement] = 1;
  drainageBasins[actualElement/sizeC]
                [actualElement - ((actualElement/sizeC)*sizeC)] 
                = actualDrainageBasin;
  int toFind;
  for (int c = 0; c < adjacentVertices[actualElement].size(); c++) {
    toFind = adjacentVertices[actualElement][c];
    if (found[toFind] == 0) {
      recursiveFind(toFind);
    }
  }
}



void watersheds::mountOutput(){
  printf("Case #%d:\n",actualCase);
  for (int l = 0; l < sizeL; l++) {
    for (int c = 0; c < sizeC; c++) {
      printf("%c ", drainageBasins[l][c]);
      
    }
    printf("\n");
  }
  
}

watersheds::watersheds(int input) {
  actualCase = input;
}

void watersheds::readInput() {
  scanf("%d %d", &sizeL, &sizeC);
  int actualNumber;
  int actualIndex = 0;
  for (int c = 0; c <= sizeL +1; c++) {
    map[c][0] = 12345;
    map[c][sizeC + 1] = 12345;
  }
  for (int c = 0; c <= sizeC +1; c++) {
    map[0][c] = 12345;
    map[sizeL + 1][c] = 12345;
  }
  for (int c1 = 1; c1 <= sizeL; c1++) {
    for (int c2 = 1; c2 <= sizeC; c2++) {
      scanf("%d",&actualNumber);
      map[c1][c2] =actualNumber;
      mapNumber[c1][c2] = actualIndex;
      actualIndex++;
    }
  }  
}

void watersheds::solve() {
  mountFlowMap();
  mountAdjList();
  findTrees();
  mountOutput();
}

int main() {
  int numOfCases;
  scanf("%d",&numOfCases);
  for (int actualCase = 1; actualCase <= numOfCases; actualCase++ ) {
    watersheds *watershed = new watersheds(actualCase);
    watershed->readInput();
    watershed->solve();
    delete watershed;
  }
  
}
