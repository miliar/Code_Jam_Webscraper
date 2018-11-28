#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct start {
    public:
    long long value;
    int next;
};

int main() {
    long long N, R, K, T, iMoney(0), iCount(0), ppl(0);
    ifstream fin("c.in");
    ofstream fout("c.out");
    vector <int> v, temp;
    vector <start> s;
    start sTemp;
    int count2(0);

    fin >> T;

    for (int t = 0; t < T; t++) {
        fin >> R >> K >> N;
        iMoney = 0;
        s.clear();
        v.clear();

        for (int i = 0; i < N; i++) {
            v.push_back(0);
            fin >> v.back();
        }

        for (int i = 0; i < N; i++) {
            ppl = 0;
            temp = v;

            for (int k = 0; k < i; k++) {
                temp.push_back(temp[0]);
                temp.erase(temp.begin(), temp.begin() + 1);
            }
            iCount = i;
            count2 = 0;

            while (true) {
                count2++;
                if (count2 > N)
                    break;
                if (ppl + temp[0] > K)
                    break;

                ppl += temp[0];
                iCount++;
                if (iCount > N - 1)
                    iCount = 0;
                temp.push_back(temp[0]);
                temp.erase(temp.begin(), temp.begin() + 1);
            }
            sTemp.value = ppl;
            sTemp.next = iCount;
            s.push_back(sTemp);
        }

        int iNext = 0;
        for (int i = 0; i < R; i++) {
            iMoney += s[iNext].value;
            iNext = s[iNext].next;
        }
        fout << "Case #" << (t + 1) << ": " << iMoney << endl;
    }

    //for (unsigned int i = 0; i < s.size(); i++) {
        //cout << s[i].value << " " << s[i].next << endl;
    //}

    return 0;
}
