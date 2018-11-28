#include <iostream>
#include <map>
#include <climits>

class MFSet {
  int * elems;
public:
  MFSet (int comps);
  ~MFSet ();
  int find (int elem);
  void merge (int elem1, int elem2);
  inline int rank (int elem) {
    return -elems[find (elem)];
  }
  inline bool same (int elem1, int elem2) {
    return find(elem1) == find(elem2);
  }
  inline void reset (int n) {
    for (int i = 0; i < n; i++)
      elems[i] = -1;
  }
};

MFSet::MFSet (int comps) {
  elems = new int [comps];
  reset(comps);
}

MFSet::~MFSet () {
  delete [] elems;
  elems = NULL;
}

int MFSet::find (int elem) {
  if (elems[elem] >= 0) {
    elems[elem] = find(elems[elem]);
    return elems[elem];
  } else {
    return elem;
  }
}

void MFSet::merge (int elem1, int elem2) {
  elem1 = find (elem1);
  elem2 = find (elem2);
  if (rank(elem1) > rank(elem2)) {
    elems[elem2] = elem1;
  } else if (rank(elem1) < rank(elem2)) {
    elems[elem1] = elem2;
  } else if (elem1 != elem2) {
    elems[elem1] = elem2;
    elems[elem2]--;
  }
}

using namespace std;

/*int main() {
  int mflen;
  cin >> mflen;
  MFSet mf(mflen);
  string op;
  int a1, a2;
  while (true) {
    cin >> op;
    if (op == "M") {
      cin >> a1 >> a2;
      mf.merge(a1,a2);
    } else if (op == "F") {
      cin >> a1;
      cout << mf.find(a1) << endl;
    } else if (op == "R") {
      cin >> a1;
      cout << mf.rank(a1) << endl;
    } else if (op == "S") {
      cin >> a1 >> a2;
      cout << mf.same(a1,a2) << endl;
    } else {
      cerr << "WTF!\n";
    }
  }R 1
}*/

class MatrixConverter {
  int cols;
public:
  inline MatrixConverter (int c) : cols(c) { }
  inline int operator () (int a, int b) {
    return a * cols + b;
  }
  inline int row (int a) {
    return a / cols;
  }
  inline int col (int a) {
    return a % cols;
  }
};

const int hmax = 100;
const int wmax = 100;

int main () {
  int T, h, w;
  short alts[hmax][wmax];
  char names[hmax][wmax];
  const char pnames[] = "abcdefghijklmnopqrstuvwxyz";
  MFSet mf(hmax*wmax);
  cin >> T;
  for (int c = 1; c <= T; c++) {
    cin >> h >> w;
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	cin >> alts[i][j];
	names[i][j]='\0';
      }
    }
    MatrixConverter mc(w);
    mf.reset(h*w);
    //Now we get the basin of each cell
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	  int xmin = j, ymin = i;
	  short zmin = alts[i][j];
	  //NORTH
	  if (i - 1 >= 0 && alts[i-1][j] < zmin) {
	    zmin = alts[i-1][j];
	    xmin =j;
	    ymin = i-1;
	  }
	  //WEST
	  if (j - 1 >= 0 && alts[i][j-1] < zmin) {
	    zmin = alts[i][j-1];
	    xmin = j-1;
	    ymin = i;
	  }
	  //EAST
	  if (j + 1 < w && alts[i][j+1] < zmin) {
	    zmin = alts[i][j+1];
	    xmin = j+1;
	    ymin = i;
	  }
	  //SOUTH
	  if (i + 1 < h && alts[i+1][j] < zmin) {
	    zmin = alts[i+1][j];
	    xmin = j;
	    ymin = i+1;
	  }
	  mf.merge(mc(ymin,xmin),mc(i,j));
      }
    }
    int curcar = 0;
    //Now we get the basin of each cell
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
	int rep = mf.find(mc(i,j));
	int rx = mc.col(rep);
	int ry = mc.row(rep);
	if (names[ry][rx] == '\0') {
	  names[ry][rx] = pnames[curcar++];
	}
	names[i][j] = names[ry][rx];
      }
    }
    //Et voila, let's print it
    cout << "Case #"<< c <<":\n";
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w -1; j++) {
	cout << names[i][j] << ' ';
      }
      if ( w -1 >= 0)
	cout << names[i][w-1];
      cout << endl;
    }
  }
  return 0;
}