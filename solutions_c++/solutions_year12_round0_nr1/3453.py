/*
 * =====================================================================================
 *
 * Nazwa pliku:  	A.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		15.04.2012 00:13:49
 *
 * =====================================================================================
 */
#include<iostream>

using namespace std;

char tab[2][200];
int map[26]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};

int main()
{
    int N;
    cin >> N;
    cin.ignore();
    for (int j = 1; j<=N; j++)
    {
        cin.getline(tab[0], 200);
        //cout << tab[0] << endl;
        for (int i  = 0; tab[0][i]!='\0'; i++)
            if(tab[0][i]>='a' && tab[0][i]<='z')
                tab[0][i]=map[tab[0][i]-'a'];
        cout << "Case #" << j << ": " << tab[0] << endl;
    }
    return 0;
}
