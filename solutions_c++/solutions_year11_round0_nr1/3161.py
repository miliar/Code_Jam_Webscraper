#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>

#define ORANGE 'O'
#define BLUE   'B'

using namespace std;

class Order {
public:
  Order() { }
  Order(char p_color, int p_pos) { m_color = p_color; m_pos = p_pos; }
  
  inline bool isValid() { return m_color == ORANGE || m_color == BLUE; }
  
  void readColor() { cin >> m_color >> m_pos; }
  
  inline bool isOrange() { return m_color == ORANGE; }
  inline bool isBlue() { return m_color == BLUE; }
  
  inline int position() { return m_pos; }
  
private:
  char m_color;
  int m_pos;
};

class Orders {
public:
  Orders() { m_opos = 1; m_bpos = 1; m_order_index = 0; }
  
  void readOrders() {
    int l_n;
    Order l_order;
  
    cin >> l_n;
    
    for(int i = 0; i < l_n; ++i)
      l_order.readColor(), m_orders.push_back(l_order);
  }
  
  inline int getOrangePos() { return m_opos; }
  inline int getBluePos() { return m_bpos; }
  
  int advance() {
    if(m_order_index >= m_orders.size())
      return 0;
    
    char l_color = (m_orders[m_order_index].isBlue() ? BLUE : ORANGE);
    Order l_cur = m_orders[m_order_index];
    Order l_otherColor = nextOrder(l_color == BLUE ? ORANGE : BLUE, m_order_index+1);
    int &l_cpos = (l_color == BLUE ? m_bpos : m_opos);
    int &l_othpos = (l_color == ORANGE ? m_bpos : m_opos);
    int l_steps = abs(l_cpos - l_cur.position()) + 1;
      
    l_cpos = l_cur.position();
      
    if(l_otherColor.isValid()) {
      if(abs(l_othpos - l_otherColor.position()) < l_steps)
        l_othpos = l_otherColor.position();
      else {
        if(l_othpos > l_otherColor.position())
          l_steps = -l_steps;

        l_othpos += l_steps;
      }
    }
    
    ++m_order_index;
    return abs(l_steps);
  }
  
private:
  int m_opos, m_bpos;
  unsigned int m_order_index;
  vector<Order> m_orders;
  
  Order nextOrder(char p_color, int p_index) {
    if(p_color == ORANGE) {
      for(unsigned int i = p_index; i < m_orders.size(); ++i)
        if(m_orders[i].isOrange())
          return m_orders[i];
    }
    else {
      for(unsigned int i = p_index; i < m_orders.size(); ++i)
        if(m_orders[i].isBlue())
          return m_orders[i];
    }
        
    return Order('G', 1);
  }
};

int doTheMath(Orders &p_orders) {
  int l_steps;
  int l_total = 0;
  
  do {
    l_steps = p_orders.advance();
    l_total += l_steps;
  }
  while(l_steps > 0);
  
  return l_total;
}

int main() {
  int l_test_cases;
  
  cin >> l_test_cases;
  
  for(int i = 0; i < l_test_cases; ++i) {
    Orders l_orders;
    
    l_orders.readOrders();
    
    cout << "Case #" << (i+1) << ": " << doTheMath(l_orders) << endl;
  }
  
  return 0;
}
