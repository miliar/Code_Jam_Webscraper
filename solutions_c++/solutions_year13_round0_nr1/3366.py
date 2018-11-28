#include <fstream>

using namespace std;

bool stest(int str[4][4],int man)
{
    for (int i = 0;i < 4;i++)
    {
        int j = 0;
        while (j < 4 && (str[i][j] == man || str[i][j] == 3)) j++;
        if (j == 4) return true;
    }

    for (int i = 0;i < 4;i++)
    {
        int j = 0;
        while (j < 4 && (str[j][i] == man || str[j][i] == 3)) j++;
        if (j == 4) return true;
    }

    int i = 0;
    for (i = 0;i < 4;i++)
    {
        if (str[i][i] != man && str[i][i] != 3) break;
    }
    if (i == 4) return true;

    for (i = 0;i < 4;i++)
    {
        if (str[i][3 - i] != man && str[i][3 - i] != 3) break;
    }
    if (i == 4) return true;
    return false;
}

bool isDraw(int str[4][4])
{
    for (int i = 0;i < 4;i++)
        for (int j = 0;j < 4;j++)
        {
            if (str[i][j] == 0) return false;
        }
    return true;
}

int main()
{
    ifstream in("T.in");
    ofstream out("T.out");

    int times = 0;
    in >> times;

    in.get();
    int str[4][4];
    for (int num = 0;num < times;num++)
    {
        char test = 0;
        for (int i = 0;i < 4;i++)
        {
            for (int j = 0;j < 4;j++)
            {
                in.get(test);
                switch(test)
                {
                    case 'X': str[i][j] = 1; break;
                    case 'O': str[i][j] = 2; break;
                    case '.': str[i][j] = 0; break;
                    case 'T': str[i][j] = 3; break;
                    case '\n': out << "Error!";
                };
            }
            in.get();
        }
        in.get();

        out << "Case #" << num + 1;
        if (stest(str,1)) out << ": X won\n";
        else if (stest(str,2)) out << ": O won\n";
        else if (isDraw(str)) out << ": Draw\n";
        else out << ": Game has not completed\n";
    }
    return 0;
}
