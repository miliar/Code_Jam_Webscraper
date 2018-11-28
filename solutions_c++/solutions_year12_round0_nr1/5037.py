#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char** argv)
{
    std::ifstream f1;
    std::ofstream f2;

    f1.open("A-small-1.in");
    f2.open("A-small-1.out");

    int T;

    f1 >> T;

    std::string googlerese = "ynficwlbkuomxsevzpdrjgthaq";
    std::string english =    "abcdefghijklmnopqrstuvwxyz";

    std::string G;
    int len, pos;

    std::getline(f1, G);

    for (int i = 1; i <= T; ++i)
        {
            f2 << "Case #" << i << ": ";

            std::getline(f1, G);

            len = G.size();

            for (int j = 0; j < len; ++j)
                {
                    if (G.at(j) != ' ')
                        {
                            pos = googlerese.find(G.at(j));
                            f2 << english.at(pos);
                        }
                    else if (G.at(j) == ' ')
                        {
                            f2 << " ";
                        }
                }

            f2 << "\n";
        }

    f1.close();
    f2.close();

    return (EXIT_SUCCESS);
}
