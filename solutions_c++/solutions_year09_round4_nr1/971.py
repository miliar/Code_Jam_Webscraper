#include <iostream>
#include <string>

int main()
{
    int t, T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int N;
        int a[40];
        std::cin >> N;
        for (int i = 0 ; i < N ; ++i)
        {
            std::string s;
            do
            {
                std::getline(std::cin, s);
            }
            while (s.size() < N);
            int k = 0;
            for (int j = 0 ; j < N ; ++j)
                if (s[j] == '1')
                    k = j;
            a[i] = k;
        }
        bool ok = false;
        int num = 0;
        do
        {
            ok = false;
            /*for (int i = 0 ; i < N-1 ; ++i)
                if (a[i] > i && a[i] != a[i+1])
                {
                    std::swap(a[i], a[i+1]);
                    ++num;
                    ok = true;
                }

            if (!ok)*/
            {
                for (int i = 0 ; i < N-1 ; ++i)
                    if (a[i] > i/* && a[i] == a[i+1]*/)
                    {
                        // bubble up smaller value
                        for (int j = i+1 ; j < N ; ++j)
                            if (a[j] < a[i])
                            {
                                while (i < j)
                                {
                                    std::swap(a[j], a[j-1]);
                                    --j;
                                    ++num;
                                }
                                break;
                            }
                        ok = true;
                        break;
                    }
            }
        }
        while (ok);
        std::cout << "Case #" << t << ": " << num << "\n";
    }
    return 0;
}
