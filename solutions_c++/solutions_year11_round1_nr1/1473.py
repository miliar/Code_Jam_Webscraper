
#include <iostream>
#include <vector>


using namespace std;
typedef std::vector<int> VI;
typedef std::vector<char> VC;

void
do_test(int test_num, long n, int pd, int pg)
{
    string ans = "Broken";
    for (int i = 1; i <= n; i++) {
        if (((i * pd) % 100) == 0) {
            ans = "Possible";
        }
    }
    if (pg == 100 && pd != 100) {
        ans = "Broken";
    } else if (pg == 0 && pd != 0) {
        ans = "Broken";
    }

    cout << "Case #" << test_num << ": " << ans << endl;
}

int
main(int argc, char **argv)
{
    int num_tests = 0;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; ++i) {
        long N;
        int Pd;
        int Pg;

        cin >> N;
        cin >> Pd;
        cin >> Pg;
            
        do_test(i, N, Pd, Pg);

    }
}
    
