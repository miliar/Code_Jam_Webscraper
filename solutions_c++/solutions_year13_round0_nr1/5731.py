#include <iostream>

using namespace std;

int main()
{
    string matriz [4];
    int casos;
    cin>>casos;
    string temp;
    char car;
    int cont;
    bool endedGame;
    bool ganador;

    for(int l=1;l<=casos;++l)
    {
        endedGame = true;
        ganador = false;
        for(int j=0;j<4;++j)
        cin>>matriz[j];

        for(int i=0;i<4 && !ganador;++i)
        {
            for(int j=0;j<4 && !ganador;++j)
            {
                car = matriz[i][j];
                if(car == '.')
                endedGame=false;
                if(j == 0 && car!='.') //reviso hacia la derecha
                {
                    cont = 1;
                    if(car == 'T')
                    {
                       if(matriz[i][j+1]!='.')
                       car = matriz[i][j+1];

                    }

                    for(int k = 1; k<4; k++)
                    {
                        if(matriz[i][k]=='T' || matriz[i][k]==car)
                            cont++;
                        else
                          {
                            break;
                          }
                    }
                    if(cont==4)
                        {
                            ganador=true;
                            break;
                        }

                }
                if(i == 0 && car!='.') //reviso hacia abajo
                {
                    cont = 1;
                    if(car == 'T')
                    {
                       if(matriz[i+1][j]!='.')
                       car = matriz[i+1][j];

                    }

                    for(int k = 1; k<4; k++)
                    {
                        if(matriz[k][j]=='T' || matriz[k][j]==car)
                            cont++;
                        else
                          {
                            break;
                          }
                    }
                    if(cont==4)
                        {
                            ganador=true;
                            break;
                        }

                }
                if(i==0 && j==0 && car!='.')
                {
                    cont = 1;
                    if(car == 'T')
                    {

                        if(matriz[i+1][j+1]!='.')
                       car = matriz[i+1][j+1];

                    }

                    for(int k = 1; k<4; k++)
                    {
                        if(matriz[k][k]=='T' || matriz[k][k]==car)
                            cont++;
                        else
                        {
                            break;
                        }
                    }
                    if(cont==4)
                    {
                        ganador=true;
                        break;
                    }
                }
                if(i==3 && j==0 && car!='.')
                {
                    //cout<<"Estoy aqui"<<endl;
                    cont = 1;
                    if(car == 'T')
                    {
                        if(matriz[i-1][j+1]!='.')
                       car = matriz[i-1][j+1];

                    }
                    //cout<<"car: "<<car<<endl;

                    for(int k = 1; k<4; k++)
                    {
                        //cout<<"revisando.. "<<matriz[3-k][k] << " == "<<car<<endl;
                        if(matriz[3-k][k]=='T' || matriz[3-k][k]==car)
                            cont++;
                        else
                        {
                            break;
                        }
                    }
                    if(cont==4)
                    {
                        ganador=true;
                        break;
                    }
                }
            }
        }

        cout<<"Case #"<<l<<": ";

        if(ganador)
        {
            cout<<car<<" won"<<endl;
        }
        else
        {
            if(endedGame)
                cout<<"Draw"<<endl;
            else
               cout<<"Game has not completed"<<endl;
        }

    }


    return 0;
}
