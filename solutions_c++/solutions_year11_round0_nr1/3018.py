#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

struct button_order
{
    int button;
    char robot;
};

int get_next_position(char robot, const vector<button_order> & sequence)
{
    for (size_t i = 0; i < sequence.size(); i++)
        if (sequence[i].robot == robot)
        {
            int v = sequence[i].button;
            return v;
        }
    return -1;
}

int main()
{
    int N, B;
    vector<button_order> sequence;
    int b_robot, o_robot;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> B;
        sequence.clear();

        for (int j = 0; j < B; j++)
        {
            button_order current;
            cin >> current.robot >> current.button;
            sequence.push_back(current);
        }

        b_robot = o_robot = 1;
        int time = 0;

        while (!sequence.empty())
        {
            int nbr = get_next_position('B', sequence);
            int nor = get_next_position('O', sequence);

            if ((sequence[0].robot == 'B' && nbr == b_robot) ||
                (sequence[0].robot == 'O' && nor == o_robot))
                sequence.erase(sequence.begin());

            if (nbr != -1)
            {
                if (nbr < b_robot)
                    b_robot--;
                else if (nbr > b_robot)
                    b_robot++;
            }

            if (nor != -1)
            {
                if (nor < o_robot)
                    o_robot--;
                else if (nor > o_robot)
                    o_robot++;
            }

            time++;
        }

        printf("Case #%d: %d\n", i+1, time);
    }

    return 0;
}
