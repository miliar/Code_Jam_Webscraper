#include <iostream>
#include <vector>
#include <boost/foreach.hpp>
#include <stdexcept>


#define foreach BOOST_FOREACH


struct Event {
  enum Color { kBlue = 'B', kOrange = 'O' };
  Color color;
  int position;
};


struct Case {
  std::vector<Event> event_seq;
};


std::vector<Case> Input()
{
  std::vector<Case> result;
  
  size_t number_of_cases;
  std::cin >> number_of_cases;
  result.resize(number_of_cases);

  foreach (Case& case_item, result) {
    size_t number_of_case_items;
    std::cin >> number_of_case_items;
    case_item.event_seq.resize(number_of_case_items);
    
    foreach (Event& event_item, case_item.event_seq) {
      char event_color;
      std::cin >> event_color;
      event_item.color = static_cast<Event::Color>(event_color);
      std::cin >> event_item.position;
    }
  }
  return result;
}


void Output(size_t case_index, int case_time)
{
  std::cout << "Case #" << case_index << ": " << case_time << '\n';
}


int ComputeCaseTime(const Case& case_item)
{
  int last_blue_position = 1;
  int last_blue_time = 0;
  int last_orange_position = 1;
  int last_orange_time = 0;
  int last_time = 0;
  
  foreach (const Event& event, case_item.event_seq) {
    if (event.color == Event::kBlue) {
      const int distance = std::abs(last_blue_position - event.position);
      
      last_time = std::max(last_time, last_blue_time + distance) + 1;
      last_blue_position = event.position;
      last_blue_time = last_time;
      
    } else if (event.color == Event::kOrange) {
      const int distance = std::abs(last_orange_position - event.position);
      
      last_time = std::max(last_time, last_orange_time + distance) + 1;
      last_orange_position = event.position;
      last_orange_time = last_time;
    }
  }
  
  return last_time;
}

int main()
{
  std::vector<Case> case_seq = Input();
  for (size_t case_no = 0; case_no < case_seq.size(); ++case_no) {
    Output(case_no + 1, ComputeCaseTime(case_seq[case_no]));
  }
}