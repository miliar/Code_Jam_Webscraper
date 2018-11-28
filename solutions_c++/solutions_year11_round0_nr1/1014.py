#include <iostream>
#include <vector>

enum Color {
  BLUE,
  ORANGE
};

struct Order {
  Color color;
  int pos;
};

int solve(const std::vector<Order> &orders) {
  int step = 0;
  std::size_t next_blue = 0, next_orange = 0;
  int blue_pos = 1, orange_pos = 1;
  while ((next_blue < orders.size()) && (orders[next_blue].color != BLUE)) {
    ++next_blue;
  }
  while ((next_orange < orders.size()) && (orders[next_orange].color != ORANGE)) {
    ++next_orange;
  }

  while ((next_blue < orders.size()) || (next_orange < orders.size())) {
    bool pushed = false;
    if (next_blue < orders.size()) {
      if (blue_pos == orders[next_blue].pos) {
        if (next_blue < next_orange) {
          ++next_blue;
          while ((next_blue < orders.size()) && (orders[next_blue].color != BLUE)) {
            ++next_blue;
          }
          pushed = true;
        }
      } else if (blue_pos < orders[next_blue].pos) {
        ++blue_pos;
      } else {
        --blue_pos;
      }
    }

    while ((next_orange < orders.size()) && (orders[next_orange].color != ORANGE)) {
      ++next_orange;
    }
    if (next_orange < orders.size()) {
      if (orange_pos == orders[next_orange].pos) {
        if (!pushed && (next_orange < next_blue)) {
          ++next_orange;
          while ((next_orange < orders.size()) && (orders[next_orange].color != ORANGE)) {
            ++next_orange;
          }
        }
      } else if (orange_pos < orders[next_orange].pos) {
        ++orange_pos;
      } else {
        --orange_pos;
      }
    }

    ++step;
  }
  return step;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    std::cin >> N;
    std::vector<Order> orders;
    for (int n = 1; n <= N; ++n) {
      Order order;
      std::string color_label;
      std::cin >> color_label;
      if (color_label == "B") {
        order.color = BLUE;
//        std::cout << "BLUE";
      } else if (color_label == "O") {
        order.color = ORANGE;
//        std::cout << "ORANGE";
      } else {
        std::cerr << "error: invalid format" << std::endl;
      }
      std::cin >> order.pos;
//      std::cout << " " << order.pos << std::endl;
      orders.push_back(order);
    }
    std::cout << "Case #" << t << ": " << solve(orders) << std::endl;
  }
  return 0;
}
