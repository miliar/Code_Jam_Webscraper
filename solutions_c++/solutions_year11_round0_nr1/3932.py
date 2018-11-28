#include <list>
#include <fstream>

struct DataSet
{
    int m_pos;    //[1, 100]
    int m_order;  //0~
    DataSet(void)
        : m_pos(1)
        , m_order(0)
    {}
    DataSet(int pos, int order)
        : m_pos(pos)
        , m_order(order)
    {}
};

/**
 *	@return is push
 */
bool robot(const DataSet& data, const int orderflag, int& posnow)
{
    bool push = false;
    if (data.m_pos != posnow)
    {
        if (data.m_pos > posnow)
        {
            ++posnow;
        }
        else
        {
            --posnow;
        }
        //printf("Move to button %d", posnow);
    }
    else if (data.m_order == orderflag)
    {
        //printf("Push button %d   ", posnow);
        push = true;
    }
    //else
    //{
    //    printf("Stay at button %d", posnow);
    //}
    return push;
}

int BlackBox(std::list<DataSet>& orange, std::list<DataSet>& blue)
{
    int orderflag(0), stepnum(0);
    int posOrange(1), posBlue(1);

    while(!orange.empty() || !blue.empty())
    {
        bool push = false;
        //printf("%d | ", stepnum + 1);
        if (!orange.empty())
        {
            bool p = robot(orange.front(), orderflag, posOrange);
            if (p)
            {
                orange.pop_front();
                push = true;
            }
        }
        //else
        //{
        //    printf(" Stay at button %d", posOrange);
        //}

        //printf(" | ");

        if (!blue.empty())
        {
            bool p = robot(blue.front(), orderflag, posBlue);
            if (p)
            {
                blue.pop_front();
                push = true;
            }
        }
        //else
        //{
        //    printf("Stay at button %d", posBlue);
        //}
        //printf("\n");

        if (push)
        {
            ++orderflag;
        }

        ++stepnum;
    }

    return stepnum;
}



int main(void)
{
    //std::list<DataSet> orange, blue;
    //int order(0);
    //orange.push_back(DataSet(2, order++));
    //blue.push_back(DataSet(1, order++));
    //blue.push_back(DataSet(2, order++));
    //orange.push_back(DataSet(4, order++));
    //int res = BlackBox(orange, blue);
    //printf("Case  %d\n", res);

    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");

    if (infile)
    {
        int testNum(0);
        infile >> testNum;
        for (int t = 0; t < testNum; ++t)
        {
            std::list<DataSet> orange, blue;
            int targetNum(0), order(0);
            infile >> targetNum;
            for (int i = 0; i < targetNum; ++i)
            {
                char robot(' ');
                int pos(1);
                infile >> robot;
                infile >> pos;
                if (robot == 'O')
                {
                    orange.push_back(DataSet(pos, order));
                }
                else
                {
                    blue.push_back(DataSet(pos, order));
                }
                ++order;
            }
            int res = BlackBox(orange, blue);
            outfile << "Case #" << t + 1 << ": " << res << std::endl;
            //printf("Case #%d: %d\n", t + 1, res);

        }
    }
    infile.close();
    outfile.close();

    system("pause");
    return 0;
}

