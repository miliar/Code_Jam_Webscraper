#include <fstream>
#include <string>

std::ifstream INPUT;
std::ofstream OUTPUT;

void RunCase();

int main(int argc, char *argv[])
{
    std::string inFileName("test.in");
    std::string outFileName("test.out");
    if (argc == 3)
    {
        inFileName = argv[1];
        outFileName = argv[2];
    }
    INPUT.open(inFileName.c_str());
    OUTPUT.open(outFileName.c_str());
    int noCases;
    INPUT >> noCases;
    for (int i = 0; i < noCases; i++)
    {
        OUTPUT << "Case #" << i + 1 << ": ";
        RunCase();
        OUTPUT << std::endl;
    }
    INPUT.close();
    OUTPUT.close();
    return 0;
}

#include <vector>
std::vector<std::vector<char> > array;
bool areEmptyFields(false);
void ReadArray(int height, int width)
{
    array.resize(height);
    for (int y = 0; y < height; y++)
    {
        array[y].resize(width);
        for (int x = 0; x < width; x++)
        {
            INPUT >> array[y][x];
            if (array[y][x] == '.')
                areEmptyFields = true;
        }
    }
}

void RunCase()
{
    areEmptyFields = false;
    ReadArray(4, 4);
    std::string line;
    getline(INPUT, line);

    char H;
    int HCount;
    char V;
    int VCount;

    for (int a = 0; a < 4; a++)
    {
        V = H = '.';
        for (int i = 0; i < 4; i++)
        {
            if (array[a][i] != '.'
                && array[a][i] != 'T')
                H = array[a][i];
            if (array[i][a] != '.'
                && array[i][a] != 'T')
                V = array[i][a];
        }

        HCount = VCount = 0;
        for (int i = 0; i < 4; i++)
        {
            if (H == array[a][i]
                || array[a][i] == 'T')
                HCount++;
            if (V == array[i][a]
                || array[i][a] == 'T')
                VCount++;
        }

        if (H != '.'
            && HCount == 4)
        {
            OUTPUT << H << " won";
            return;
        }
        if (V != '.'
            && VCount == 4)
        {
            OUTPUT << V << " won";
            return;
        }
    }

    V = H = '.';
    for (int i = 0; i < 4; i++)
    {
        if (array[i][i] != '.'
            && array[i][i] != 'T')
            H = array[i][i];
        if (array[i][3-i] != '.'
            && array[i][3-i] != 'T')
            V = array[i][3-i];
    }

    HCount = VCount = 0;
    for (int i = 0; i < 4; i++)
    {
        if (H == array[i][i]
            || array[i][i] == 'T')
            HCount++;
        if (V == array[i][3-i]
            || array[i][3-i] == 'T')
            VCount++;
    }

    if (H != '.'
        && HCount == 4)
    {
        OUTPUT << H << " won";
        return;
    }
    if (V != '.'
        && VCount == 4)
    {
        OUTPUT << V << " won";
        return;
    }

    if (areEmptyFields)
        OUTPUT << "Game has not completed";
    else
        OUTPUT << "Draw";
}
