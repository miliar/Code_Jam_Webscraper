#include <iostream>
#include <fstream>
#include <iomanip>// fixed << setprecision(#);
#include <vector>
#include <string>

using namespace std;
bool hashLeft(vector<string> painting, int R, int C);
int main()
{
    ifstream input ("input2.txt");
    ofstream output ("output2.txt");

    int cases;
    input >> cases;

    for(int a = 0; a < cases; a ++)
    {
        int C, R;
        input >> R >> C;
        vector<string> painting;
        vector<string> origPainting;
        string tmp;
        for(int b = 0; b < R; b ++)
        {
            input>>tmp;
            painting.push_back(tmp);
        }
        origPainting = painting;

        for(int i = 0; i < 2; i++)
        {
            for(int j = 0; j < 2; j ++)
            {
                for(int b = i; b< R-1;b++)
                {
                    for(int c = j; c < C-1; c++)
                    {
                        if(painting[b][c] =='#'&&painting[b+1][c] =='#'&& painting[b+1][c+1] =='#'&& painting[b][c+1] =='#')
                        {
                            painting[b][c] = '/';
                            painting[b+1][c] = char(char(92));
                            painting[b+1][c+1] = '/';
                            painting[b][c+1] = char(char(92));
                        }

                    }

                }
                if(hashLeft(painting,R,C) == true)
                {
                    painting = origPainting;
                }
                else
                {
                    break;
                }
            }
            if(hashLeft(painting,R,C) == true)
            {
                break;
            }
        }
        // scan for  #

        if(hashLeft(painting,R,C) == true)
        {
            output << "Case #" << a+1 << ": " << endl <<"Impossible"<<endl;
            /*for(int b = 0; b< R;b++)
            {
                output << painting[b] << endl;
            }*/
        }
        else
        {

            output << "Case #" << a+1 << ": " << endl;
            for(int b = 0; b< R;b++)
            {
                output << painting[b] << endl;
            }
        }

    }

    return 0;
}
bool hashLeft(vector<string> painting, int R, int C)
{

        for(int b = 0; b< R;b++)
        {
            for(int c = 0; c < C; c++)
            {
                if(painting[b][c] =='#')
                {
                    return true;
                }

            }

           // output << painting[b] <<endl;
        }
        return false;
}
