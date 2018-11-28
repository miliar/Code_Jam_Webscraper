#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>


using namespace std;

template <typename S, typename E>
void Dump(const S &sequence)
{
    copy(sequence.begin(), sequence.end(), ostream_iterator<E>(cout, " "));
    cout << endl;
}

template <typename M>
void DumpMap(const M &m)
{
    for (typename M::const_iterator iter=m.begin(); iter!=m.end(); ++iter)
    {
        cout << "(" << iter->first << ", " << iter->second << ") ";
    }

    cout << endl;
}

void Clear()
{
}

void Run()
{
    int P, K, L;
    cin >> P >> K >> L;

    //vector<int> letters;
    multimap<int, int> freqs;

    for (int i=0; i<L; i++)
    {
        int freq;
        cin >> freq;
        //letters.push_back(letter);
        freqs.insert(multimap<int, int>::value_type(freq, i+1));
    }

    //DumpMap<multimap<int, int> >(freqs);

    int keypad[K];

    for (int i=0; i<K; i++)
    {
        keypad[i] = 0;
    }

    long long numPresses = 0;
    int n = 0;

    for (multimap<int, int>::reverse_iterator iter = freqs.rbegin();
         iter != freqs.rend();
         iter++)
    {
        int key = iter->second;
        int freq = iter->first;
        //cout << "(" << iter->first << ", " << iter->second << ") ";

        keypad[n] += 1;
        assert(keypad[n] <= P);
        numPresses += freq * keypad[n];

        n = (n + 1) % K;
    }

    cout << numPresses << endl;

    Clear();
}

int main(int argc, char *argv[])
{
    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        Run();
    }

    return 0;
}
