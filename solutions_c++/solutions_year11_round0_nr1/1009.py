#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>
#include <queue>

using namespace std;

struct mov {
    int pos;
    int quien;
};

int main(void)
{
    queue<mov*> lista;
    int casos;
    int cuantos;
    int c = 1;
    char temtem;

    cin >> casos;

    while(casos){
        cin >> cuantos;

        while(cuantos){
            mov *temp = new mov;

            cin >> temtem;

            if (temtem == 'O')
                temp->quien = 0;
            else
                temp->quien = 1;

            cin >> temp->pos;
            lista.push(temp);

            cuantos--;
        }

        int pos[2] = {1,1};
        int tiempo[2] = {0,0};

        int total = lista.front()->pos;
        int ant = lista.front()->quien;
        pos[ant] = total;
        tiempo[ant] = total;

        lista.pop();

        while(!lista.empty()){
            mov *temp = lista.front();
            lista.pop();
            
            if(temp->quien == ant){
                total += abs(temp->pos - pos[ant]) + 1;
                pos[ant] = temp->pos;
                tiempo[ant] = total;
            }
            else{
                int diff = abs(pos[temp->quien]-temp->pos);
                if(tiempo[ant]-tiempo[temp->quien] >= diff)
                    total++;
                else{
                    //cout << diff << ":" << tiempo[ant]-tiempo[temp->quien] << endl;
                    diff = diff - (tiempo[ant]-tiempo[temp->quien]) + 1;
                    //cout << diff << endl;
                    total += diff;
                }

                ant = temp->quien;
                tiempo[ant] = total;
                pos[ant] = temp->pos;
            }
            delete temp;
        } 
        cout << "Case #" << c << ": " <<  total << endl;
        casos--; 
        c++;
    }

    return 0;
}
