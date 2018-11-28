#include <iostream>
#include <vector>
#include <string>
#include <set>


using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int Case = 1; Case <= T; ++Case) {
        int N, M;

        cin >> N >> M;

        set<string> exists;
        for (int i = 0; i < N; ++i) {
            string s;
            cin >> s;

            while (exists.count(s) == 0 && !s.empty()) {
                exists.insert(s);
                s.erase(s.rfind('/'));
            }
        }

		int result = 0;

        for (int i = 0; i < M; ++i) {
            string s;
            cin >> s;

			while (exists.count(s) == 0 && !s.empty()) {
				exists.insert(s);
				s.erase(s.rfind('/'));
				++result;
			}
        }

		printf("Case #%d: %d\n", Case, result);
    }

    return 0;
}

