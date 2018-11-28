#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>

typedef unsigned long uint32;


class CentralSystem {
  private :
    std::vector<std::string> searchEngines;
    std::vector<std::string> queries;

  public :
    void readSearchEngines(std::istream &is);
    void readQueries(std::istream &is);
    uint32 getNumSwitches();
};

void CentralSystem::readSearchEngines(std::istream &is) {
  std::string line;
  if (!getline(is, line)) {
    exit(1);
  }
  uint32 s = 0;
  {
    std::stringstream ss(line);
    ss >> s;
    if (!ss) exit(1);
  }
  for (int i = 0; i < s; ++i) {
    if (!getline(is, line)) {
      exit(1);
    }
    searchEngines.push_back(line);
  }
}

void CentralSystem::readQueries(std::istream &is) {
  std::string line;
  if (!getline(is, line)) {
    exit(1);
  }
  uint32 q = 0;
  {
    std::stringstream ss(line);
    ss >> q;
    if (!ss) exit(1);
  }
  for (int i = 0; i < q; ++i) {
    if (!getline(is, line)) {
      exit(1);
    }
    queries.push_back(line);
  }
}

uint32 CentralSystem::getNumSwitches() {
  uint32 switches = 0;
  std::set<std::string> run;
  
  std::vector<std::string>::iterator query_it = queries.begin();

  while (query_it != queries.end()) {
    run.insert(*query_it);
    while ((run.size() < searchEngines.size()) && (query_it != queries.end())) {
      ++query_it;
      if (query_it != queries.end()) run.insert(*query_it);
    }
    if (query_it != queries.end()) {
      ++switches;
      run.clear();
    }
  }
  
  return switches;
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
    CentralSystem cs;
    cs.readSearchEngines(infile);
    cs.readQueries(infile);
    outfile << "Case #" << (i + 1) << ": " << cs.getNumSwitches() << std::endl;
  }
  
  infile.close();
  outfile.close();

  return 0;
}
