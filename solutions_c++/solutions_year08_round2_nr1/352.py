#include <fstream>
#include <string>
#include <sstream>
#include <vector>


typedef unsigned long uint32;
typedef unsigned long long uint64;



typedef struct Tree {
  uint64 x;
  uint64 y;
  Tree(uint64 xx, uint64 yy) : x(xx), y(yy) { }
} Tree;

uint64 calculateTriangles(std::vector<Tree> &trees) {
  uint64 cnt = 0;
  std::vector<Tree>::const_iterator firstTree;
  std::vector<Tree>::const_iterator secondTree;
  std::vector<Tree>::const_iterator thirdTree;
  for (firstTree = trees.begin(); firstTree != trees.end() - 2; ++firstTree) {
    for (secondTree = firstTree + 1; secondTree != trees.end() - 1; ++ secondTree) {
      for (thirdTree = secondTree + 1; thirdTree != trees.end(); ++ thirdTree) {
        if (!(((*firstTree).x + (*secondTree).x + (*thirdTree).x) % 3) && !(((*firstTree).y + (*secondTree).y + (*thirdTree).y) % 3)) {
          ++cnt;
        }
      }
    }
  }
  return cnt;
}


int main(int argc, char *argv[]) {
  if (argc < 3) exit(1);

  std::ifstream infile(argv[1]);
  std::ofstream outfile(argv[2]);
  
  std::string line;
  if (!getline(infile, line)) {
    exit(1);
  }
  uint32 n = 0;
  {
    std::stringstream ss(line);
    ss >> n;
    if (!ss) exit(1);
  }
  for (int i = 0; i < n; ++i) {
    uint32 no_trees = 0;
    uint64 a = 0, b = 0, c = 0, d = 0;
    uint64 x0 = 0, y0 = 0;
    uint64 m = 0;

    if (!getline(infile, line)) {
      exit(1);
    }
    std::stringstream ss(line);
    ss >> no_trees >> a >> b >> c >> d >> x0 >> y0 >> m;
    if (!ss) exit(1);

    std::vector<Tree> trees;
    uint64 x = x0, y = y0;
    trees.push_back(Tree(x, y));
    for (uint32 no = 1; no < no_trees; ++no) {
      x = (a * x + b) % m;
      y = (c * y + d) % m;
      trees.push_back(Tree(x, y));
    }

    outfile << "Case #" << (i + 1) << ": " << calculateTriangles(trees) << std::endl;
  }
  
  infile.close();
  outfile.close();

  return 0;
}
