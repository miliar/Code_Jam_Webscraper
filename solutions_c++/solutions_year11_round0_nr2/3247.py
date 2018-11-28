#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "B-large.in"
#define OUTPUT "b.out"
#define MAX 105

int T,o,c,n,length;
char combine[MAX][3],oppose[MAX][2],list[MAX],e;

bool isCombine(){
    for (int i=0;i<c;i++)
        if ((list[length-1] == combine[i][0] && e==combine[i][1])
            ||(list[length-1] == combine[i][1] && e==combine[i][0]))
            {
                list[length-1] =  combine[i][2];
                return true;
            }
    return false;
}

bool isClear(){
    for (int i=0;i<o;i++){
        if (oppose[i][0]== e){
            for (int j=0;j<length;j++)
                if (list[j] == oppose[i][1]){
                    length = 0;
                    return true;
                }
        }

        if (oppose[i][1]==e){
            for (int j=0;j<length;j++)
                if (list[j] == oppose[i][0]){
                    length = 0;
                    return true;
                }
        }
    }

    return false;
}

int main(){
    freopen(INPUT,"r",stdin);
    freopen(OUTPUT,"w",stdout);

    cin >> T;
    for (int task=1;task <= T; task ++){
        cin >> c;
        for (int i=0;i<c;i++){
            cin >> combine[i][0] >> combine[i][1] >> combine[i][2];
        }

        cin >> o;
        for (int i=0;i<o;i++){
            cin >> oppose[i][0] >> oppose[i][1];
        }

        cin >> n;

        length = 0;
        for (int i=0;i<n;i++){
            cin >> e;
            if (!isCombine()){
                if (!isClear()){
                    list[length++] = e;
                   // cerr << e;
                }
            }

        }
        //cerr << endl;

        cout << "Case #" << task << ": ";
        cout << "[";
        if (length > 0){
            for (int i=0;i<length-1;i++)
                cout << list[i]<<", ";
            cout << list[length-1];
        }
        cout << "]" <<endl;

    }

    fclose(stdin);
    fclose(stdout);
}
