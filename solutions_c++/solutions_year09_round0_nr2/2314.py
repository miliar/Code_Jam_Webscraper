#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <fstream>
#include <algorithm>

using namespace std;

int H = 0, W = 0;
int rmap[101][101];
char db[101][101];
int getMinIndex(int j, int k, int *minJ, int *minK)
{
    
    if(j > 0 && rmap[*minJ][*minK] > rmap[j-1][k])
    {
        //North
        *minJ = j - 1;
        *minK = k;
    }

    if(k > 0 && rmap[*minJ][*minK] > rmap[j][k-1])
    {
        //West
        *minJ = j;
        *minK = k - 1;
    }

    if(k < W - 1 && rmap[*minJ][*minK]  > rmap[j][k+1])
    {
        //East
        *minJ = j;
        *minK = k+1;
    }

    if(j < H - 1 && rmap[*minJ][*minK] > rmap[j + 1][k])
    {
        //South
        *minJ = j + 1;
        *minK = k;
    }

}

char setNextChar(int j, int k, char *nextChar)
{
    char setChar ;
    int minJ = j, minK = k;
    getMinIndex(j, k, &minJ, &minK);

    if(j == minJ && k == minK)
    {
        if(db[j][k] == 0)
        {
            setChar = *nextChar;
            (*nextChar)++;
        }
        else
        {
            setChar = db[j][k];
        }
    }
    else if(db[minJ][minK] == 0)
    {
        setChar = setNextChar(minJ, minK, nextChar);
    }
    else
    {
        setChar = db[minJ][minK];
    }

    db[j][k] = setChar;
    return setChar;
}

int main(int argc, char* argv[])
{
    int TCount = 0; //Test case count
    if(argc == 3)
    {
        ifstream fin;
        ofstream fout;

        fin.open(argv[1]);
        fout.open(argv[2]);

        fin >> TCount;
    
        for(int i = 0 ; i < TCount; i++)
        {
            H = 0;
            W = 0;
            int  j = 0;
            int k = 0;
            char nextChar = 'a';
            fin >> H >> W;

            cout << "H = " << H  << "W= " << W << endl;
            for(j = 0; j < H; j++)
            {
                for(k = 0 ; k < W; k++)
                {
                    fin >> rmap[j][k];
                    db[j][k] = 0;
                }
            }
            
            
            for(j = 0; j < H ; j++)
            {
                for(k = 0; k < W; k++)
                {
                    if(db[j][k] == 0)
                    {
                        int minJ = j, minK = k;
                        getMinIndex(j, k, &minJ, & minK);
                        //cout << " Checking " << j << "x" << k << endl;
                        if(db[minJ][minK] != 0)
                        {
                            db[j][k] = db[minJ][minK];
                        }
                        else
                        {
                            db[j][k] = setNextChar(j, k, &nextChar);
                        }
                    }
                }
            }

            fout << "Case #" << i+1 << ":"<< endl;
            //output the map
            for(j = 0; j < H ; j++)
            {
                for(k = 0; k < W; k++)
                {
                    fout << db[j][k] << " ";
                }

                fout << endl;
            }
        }
        fin.close();
        fout.close();

    }
    else
    {
        cout << "Pass the test case file and output file" << endl;
    }
    return 0;
}
