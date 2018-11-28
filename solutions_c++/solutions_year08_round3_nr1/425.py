#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <stdint.h>

//#define DEBUG

void output(int64_t result, size_t line)
{
    if (!result)
        std::cout << "Case #" << line + 1 << ": Impossible" << std::endl;
    else
        std::cout << "Case #" << line + 1 << ": " << result << std::endl;
}

typedef std::multimap<int32_t, size_t> freq_letter_map_t;

class KeyMap 
{
    size_t P, K, L, i;
public:
    KeyMap(size_t in_P, size_t in_K, size_t in_L)
        : P(in_P), K(in_K), L(in_L), i(0)
    {
#ifdef DEBUG
        printf("P(letters/key): %d K(keys): %d L(letters): %d\n", P, K, L);
#endif
    }

    int64_t add()
    {
        // assume called once per letter in frequency order
        return 1 + (i++/K);
    }
};

int64_t minimize(size_t P, size_t K, size_t L, const freq_letter_map_t& map)
{
    int64_t result = 0;
    KeyMap km(P, K, L);
    for (freq_letter_map_t::const_reverse_iterator iter = map.rbegin();
         iter != map.rend();
         ++iter)
    {
        int64_t temp_result = km.add() * iter->first; // add this letter
#ifdef DEBUG
        printf("letter: %d freq: %d presses*freq: %d\n", iter->second, iter->first, (int)temp_result);
#endif
        if (!temp_result) return 0;
        result += temp_result;
    }
    return result;
}
    

int main()
{
    size_t numlines;
    std::cin >> numlines;

    for (size_t line = 0; line < numlines; ++line)
    {
        size_t P, K, L;
        std::cin >> P >> K >> L;
        std::multimap<int32_t, size_t> freq_letter_map;
        for (size_t item = 0; item < L; ++item)
        {
            int32_t freq;
            std::cin >> freq;
            freq_letter_map.insert(std::pair<int32_t, size_t>(freq, item));
        }

        int64_t result = minimize(P, K, L, freq_letter_map);
        output(result, line);
    }

    return 0;
}
