#include <iostream>

using namespace std;

int main()
{
    FILE *input = fopen("C-small-attempt0.in","r");

    FILE *output = fopen("output.out","w");

    int cases;
    fscanf(input, "%d", &cases);

    for (int i=0; i<cases; i++) {
        int voltas, maxcap, groups;
        fscanf(input, "%d %d %d", &voltas, &maxcap, &groups);
        cout<<"voltas:"<<voltas<<" maxcap:"<<maxcap<<" groups:"<<groups<<endl;

        int group[groups];

        for (int k=0; k<groups; k++){
            fscanf(input, "%d", &group[k]);
        }

        int money = 0;
        int currenttrack = 0;
        int g = 0;
        bool full = false;
        for (int k=0; k<voltas; k++){

            for (int j=0;j<groups;j++) {
                if (!full){
                    //cout<<group[j]<<".";
                    if(currenttrack+group[g] <= maxcap){
                        currenttrack = currenttrack+group[g];
                        money = money + group[g];
                        g++;
                    } else {
                        full = true;
                        //g--;
                        int aux = 0;
                        for (int l=0; l<g; l++){
                            aux = group[0];
                            for (int m=0; m<groups-1; m++){
                                group[m] = group[m+1];
                            }
                            group[groups-1] = aux;
                        }
                    }

                }
            }
            cout << endl;

            /*while(!full && g<groups){

                if (){

                    currenttrack+=group[g];
                    money += group[g];

                    int aux = group[0];
                    for(int j=0;j<groups-1;j++){
                        group[j] = group[j+1];
                    }
                    group[groups-1] = aux;

                    g++;
                } else {
                    full = true;
                }
            }*/
            g = 0;
            full = false;
            currenttrack = 0;
        }
        cout<<"Money:"<<money<<endl<<endl;
        fprintf(output, "Case #%d: %d\n", i+1, money);
    }

    fclose(input);
    fclose(output);

    return 0;
}
