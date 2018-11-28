#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void checkResult(char* file)
{
    ifstream fileIn(file);
    ofstream fileOu("OutputResult.txt");

    if(fileOu && fileIn)
    {
        int T, i(1), j(0);
        char game[4][4];
        fileIn >> T;

        string ligne;
        while(getline(fileIn, ligne))
        {
            if(ligne[0] == '.' || ligne[0] == 'T' || ligne[0] == 'O' || ligne[0] == 'X')
            {
                game[j][0] = ligne[0];
                game[j][1] = ligne[1];
                game[j][2] = ligne[2];
                game[j][3] = ligne[3];
                j++;
            }
            if(j == 4)
            {
                bool rep = false;
                if(!rep)
                {
                    for(int k(0); k<=3; k++)
                    {
                        if(game[k][0] != '.' && game[k][1] != '.' && game[k][2] != '.' && game[k][3] != '.')
                        {
                            if(game[k][0] == 'T')
                            {
                                if(game[k][1] == game[k][2] && game[k][1] == game[k][3])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][1] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[k][1] == 'T')
                            {
                                if(game[k][0] == game[k][2] && game[k][0] == game[k][3])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][0] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[k][2] == 'T')
                            {
                                if(game[k][0] == game[k][1] && game[k][0] == game[k][3])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][0] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[k][3] == 'T')
                            {
                                if(game[k][0] == game[k][1] && game[k][0] == game[k][2])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][0] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else
                            {
                                if(game[k][0] == game[k][1] && game[k][0] == game[k][2] && game[k][0] == game[k][3])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][0] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                        }
                    }
                }
                if(!rep)
                {
                    for(int k(0); k<=3; k++)
                    {
                        if(game[0][k] != '.' && game[1][k] != '.' && game[2][k] != '.' && game[3][k] != '.')
                        {
                            if(game[0][k] == 'T')
                            {
                                if(game[1][k] == game[2][k] && game[1][k] == game[3][k])
                                {
                                    fileOu << "Case #" << i << ": " << game[k][1] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[1][k] == 'T')
                            {
                                if(game[0][k] == game[2][k] && game[0][k] == game[3][k])
                                {
                                    fileOu << "Case #" << i << ": " << game[0][k] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[2][k] == 'T')
                            {
                                if(game[0][k] == game[1][k] && game[0][k] == game[3][k])
                                {
                                    fileOu << "Case #" << i << ": " << game[0][k] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else if(game[3][k] == 'T')
                            {
                                if(game[0][k] == game[1][k] && game[0][k] == game[2][k])
                                {
                                    fileOu << "Case #" << i << ": " << game[0][k] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                            else
                            {
                                if(game[0][k] == game[1][k] && game[0][k] == game[2][k] && game[0][k] == game[3][k])
                                {
                                    fileOu << "Case #" << i << ": " << game[0][k] << " won" << endl;
                                    rep = true;
                                    break;
                                }
                            }
                        }
                    }
                }
                if(!rep)
                {
                    if(game[0][0] != '.' && game[1][1] != '.' && game[2][2] != '.' && game[3][3] != '.')
                    {
                        if(game[0][0] == 'T')
                        {
                            if(game[1][1] == game[2][2] && game[1][1] == game[3][3])
                            {
                                fileOu << "Case #" << i << ": " << game[1][1] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[1][1] == 'T')
                        {
                            if(game[0][0] == game[2][2] && game[0][0] == game[3][3])
                            {
                                fileOu << "Case #" << i << ": " << game[0][0] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[2][2] == 'T')
                        {
                            if(game[0][0] == game[1][1] && game[0][0] == game[3][3])
                            {
                                fileOu << "Case #" << i << ": " << game[0][0] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[3][3] == 'T')
                        {
                            if(game[0][0] == game[1][1] && game[0][0] == game[2][2])
                            {
                                fileOu << "Case #" << i << ": " << game[0][0] << " won" << endl;
                                rep = true;
                            }
                        }
                        else
                        {
                            if(game[0][0] == game[1][1] && game[0][0] == game[2][2] && game[0][0] == game[3][3])
                            {
                                fileOu << "Case #" << i << ": " << game[0][0] << " won" << endl;
                                rep = true;
                            }
                        }
                    }
                }
                if(!rep)
                {
                    if(game[0][3] != '.' && game[1][2] != '.' && game[2][1] != '.' && game[3][0] != '.')
                    {
                        if(game[0][3] == 'T')
                        {
                            if(game[1][2] == game[2][1] && game[1][2] == game[3][0])
                            {
                                fileOu << "Case #" << i << ": " << game[1][2] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[1][2] == 'T')
                        {
                            if(game[0][3] == game[2][1] && game[0][0] == game[3][0])
                            {
                                fileOu << "Case #" << i << ": " << game[0][3] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[2][1] == 'T')
                        {
                            if(game[0][3] == game[1][2] && game[0][0] == game[3][0])
                            {
                                fileOu << "Case #" << i << ": " << game[0][3] << " won" << endl;
                                rep = true;
                            }
                        }
                        else if(game[3][0] == 'T')
                        {
                            if(game[0][3] == game[1][2] && game[0][3] == game[2][1])
                            {
                                fileOu << "Case #" << i << ": " << game[0][3] << " won" << endl;
                                rep = true;
                            }
                        }
                        else
                        {
                            if(game[0][3] == game[1][2] && game[0][3] == game[2][1] && game[0][3] == game[3][1])
                            {
                                fileOu << "Case #" << i << ": " << game[0][3] << " won" << endl;
                                rep = true;
                            }
                        }
                    }
                }
                if(!rep)
                {
                    for(int k(0); k<=3; k++)
                    {
                        for(int l(0); l<=3; l++)
                        {
                            //cout << game[k][l];
                            if(game[k][l] == '.')
                            {
                                fileOu << "Case #" << i << ": Game has not completed" << endl;
                                rep = true;
                                break;
                            }
                        }
                        //cout << endl;
                        if(rep)
                        {
                            break;
                        }
                    }
                }
                if(!rep)
                {
                    fileOu << "Case #" << i << ": Draw" << endl;
                    rep = true;
                }
                j = 0;
                i++;
            }
        }
    }
    else
    {
        cout << "Fichier non ouvert. Fin du programme" << endl;
    }
}

int main(int argc, char** argv)
{
    checkResult(argv[1]);
    return 0;
}
