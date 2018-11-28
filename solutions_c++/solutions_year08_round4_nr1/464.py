#include <iostream>

using namespace std;

class node
{
public:
    node() {}

    void readin(bool leaf)
    {
        this->leaf = leaf;
        if (leaf)
        {
            canChange = false;
            cin >> value;
        }
        else
        {
            cin >> gate >> canChange;
        }

        min[0] = min[1] = -2;
    }

    bool leaf;
    int value;
    int gate;
    int canChange;

    int min[2];
};

node nodes[10000];
int m, v;
int half;

int calc(int x)
{
    if (x < half)
    {
        int o1 = calc((x << 1) + 1);
        int o2 = calc((x << 1) + 2);
        if (nodes[x].gate == 0)
        {
            nodes[x].value = o1 | o2;
        }
        else
        {
            nodes[x].value = o1 & o2;
        }
    }

    return nodes[x].value;
}

int calcmin(int x, int v)
{
    if (nodes[x].value == v)
        return 0;

    if (nodes[x].min[v] != -2)
        return nodes[x].min[v];

    if (nodes[x].leaf)
        return 10001;

    int min = 10001;

    int c1 = (x << 1) + 1;
    int c2 = c1 + 1;

    if (nodes[x].canChange)
    {
        node save = nodes[x];
        // try changing the gate
        nodes[x].canChange = false;
        nodes[x].gate = (1 - nodes[x].gate);
        if (nodes[x].gate == 0)
        {
            nodes[x].value = nodes[c1].value | nodes[c2].value;
        }
        else
        {
            nodes[x].value = nodes[c1].value & nodes[c2].value;
        }

        int min2 = calcmin(x, v) + 1;
        if (min2 < min)
            min = min2;

        nodes[x] = save;
    }

    if (nodes[x].gate == 0)
    {
        // or gate
        if (nodes[x].value == 0)
        {
            // need one or the other
            int m1 = calcmin(c1, 1);
            int m2 = calcmin(c2, 1);
            if (m1 < min)
                min = m1;
            if (m2 < min)
                min = m2;
        }
        else
        {
            // need them both off
            int m = 0;
            if (nodes[c1].value == 1)
                m += calcmin(c1, 0);
            if (nodes[c2].value == 1)
                m += calcmin(c2, 0);
            if (m < min)
                min = m;
        }
    }
    else
    {
        // and gate
        if (nodes[x].value == 0)
        {
            // need them both
            int m = 0;
            if (nodes[c1].value == 0)
                m += calcmin(c1, 1);
            if (nodes[c2].value == 0)
                m += calcmin(c2, 1);
            if (m < min)
                min = m;
        }
        else
        {
            // need one off
            int m1 = calcmin(c1, 0);
            int m2 = calcmin(c2, 0);
            if (m1 < min)
                min = m1;
            if (m2 < min)
                min = m2;
        }
    }

    nodes[x].min[v] = min;
    return min;
}

int main()
{
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++)
    {
        cin >> m >> v;
        half = (m - 1) / 2;
        for (int i = 0; i < half; i++)
            nodes[i].readin(false);
        for (int i = half; i < m; i++)
            nodes[i].readin(true);

        calc(0);

        int min = calcmin(0, v);

        cout << "Case #" << c << ": ";
        if (min == 10001)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << min << endl;
    }
    return 0;
}
