#include <string>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
    vector<int> pred[256];
    pred['w'].push_back(1);
    pred['e'].push_back(2);
    pred['l'].push_back(3);
    pred['c'].push_back(4);
    pred['o'].push_back(5);
    pred['m'].push_back(6);
    pred['e'].push_back(7);
    pred[' '].push_back(8);
    pred['t'].push_back(9);
    pred['o'].push_back(10);
    pred[' '].push_back(11);
    pred['c'].push_back(12);
    pred['o'].push_back(13);
    pred['d'].push_back(14);
    pred['e'].push_back(15);
    pred[' '].push_back(16);
    pred['j'].push_back(17);
    pred['a'].push_back(18);
    pred['m'].push_back(19);

    int n;
    scanf("%d\n", &n);

    for (int caseNum = 1; caseNum <= n; caseNum++)
    {
        int counts[20];
        memset(counts, 0, sizeof(counts));
        counts[0] = 1;

        char line[1000];
        fgets(line, 1000, stdin);
        if (line[strlen(line) - 1] == '\n')
            line[strlen(line) - 1] = 0;

        int len = strlen(line);
        for (int i = 0; i < len; i++)
        {
            vector<int> &pos = pred[line[i]];
            for (unsigned int j = 0; j < pos.size(); j++)
            {
                int p = pos[j];
                counts[p] = (counts[p] + counts[p - 1]) % 10000;
            }
        }

        printf("Case #%d: %04d\n", caseNum, counts[19]);
    }

    return 0;
}
