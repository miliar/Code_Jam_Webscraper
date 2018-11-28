#include <cstdio>
#include <string>
#include <set>
#include <iostream>

const std::string
read_line(FILE* fp) {
  char line[512] = {0};

  fgets(line, 512, fp);
  if (line[strlen(line) - 1] == '\n')
    line[strlen(line) - 1] = '\0';
  return line;
}

int
read_int(FILE* fp) {
  return atoi(read_line(fp).c_str());
}

int
main(int argc, char** argv) {
  int cases;
  FILE* fp = fopen(argv[1], "r");

  cases = read_int(fp);
  for (int i = 1; i <= cases; ++i) {
    int S;
    std::set<std::string> engines;

    S = read_int(fp);
    while (S--) {
      std::string engine;
      engine = read_line(fp);
      engines.insert(engine);
    }

    int Q;
    int n = 0;
    std::set<std::string> queries;

    Q = read_int(fp);
    while (Q--) {
      std::string query;

      query = read_line(fp);
      queries.insert(query);

      if (engines == queries) {
        ++n;
        queries.clear();
        queries.insert(query);
      }
    }

    printf("Case #%d: %d\n", i, n);
  }
  fclose(fp);
  return 0;
}
