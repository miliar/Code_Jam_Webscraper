#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void){
        int t;
        freopen("input.in","r", stdin);
        freopen("output.out","w", stdout);
        cin >> t;
        string str = "";
       // getline(cin, str);
        int n, s, pz;


        for (int i = 0; i < t; i++){
                cin >> n >> s >> pz;
                int k = 0;
                for (int j = 0, a; j < n; j++){
                        cin >> a;
                        for (int p = pz; p <= 10; p++){
                                if (pz == 0) {k++; break;}
                        if ((p + p + p) == a){   k++; break;}
                        else
                                if ((p+1 + p + p+1) == a){ k++;  break;}
                                else
                                if ((p+1 + p + p) == a){ k++; break;}
                                else
                                if ((p-1 + p + p) == a) {k++;  break;}
                                else if ((p-1 + p - 1 + p) == a){ k++;  break;}
                                else if ((p-1 + p + p) == a){ k++;  break;}
                                else
                                if (s > 0){
                                if ((p-2)>= 0)
                                        if ((p - 2 + p - 2 + p) == a){
                                                k++;
                                                s--;
                                                break;
                                        }
                                        else
                                        if ((p - 2 + p + p) == a){
                                                k++;
                                                s--;
                                                break;
                                        }
                                        else
                                        if ((p - 2 + p - 1 + p) == a){
                                                k++;
                                                s--;
                                                break;
                                        }
                                }
                        }
                }
               cout <<"Case #" << i+1<<": " << k << endl;

        }
        

        fclose(stdin);
        fclose(stdout);

return 0;
}


