#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

char needle[] = "welcome to code jam";

int main(){
    int N;
    cin >> N;
    cin.ignore();
    short amount[501][19];
    for(int x=1;x<=N;x++){
        string curr;
        getline(cin,curr);
        short ans=0;
        for(int i=0;i<curr.size();i++){
            if(curr[i]=='w') amount[i][0] = 1;
            else amount[i][0] = 0;
            for(int j=1;j<19;j++){
                amount[i][j] = 0;
                if(curr[i] == needle[j]){
                    for(int k=0;k<i;k++){
                        amount[i][j] += amount[k][j-1];
                        amount[i][j] %= 10000;
                    }
                }
            }
            ans+=amount[i][18];
            ans%=10000;
        }
        cout << "Case #" << x << ": " << setfill('0') << setw(4) << ans << endl;
    }
}
