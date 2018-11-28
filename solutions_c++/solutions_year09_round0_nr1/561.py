#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> words;
std::vector<int> count;
int L, D, N;

int main()
{
    std::cin >> L >> D >> N;
    
    std::string s;
    std::getline(std::cin, s);
    for (int i = 0 ; i < D ; ++i)
    {
        std::getline(std::cin, s);
        words.push_back(s);
    }

    for (int n = 1 ; n <= N ; ++n)
    {
        count.clear();
        count.resize(D);
        for (int i = 0 ; i < L ; ++i)
        {
            bool single = true;
            char c;
            do
            {
                std::cin >> c;
                if (c == '(')
                    single = false;
                if (c >= 'a' && c <= 'z')
                {
                    // find the word
                    for (int j = 0 ; j < D ; ++j)
                        if (words[j][i] == c)
                            ++count[j];
                }
            }
            while (!single && c != ')');
        }
        int K = 0;
        for (int i = 0 ; i < D ; ++i)
            if (count[i] == L)
                ++K;
        std::cout << "Case #" << n << ": " << K << "\n";
    }
	return 0;
}

