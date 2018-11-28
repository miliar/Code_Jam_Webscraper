#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <functional>

#include <boost/foreach.hpp>

#define foreach BOOST_FOREACH

typedef char Element;

struct ElementCombination {
  Element first_element;
  Element second_element;
};


struct ElementCombinationLess : public std::binary_function<const ElementCombination, const ElementCombination, bool> {
  bool operator () (const ElementCombination& left, const ElementCombination& right) const
  {
    return
        left.first_element < right.first_element || 
        (left.first_element == right.first_element && left.second_element < right.second_element);
  }
};


struct Case {
  std::map<ElementCombination, Element, ElementCombinationLess> element_combinations;
  std::set<ElementCombination, ElementCombinationLess> oposite_element_combinations;
  std::vector<Element> element_seq;
};


std::vector<Element> ComputeCaseElementSeq(const Case& case_item)
{
  std::vector<Element> element_seq;
  std::map<Element, int> elements_presented;
  typedef std::pair<Element, int> ElementIntPair;
  
  foreach (Element element, case_item.element_seq) {
    if (!element_seq.empty()) {
      const ElementCombination combination = { element_seq.back(), element };
      const std::map<ElementCombination, Element, ElementCombinationLess>::const_iterator it =
      case_item.element_combinations.find(combination);
      if (it != case_item.element_combinations.end()) {
        --elements_presented[element_seq.back()];
        element_seq.back() = it->second;
        continue;
      }
    }
    
    bool was_cleaned = false;
    
    foreach (ElementIntPair pair, elements_presented) {
      if (pair.second > 0) {
        const ElementCombination combination = { pair.first, element };
        if (case_item.oposite_element_combinations.count(combination)) {
          element_seq.clear();
          elements_presented.clear();
          was_cleaned = true;
          break;
        }
      }
    }
      
    if (!was_cleaned) {
      element_seq.push_back(element);
      ++elements_presented[element];
    }
  }
  
  return element_seq;
}


std::vector<Case> Input()
{
  size_t number_of_cases;
  size_t number_of_combinations;
  size_t element_seq_length;
  std::string element_seq;
  std::string combination_descriptor;
  ElementCombination combination;
  
  std::vector<Case> result;
  std::cin >> number_of_cases;
  result.resize(number_of_cases);
  
  foreach (Case& case_item, result) {
    std::cin >> number_of_combinations;
    for (size_t i = 0; i < number_of_combinations; ++i) {
      std::cin >> combination_descriptor;
      combination.first_element = combination_descriptor.at(0);
      combination.second_element = combination_descriptor.at(1);
      case_item.element_combinations[combination] = combination_descriptor.at(2);
      std::swap(combination.first_element, combination.second_element);
      case_item.element_combinations[combination] = combination_descriptor.at(2);
    }
    
    std::cin >> number_of_combinations;
    for (size_t i = 0; i < number_of_combinations; ++i) {
      std::cin >> combination_descriptor;
      combination.first_element = combination_descriptor.at(0);
      combination.second_element = combination_descriptor.at(1);
      case_item.oposite_element_combinations.insert(combination);
      std::swap(combination.first_element, combination.second_element);
      case_item.oposite_element_combinations.insert(combination);
    }
    
    std::cin >> element_seq_length;
    std::cin >> element_seq;
    element_seq.at(element_seq_length - 1);
    case_item.element_seq.assign(element_seq.begin(), element_seq.begin() + element_seq_length);
  }
  
  return result;
}


void Output(size_t case_index, const std::vector<Element>& case_element_seq)
{
  std::cout << "Case #" << case_index << ": ";
  
  std::cout << "[";
  bool is_first = true;
  foreach (Element element, case_element_seq) {
    if (is_first) {
      is_first = false;
      std::cout << element;
    } else {
      std::cout << ", " << element;
    }
  }
  std::cout << "]\n";
}


int main()
{
  const std::vector<Case> case_seq = Input();
  for (size_t case_no = 0; case_no < case_seq.size(); ++case_no) {
    Output(case_no + 1, ComputeCaseElementSeq(case_seq[case_no]));
  }
  return 0;
}