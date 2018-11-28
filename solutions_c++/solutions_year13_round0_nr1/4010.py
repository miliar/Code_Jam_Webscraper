#include <fstream>
#include <string>
#include <iostream>


using namespace std;

void izracunaj(char arr[4][4] , int broj)
{
    ofstream ofs;
    ofs.open("output1.out", fstream::app | fstream::out);
    string result = "";
    bool draw = true;
    int i = 0; int j = 0;
    int Ol = 0;
    int Xl = 0;
    for(i=0;i<4;i++)
    {
        Ol= 0;
        Xl = 0;
        for(j=0;j<4;j++)
        {
            if(arr[i][j] == 'X')
            {
                Xl++;
            }
            else if(arr[i][j] == 'O')
            {
                Ol++;
            }
            else if(arr[i][j] == 'T')
            {
                Xl++;
                Ol++;
            }
            else
            {
                draw=false;
                break;
            }
        }
        if(Ol==4)
        {
            result = "O won";
            break;
        }
        if(Xl == 4)
        {
            result = "X won";
            break;
        }
    }

    if(result.compare("")==0)
    {
        for(j=0;j<4;j++)
        {
            Ol= 0;
            Xl = 0;
            for(i=0;i<4;i++)
            {
                if(arr[i][j] == 'X')
                {
                    Xl++;
                }
                else if(arr[i][j] == 'O')
                {
                    Ol++;
                }
                else if(arr[i][j] == 'T')
                {
                    Xl++;
                    Ol++;
                }
                else
                {
                    break;
                }
            }
            if(Ol==4)
            {
                result = "O won";
                break;
            }
            if(Xl == 4)
            {
                result = "X won";
                break;
            }
        }
    }

    if(result.compare("")==0)
    {
        Ol= 0;
        Xl = 0;
        for(i =0; i<4; i++)
        {
            if(arr[i][i] == 'X')
            {
                Xl++;
            }
            else if(arr[i][i] == 'O')
            {
                Ol++;
            }
            else if(arr[i][i] == 'T')
            {
                Xl++;
                Ol++;
            }
            else
            {
                break;
            }
        }
        if(Ol==4)
        {
            result = "O won";
        }
        if(Xl == 4)
        {
            result = "X won";
        }
    }

    if(result.compare("")==0)
    {
        Ol= 0;
        Xl = 0;
        for(i =0; i<4; i++)
        {
            if(arr[i][3-i] == 'X')
            {
                Xl++;
            }
            else if(arr[i][3-i] == 'O')
            {
                Ol++;
            }
            else if(arr[i][3-i] == 'T')
            {
                Xl++;
                Ol++;
            }
            else
            {
                break;
            }
        }
        if(Ol == 4)
        {
            result = "O won";
        }
        if(Xl == 4)
        {
            result = "X won";
        }
    }

    if(result.compare("")==0 && draw)
    {
        result = "Draw";
    }
    else if(result.compare("")==0)
    {
        result = "Game has not completed";
    }

    ofs<<"Case #"<<broj<<": " << result<<endl;
    ofs.close();
}

int main()
{
    ifstream ifs("A-large.in");
    int broj_testa;
    string line;
    char polje[4][4];
    int i, j;
    if(ifs.is_open())
    {
        getline(ifs, line);
        i = 0; j=0; broj_testa = 1;
        int Od = 0; int Oo = 0; int Ol = 0;
        int Xd = 0; int Xo = 0; int Xl = 0;
        bool nijeDraw = true;
        while(ifs.good())
        {
            getline(ifs, line);
            for(j=0; j<4;j++)
            {
                char znak = line[j];
                polje[i][j] = znak;
            }
            i++;
            if(i==4)
            {
                izracunaj(polje, broj_testa);
                broj_testa++;
                i=0;
                getline(ifs, line);
            }
        }
    }
    ifs.close();
}
