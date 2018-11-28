#include <fstream>
#include <string>
#include <iostream>

using namespace std;

long Finder(int candies[], int begin, int end, int size)
{
    long sum = 0, sum_next = 0, sum_dec_left = 0, sum_dec_right = 0;
    for (int i = begin; i < end; ++i) {
        if (i >= size) {
            sum ^= candies[i % size];
            sum_dec_left += candies[i % size];
        }
        else {
            sum ^= candies[i];
            sum_dec_left += candies[i];
        }
        sum_dec_right = 0;
        sum_next = 0;
        for (int j = i + 1; j < end; ++j) {
            if (j >= size) {
                sum_next ^= candies[j % size];
                sum_dec_right += candies[j % size];
            }
            else {
                sum_next ^= candies[j];
                sum_dec_right += candies[j];
            }
        }
        if (sum == sum_next)
            return ((sum_dec_left > sum_dec_right)? sum_dec_left: sum_dec_right);  
    }
    return (-1);    
}

int main()
{
    ifstream in("C-large.in");
    ofstream out("C-large.out");
    int N, T, const_T;
    int candies[1000];
    long sum, max = 0;
    
    in >> T;
    const_T = T;
    while (T) {
        in >> N;
        max = 0;
        for (int i = 0; i < N; ++i)
            in >> candies[i];
        out << "Case #" << (const_T - T + 1) << ": ";
        for (int i = 0; i < N; ++i) {
            sum = Finder(candies, i, N + i, N);
            if (sum > max)
                max = sum;   
        }
        if (!max)
           out << "NO" << endl;
        else
           out << max << endl;
        T--;      
    }
    
    return 0;    
}
