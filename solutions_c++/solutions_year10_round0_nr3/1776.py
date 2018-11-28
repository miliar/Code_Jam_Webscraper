#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        long long r, k, n;
        cin >> r >> k >> n;

        vector<long long> groups(n);
        vector<long long> sums(2 * n);
        long long curSum = 0;
        bool startAt[n];
        for (int i = 0; i < n; i++)
        {
            cin >> groups[i];
            curSum += groups[i];
            sums[i] = curSum;
            startAt[i] = false;
        }

        for (int i = 0; i < n; i++)
        {
            curSum += groups[i];
            sums[n + i] = curSum;
        }

        vector<long long> money;
        long long total = 0;
        int start = 0;
        vector<long long> startsAt;
        while (money.size() < r && !startAt[start])
        {
            startAt[start] = true;
            startsAt.push_back(start);
            int curIndex = start;
            while ((curIndex - start < n) && sums[curIndex] - sums[start] + groups[start] <= k)
                curIndex++;
            if (curIndex == start)
            {
                // Special case; no-one rides the rollercoaster
                money.push_back(0);
                break;
            }

            money.push_back(sums[curIndex - 1] - sums[start] + groups[start]);
            start = curIndex % n;
            total += money.back();
        }

        if (money.size() < r)
        {
            // Find where the cycle starts
            long long cycleStart = 0;
            long long cyclePay = total;

            while (startsAt[cycleStart] != start)
            {
                cyclePay -= money[cycleStart];
                cycleStart++;
            }

            long long cycleLength = money.size() - cycleStart;

            total += ((r - money.size()) / cycleLength) * cyclePay;
            long long rem = (r - money.size()) % cycleLength;
            for (long long i = 0; i < rem; i++)
                total += money[i + cycleStart];
        }

        cout << "Case #" << caseNum << ": " << total << endl;
    }

    return 0;
}
