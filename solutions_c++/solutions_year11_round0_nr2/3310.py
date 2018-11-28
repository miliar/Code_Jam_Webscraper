#include <list>
#include <vector>
#include <iostream>

using namespace std;

struct element
{
public:
    element() {
        memset(opposeM, false, sizeof(opposeM));
        memset(combineM, '\0', sizeof(combineM));
        fOpposeM = false;
    }
    bool opposeM[26];
    char combineM[26];
    bool fOpposeM;
};

class Magicka
{
public:
    void Start() {
        int T = 0;
        cin >> T;
        
        for (int t = 0; t < T; t++) {
            elementDefsM.clear();
            elementListM.clear();
            sizeM = 0;
            elementDefsM.resize(26);
            int C = 0;
            cin >> C;
            if (C > 0) {
                for (int c = 0; c < C; c++) {
                    char c1, c2, c3;
                    cin >> c1;
                    cin >> c2;
                    cin >> c3;
                    elementDefsM[c1 - 'A'].combineM[c2 - 'A'] = c3;
                    elementDefsM[c2 - 'A'].combineM[c1 - 'A'] = c3;
                }
            }
            int D = 0;
            cin >> D;
            if (D > 0) {
                for (int d = 0; d < D; d++) {
                    char c1, c2;
                    cin >> c1;
                    cin >> c2;
                    elementDefsM[c1 - 'A'].opposeM[c2 - 'A'] = true;
                    elementDefsM[c2 - 'A'].opposeM[c1 - 'A'] = true;
                    elementDefsM[c1 - 'A'].fOpposeM = true;
                    elementDefsM[c2 - 'A'].fOpposeM = true;
                }
            }
            int N = 0;
            cin >> N;
            for (int n = 0; n < N; n++) {
                char c;
                cin >> c;
                this->Invoke(c);
            }

            cout << "Case #" << (t + 1) << ": ";
            this->Print();
            cout << "\n";
        }
    }

    void Print() 
    {
        list<char>::iterator iter = elementListM.begin();
        cout << "[";
        bool fFirst = true;;
        while (iter != elementListM.end())
        {
            if (!fFirst) {
                cout << ", ";
            }
            else {
                fFirst = false;
            }
            cout << *iter;
            iter++;
        }
        cout << "]";
    }

    void Invoke(char c)
    {
        elementListM.push_back(c);
        sizeM++;
        this->CheckCombine();
    }

    void CheckCombine()
    {
        if (sizeM <= 1) return;

        char c1 = elementListM.back();
        elementListM.pop_back();
        char c2 = elementListM.back();
        elementListM.pop_back();
        char c3;
        if ((c3 = elementDefsM[c1 - 'A'].combineM[c2 - 'A']) != '\0') {
            elementListM.push_back(c3);
            sizeM--;
        }
        else {
            elementListM.push_back(c2);
            elementListM.push_back(c1);
        }
        this->CheckOppose();
    }

    void CheckOppose() {
        if (sizeM <= 1) return;

        char c1 = elementListM.back();
        if (!elementDefsM[c1 - 'A'].fOpposeM) {
            return;
        }
        list<char>::reverse_iterator iter = elementListM.rbegin();
        iter++;
        while (iter != elementListM.rend()) {
            if (elementDefsM[c1 - 'A'].opposeM[*iter - 'A']) {
                elementListM.clear();
                sizeM = 0;
                return;
            }
            iter++;
        }
    }

private:
    vector<element> elementDefsM;
    list<char> elementListM;
    int sizeM;
};

int main(int argc, const char *argv[])
{
    Magicka m;
    m.Start();
    return 0;
}
