#include <cstdio>
#include <cassert>
#include <algorithm>

class Robot
{
public:
    int m_state, m_time, m_wait;

    void reset()
    {
        m_state = 1; m_time = 0; m_wait = 0;
    }

    void advance(int n)
    {
        int timetomove = abs(m_state - n) - m_wait;

        m_time += ((timetomove > 0) ? timetomove : 0) + 1;
        m_state = n;
        m_wait = 0;
    }

    void wait(const Robot &n)
    {
        m_wait += n.m_time - m_time;

        m_time = n.m_time;
    }

    int time() const { return m_time; }
};

Robot r1, r2;

int main()
{
    FILE *f = fopen("in.txt", "r");
    FILE *fo = fopen("out.txt", "w");
//    FILE *fo = stdout;
    assert(f && fo);

    int n;
    fscanf(f, "%d\n", &n);

    for (int i = 0; i < n; i++)
    {
        r1.reset(); r2.reset();
        int m;
        fscanf(f, "%d", &m);
        fprintf(fo, "Case #%d: ", i+1);

        for (int j = 0; j < m; j++)
        {
            int a;
            char b = fgetc(f);

            while (b != 'O' && b != 'B') b = fgetc(f);

            fscanf(f, "%d", &a);

            switch (b)
            {
            case 'B':
                r1.advance(a);
                r2.wait(r1);
                break;
            case 'O':
                r2.advance(a);
                r1.wait(r2);
                break;
            }
        }

        fprintf(fo, "%d\n", std::max(r1.time(), r2.time()));


    }
}
