#include <iostream>

int main()
{
  size_t number_of_cases;
  std::cin >> number_of_cases;

  for (size_t case_index = 1; case_index <= number_of_cases; ++case_index) {
    size_t number_of_elements;
    std::cin >> number_of_elements;

    size_t number_of_mismatch = 0;
    for (size_t element_index = 1; element_index <= number_of_elements; ++element_index) {
      size_t element;
      std::cin >> element;
      if (element != element_index) {
	++number_of_mismatch;
      }
    }

    std::cout << "Case #" << case_index << ": " << number_of_mismatch << '\n';
  }

  return 0;
}
