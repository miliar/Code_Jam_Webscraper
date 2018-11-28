#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream file("C-small-attempt0.in");
    int casos, R, k, N, c = 1, total, pos, board;
    file >> casos;
    while(casos--){
        pos = total = 0;
        file >> R >> k >> N;
        int arr[N];
        for(int i = 0; i < N; i++) file >> arr[i];
        while(R--){
            int ya[N];
            for(int i = 0; i < N; i++) ya[i] = 0;
            board = 0;
            while(1){
                if(board + arr[pos%N] <= k && ya[pos%N] != 1){
                    total += arr[pos%N];     
                    board += arr[pos%N]; 
                    ya[pos%N] = 1;
                    pos++;
                } else {
                    break;   
                }           
            }
        }
        cout << "Case #" << (c++) << ": " << total << endl;
    }
    file.close();
    system("PAUSE");
    return 0;
}
