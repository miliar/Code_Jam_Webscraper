#include <iostream>
#include <map>
#include <set>

size_t calc()
{
  size_t result = 0;
  std::string dummy;
  std::map<std::string, size_t> engines;
  size_t n_engines, n_queries;
  std::cin >> n_engines;
  std::getline(std::cin, dummy);
  for (size_t i = 0; i < n_engines; i++) {
    std::string engine_name;
    std::getline(std::cin, engine_name);
    engines[engine_name] = i;
  }
  std::cin >> n_queries;
  std::getline(std::cin, dummy);
  std::set<size_t> excluded;
  size_t n_excluded = 0; // Redundant, kept for speed
  for (size_t i = 0; i < n_queries; i++) {
    std::string query;
    std::getline(std::cin, query);
    std::map<std::string, size_t>::const_iterator it
      = engines.find(query);
    if (it == engines.end())
      abort();
    n_excluded += excluded.insert(it->second).second;
    if (n_excluded == n_engines) {
      result++;
      excluded.clear();
      excluded.insert(it->second);
      n_excluded = 1;
    }
  }
  return result;
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": " << calc() << std::endl;
  }
}
