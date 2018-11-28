#include <iostream>
#include <vector>

using namespace std;

class cell{
  public:
    int altitude;
    char basin;
    vector<cell*> parents;
    void addparent(cell* p);
    void assignbasin(char b);
};

void cell::addparent(cell *p){
  parents.push_back(p);
}

void cell::assignbasin(char b){
  basin = b;
  vector<cell*>::iterator p = parents.begin();
  while(p!=parents.end()){
    (*p)->assignbasin(b);
    p++;
  }
}

int main(){
  int T, H, W;
  cin >> T;
  for(int i=0;i<T;i++){
    cin >> H >> W;
    vector<cell*> sinks;
    cell** table = new cell*[H];
    // read in cell altitudes
    for(int r=0; r<H; r++){
      table[r] = new cell[W];
      for(int c=0; c<W; c++){
	cin >> table[r][c].altitude;
      }
    }
    // process water flow
    for(int r=0; r<H; r++)
      for(int c=0; c<W; c++){
	// find min in n,w,e,s order
	int min = 999999, x,y;
	if(r>0 && table[r-1][c].altitude<min){
	  min=table[r-1][c].altitude;
	  x=r-1;
	  y=c;
	}
	if(c>0 && table[r][c-1].altitude<min){
	  min=table[r][c-1].altitude;
	  x=r;
	  y=c-1;
	} 
	if(c<(W-1) && table[r][c+1].altitude<min){
	  min=table[r][c+1].altitude;
	  x=r;
	  y=c+1;
	}
	if(r<(H-1) && table[r+1][c].altitude<min){
	  min=table[r+1][c].altitude;
	  x=r+1;
	  y=c;
	}
	// if it's a sink, add to sinks
	if(min>=table[r][c].altitude){
	  cell* sink = &table[r][c];
	  sinks.push_back(sink);
	}
	// else add parent node* from min to this one
	else{
	  cell* me = &table[r][c];
	  table[x][y].addparent(me);
	}
      }
    // assign initial basin nos (0-25)
    char basin = 0;
    vector<cell*>::iterator s = sinks.begin();
    while(s!=sinks.end()){
      (*s)->assignbasin(basin);
      basin++;
      s++;
    }
    // assign correct basin letters (a-z)
    char basinletters[26] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    basin = 'a';
    for(int r=0; r<H; r++){
      for(int c=0; c<W; c++){
	if(basinletters[table[r][c].basin]==-1){
	  basinletters[table[r][c].basin] = basin;
	  table[r][c].basin = basin;
	  basin++;
	}
	else table[r][c].basin = basinletters[table[r][c].basin];
      }
    }
    cout << "Case #" << i+1 << ":" << endl;
    for(int r=0; r<H; r++){
      for(int c=0; c<W; c++){
	cout << table[r][c].basin;
	if(c<(W-1)) cout << " ";
      }
      cout << endl;
    }
  } 
  return 0;
}

