#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

const size_t NONE = size_t(-1);

struct customer_t {
  customer_t(): malted(NONE) {}
  // The set of flavors that this customer likes
  std::vector<size_t> unmalted;
  size_t malted;
};

void calc()
{
  // Number of flavors
  size_t n;
  std::cin >> n;
  // Number of customers
  size_t m;
  std::cin >> m;

  // Customer list
  std::vector<customer_t> customers(m);
  // Mapping from unmalted flavor to customers liking this variant
  std::multimap<size_t, size_t> reverse_map;

  std::set<size_t> work_queue;
  for (size_t i = 0; i < m; i++) {
    size_t num_favorites;
    std::cin >> num_favorites;
    for (size_t j = 0; j < num_favorites; j++) {
      size_t flavor;
      std::cin >> flavor;
      int is_malted;
      std::cin >> is_malted;
      if (is_malted)
        customers[i].malted = flavor - 1;
      else {
        customers[i].unmalted.push_back(flavor - 1);
        reverse_map.insert(std::make_pair(flavor - 1, i));
      }
    }
    work_queue.insert(i);
  }
  // Whether to produce each flavor malted, initially all false, set
  // each entry to true if forced to, and find out if solution
  // possible
  std::vector<bool> produce_malted(n, false);
  while (!work_queue.empty()) {
    size_t customer = *work_queue.begin();
    work_queue.erase(work_queue.begin());
    // See if this customer is satisfied
    if (customers[customer].malted != NONE
        && produce_malted[customers[customer].malted]) {
      // She gets her malted favorite
      continue;
    }
    bool satisfied = false;
    for (std::vector<size_t>::const_iterator
           it = customers[customer].unmalted.begin();
         it != customers[customer].unmalted.end(); ++it) {
      if (!produce_malted[*it]) {
        // She gets one of her unmalted favorites
        satisfied = true;
        break;
      }
    }
    if (satisfied)
      continue;
    // This customer did not get any of her favorite flavors, we have
    // to make her malted favorite
    if (customers[customer].malted == NONE) {
      std::cout << " IMPOSSIBLE" << std::endl;
      return;
    }
    produce_malted[customers[customer].malted] = true;
    // Now we have to re-inspect any customers who liked the
    // non-malted variant of this flavor to see if they are still
    // satisfied
    std::pair<std::map<size_t, size_t>::const_iterator,
      std::map<size_t, size_t>::const_iterator> range
      = reverse_map.equal_range(customers[customer].malted);
    for (std::map<size_t, size_t>::const_iterator it = range.first;
         it != range.second; ++it)
      work_queue.insert(it->second);
  }
  // Output which flavors needs to be malted
  for (size_t i = 0; i < n; i++)
    std::cout << " " << (produce_malted[i] ? "1" : "0");
  std::cout << std::endl;
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ":";
    calc();
  }
}
