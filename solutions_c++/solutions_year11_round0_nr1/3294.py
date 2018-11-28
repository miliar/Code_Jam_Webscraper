#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv){
	int t, n, k, i;
	int b_pos, o_pos, b_nxt, o_nxt, time;
	int seq_i[105];
	char seq_c[105];
	bool pressed;

	ofstream salida("A.out.txt");
	cout.rdbuf(salida.rdbuf());

	cin >> t;
	for(k=1; k<=t; k++){
        cin >> n;

        for(i=0; i<n; i++){
            cin >> seq_c[i] >> seq_i[i];
        }

        b_pos = o_pos = 1;
        b_nxt = o_nxt = n;
        time = 0;

        for(i=0; i<n; i++){
            if(seq_c[i] == 'B'){
                b_nxt = i;
                break;
            }
        }

        for(i=0; i<n; i++){
            if(seq_c[i] == 'O'){
                o_nxt = i;
                break;
            }
        }

        while(b_nxt < n || o_nxt < n){
            pressed = false;

            if(o_pos != seq_i[o_nxt]){
                //mover
                if(o_pos < seq_i[o_nxt]) o_pos ++;
                else o_pos --;
            } else{
                //presionar
                if(o_nxt < b_nxt && !pressed){
                    for(i=o_nxt+1; i<n; i++){
                        if(seq_c[i] == 'O'){
                            o_nxt = i;
                            break;
                        }
                    }
                    if(i==n) o_nxt = n;
                    pressed = true;
                }
            }

            if(b_pos != seq_i[b_nxt]){
                //mover
                if(b_pos < seq_i[b_nxt]) b_pos ++;
                else b_pos --;
            } else{
                //presionar
                if(b_nxt < o_nxt && !pressed){
                    for(i=b_nxt+1; i<n; i++){
                        if(seq_c[i] == 'B'){
                            b_nxt = i;
                            break;
                        }
                    }
                    if(i==n) b_nxt = n;
                    pressed = true;
                }
            }

            time ++;
        }

        cout << "Case #" << k << ": " << time << endl;
	}

	return 0;
}
