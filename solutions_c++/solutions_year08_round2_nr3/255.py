#include <fstream>
#include <string>
#include <sstream>
#include <vector>


typedef unsigned long uint32;


void calcPerfectDeck(uint32 k, std::vector<uint32> &cards) {
  uint32 pos = 0;
  
  std::vector<uint32> poss;
  poss.resize(k, 0);
  for (uint32 i = 0; i < k; ++i) {
    poss[i] = i;
  }

  cards.resize(k, 0);

  for (uint32 i = 0; i < k; ++i) {
    pos = (pos + i) % poss.size();
    cards[poss[pos]] = i + 1;
    poss.erase(poss.begin() + pos);
  }
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
    uint32 k = 0;
    if (!getline(infile, line)) {
      exit(1);
    }

    {
      std::stringstream ss(line);
      ss >> k;
      if (!ss) exit(1);
    }

    if (!getline(infile, line)) {
      exit(1);
    }

    uint32 indices = 0;
    std::stringstream ss(line);
    ss >> indices;
    if (!ss) exit(1);
    
    std::vector<uint32> cards;
    calcPerfectDeck(k, cards);

    outfile << "Case #" << (i + 1) << ":";
    for (uint32 ind = 0; ind < indices; ++ind) {
      uint32 index = 0;
      ss >> index;
      if (!ss) exit(1);
      outfile << " " << cards[index - 1];
    }
    outfile << std::endl;
  }
  
  infile.close();
  outfile.close();

  return 0;
}
