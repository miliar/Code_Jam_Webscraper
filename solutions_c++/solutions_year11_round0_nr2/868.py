#include <iostream>
#include <string>
using namespace std;

int main(){

    int T, cases;

    cin >> T;
    cases = T;
    while(T--){

        int c, d, n;
        string cc[100], dd[100], nn;  

        cin >> c;
        for(int i = 0; i < c; i++)
            cin >> cc[i];
             
        cin >> d;
        for(int i = 0; i < d; i++)
            cin >> dd[i];


        cin >> n;
        cin >> nn;

        char list[200];
            
        int len = 0;
        for(int i = 0; i < n; i++){

            list[len++] = nn[i];

            if(len > 1){

                bool match = false;
                for(int num = 0; num < c; num++){
                    string str = cc[num];
                    if((list[len-1] == str[0] && list[len-2] == str[1]) || (list[len-1] == str[1] && list[len-2] == str[0])){
                         len--;
                         list[len-1] = str[2];
                         match = true;
                         break;
                    }
                }


                if(match)
                    continue;

                for(int num = 0; num < d; num++){
                    string str = dd[num];
                    bool clean = false;
                    if((list[len-1] == str[0]) || (list[len-1] == str[1])){
                         
                        char opp = (list[len-1] == str[0])?str[1]:str[0];

                        for(int m = 0; m < len-1; m++)
                          if(list[m] == opp){
                            len = 0;
                            clean = true;
                            break;
                          }
                    }
                    if(clean)
                        break;
                }


            }
            
        } 


        cout << "Case #" << (cases-T) << ": [";
        for(int i = 0; i < len; i++){
            if(i)
                cout << ", ";
            cout << list[i];
        }

        cout << "]\n";
    }

    return 0;
}
