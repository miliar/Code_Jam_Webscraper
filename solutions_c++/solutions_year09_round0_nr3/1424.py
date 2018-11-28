#include <iostream>
#include <string>
using namespace std;

int main(){
    string model = "welcome to code jam";
    int nc; cin >> nc;
    string s;
    getline(cin,s);
    for (int q = 1; q <= nc; q++){
        getline(cin,s);
        //cout << "s = " << s << endl;
        int quants[s.size()][model.size()];
        memset(quants,0,sizeof(quants));
        for (int i = 0; i < s.size(); i++){
            int n = 0;
            if (s[i] == 'w'){
               quants[i][0] = 1;
            } 
            else quants[i][0] = 0;
        }
        for (int i = 0; i < s.size(); i++){
            for (int j = 1; j < model.size(); j++){
                if (s[i] == model[j]){
                   for (int k = 0; k < i; k++){
                       quants[i][j]+=quants[k][j-1];
                       quants[i][j]%=10000;
                   }
                }
            }
        }
        int sum = 0;
        for (int i= 0; i < s.size();i++){
            sum+=quants[i][model.size()-1];
            sum%=10000;
        }
        printf("Case #%d: %04d\n",q,sum);
//        cout << "Case #" << q << ": " << sum << endl;
    }
}
