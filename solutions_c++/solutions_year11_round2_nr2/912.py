#include <iostream>

int main()
{
    size_t number_of_cases;
    std::cin >> number_of_cases;

    for (size_t case_index =  1; case_index <= number_of_cases; ++case_index) {
        int number_of_points;
        long double distance;
        std::cin >> number_of_points >> distance;

        long double time = 0;
        long double previouse_position = -1000000000;

        for (int i = 0; i < number_of_points; ++i) {
            long double x;
            size_t n;
            std::cin >> x >> n;

            for (size_t j = 0; j < n; ++j) {
                const long double left = std::max(previouse_position + distance, x - time);
                const long double right = x + time;

                if (left < right) {
                    previouse_position = left;
                } else {
                    time += (left - right) / 2;
                    previouse_position += time;
                }
            }
        }

        std::cout << "Case #" << case_index << ": " << std::fixed <<  time << '\n';
    }
}
