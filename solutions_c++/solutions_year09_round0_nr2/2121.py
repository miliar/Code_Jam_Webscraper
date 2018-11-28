#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct cell
{
  bool is_sink;
  short alt;
  vector<cell*> incoming;
  cell* outgoing;
  char letter;
  
  cell()
  {
    is_sink = false;
    outgoing = 0;
    letter = '\0';
  }
};

void print_grid(vector< vector<cell> > & grid, int w, int h)
{
  for (int y=0; y < h; y++)
  {
    int x;
    for (x=0; x < w-1; x++)
    {
      cout << grid[x][y].letter << " ";
    }
    cout << grid[x][y].letter << " ";
    cout << endl;
  }
}


void print_grid_n(vector< vector<cell> > & grid, int w, int h)
{
  for (int y=0; y < h; y++)
  {
    int x;
    for (x=0; x < w-1; x++)
    {
          cout << grid[x][y].alt << " ";
    }
    cout << grid[x][y].alt << " ";
    cout << endl;
  }
}

cell *find_sink(cell* me, vector<cell*> & ontheway)
{
  if (me->is_sink)
  {
    // gcc bug, with -O3 it optimizes something it shouldn't making this fail
    // if we don't access "me" in a user-visible way
    // nope, was my bug (not returning below)
    //cerr << "found sink with value " << me << endl;
    return me;
  }
  
  
  ontheway.push_back(me->outgoing);
  
  return find_sink(me->outgoing, ontheway);
}

cell *lowest_neighbor(vector< vector<cell> > & grid, int x, int y, int w, int h)
{
//  cerr << "Lowest for " << x << " " << y << "(value: " << grid[x][y].alt << ")" << endl;
  
  int U,L,R,D;
  int m = grid[x][y].alt;
  
  if (y <= 0)     { U = 999999; } else { U = grid[x][y-1].alt; }
  if (x <= 0)     { L = 999999; } else { L = grid[x-1][y].alt; }
  if (x >= (w-1)) { R = 999999; } else { R = grid[x+1][y].alt; }
  if (y >= (h-1)) { D = 999999; } else { D = grid[x][y+1].alt; }

  if ( U >= m && L >= m && R >= m && D >= m )
  {
//    cerr << "Return 0" << endl;
    return 0;
  }
  
  if ( U <= L && U <= R && U <= D )
  {
//    cerr << "Return U" << endl;
    return (&(grid[x][y-1]));
  }

  if ( L <= R && L <= D )
  {
//    cerr << "Return L" << endl;
    return (&(grid[x-1][y]));
  }
  
  if ( R <= D )
  {
//    cerr << "Return R" << endl;
    return (&(grid[x+1][y]));
  }

//  cerr << "Return D" << endl;
  return (&(grid[x][y+1]));

}

void run_task(int casenum, int w, int h, vector< vector<cell> > & grid)
{
  vector<cell*> sinks;
  
  char cur_letter = 'a';
  
  for (int y=0; y<h;y++)
  {
    for (int x=0;x<w;x++)
    {
      cell *low = lowest_neighbor(grid, x, y, w, h);
      
      if (low == 0)
      {
        grid[x][y].outgoing = 0;
        grid[x][y].is_sink = true;
        sinks.push_back(&(grid[x][y]));
      }
      else
      {
        grid[x][y].outgoing = low;
        (*low).incoming.push_back(&(grid[x][y]));
        grid[x][y].is_sink = false;
      }
    }
  }
  
  for (int y=0; y < h; y++)
  {
    for (int x=0; x < w; x++)
    {
      if (grid[x][y].letter != '\0') { /*cerr << "continue " << endl;*/continue; /* already assigned */ }
      
      vector<cell*> ontheway;
      cell* mysink = find_sink(&(grid[x][y]), ontheway);
      
//      cerr << "got sink " << mysink <<  endl;
      if (mysink->letter == '\0')
      {
        // assign letter
        mysink->letter = cur_letter;
        cur_letter++;
      }
      
      grid[x][y].letter = mysink->letter;
      
      for (unsigned int j=0; j < ontheway.size(); j++)
      {
        ontheway[j]->letter = mysink->letter;
      }
    }
  }
  
  cout << "Case #" << casenum << ":" << endl;
  print_grid(grid, w, h);
}

int main()
{
  int num_maps;
  cin >> num_maps;
  
  for (int i=0; i < num_maps; i++)
  {
    int w,h;
    
    cin >> h >> w;
    
    vector< vector <cell> > grid(w, vector<cell>(h));
    
    for (int y = 0; y < h; y++)
    {
      for (int x = 0; x < w; x++)
      {
        cin >> grid[x][y].alt;
      }
    }
    
    //print_grid_n(grid,w,h);
    run_task(i+1, w, h, grid);
  }
}
