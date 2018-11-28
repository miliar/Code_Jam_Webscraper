#include<iostream>
#include <fstream>
using namespace std;

int main(void) {
    fstream input, output;
    long tests, rides_per_day, people_at_once, ride_people, groups, income_per_day, *group_size;
    int i, r, g, j, case_ = 0, g_count;

    input.open("C-small-attempt0.in", ios::in);
    output.open("C-small-attempt0.out", ios::out);
    if (!input.is_open() || !output.is_open()) {
        cout << "Error opening files....\n\n";
        getchar();
        return 1;
    }
    input >> tests;
    cout << tests << endl;

    for (i = 0; i < tests; i++) {
        input >> rides_per_day;
        cout << rides_per_day << "  ";
        input >> people_at_once;
        cout << people_at_once << "  ";
        input >> groups;
        cout << groups << "  " << endl;

        group_size = new long[groups];

        for (j = 0; j < groups; j++) {
            input >> group_size[j];
            cout << group_size[j] << endl;
        }

        income_per_day = 0;
        g = 0;
        for (r = 0; r < rides_per_day; r++) {

            cout << "\nride : " << r << endl;

            ride_people = 0;
            g_count = 0;
            while (1) {
                if (g == groups) {
                    g = 0;
                }

                if (ride_people + group_size[g] <= people_at_once && g_count < groups) {
                    income_per_day += group_size[g];
                    ride_people += group_size[g];
                    cout << group_size[g] << " ";
                    g_count++;
                    g++;
                } else {
                    break;
                }
            }
        }
        cout << "income_per_day : " << income_per_day << endl;
        output << "Case #" << ++case_ << ": " << income_per_day << "\n";
    }
    input.close();
    output.close();
    return 0;
}