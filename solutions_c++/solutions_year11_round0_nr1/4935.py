#include <iostream>
#include <vector>

using namespace std;



int main(){
    int t, time, tmp, n, k;
    int pos_o = 1, pos_b = 1, offset_o = 0, offset_b = 0, off;
    char c;

    cin >> t;

    for( k = 1; k <= t; ++k ){
        pos_o = 1; pos_b = 1; offset_o = 0; offset_b = 0; off=0;
        bool b_done = false, o_done = false;

        vector<int> bt_o;
        vector<int> bt_b;
        vector<int> que;
         bt_o.clear();
        bt_b.clear();
        que.clear();
        time = 0;

        cin >> n;
        for(int i = 1; i <= n; ++i){
            cin >> c >> tmp;

            if( c == 'O' ){
                bt_o.push_back( tmp );
                que.push_back(1);
            }else{
                bt_b.push_back( tmp );
                que.push_back(2);
            }
        }

        if( offset_b >= bt_b.size() )
            b_done = true;
        if( offset_o >= bt_o.size() )
            o_done = true;

        while( true ){
            time++;
            //cout << "Czas: " << time << "\n";
            bool not_yet = true;
            //if( offset_o > bt_o.count() && offset_b > bt_b.count() )
            //    break;

            /*if( offset_o <= bt_o.count() && pos_o == bt_o[ offset_o ] ){
                offset_b++;
            }else{

            }*/
            if( !o_done)
            if( !o_done && (bt_o[offset_o] == pos_o )){
                if(que[off] == 1){
                    offset_o++;
                    off++;
                    not_yet = false;
                    //cout << "O naciska przycisk\n";
                    if( offset_o >= bt_o.size() )
                        o_done = true;

                }
                //continue;
            }else if (bt_o[offset_o] > pos_o){
                //cout << "O przesuwa sie do przodu\n";
                pos_o++;
            } else{
                 //cout << "O przesuwa sie do tylu\n";
                pos_o--;
            }

            if( !b_done)
            if( !b_done && (bt_b[offset_b] == pos_b )){
                if(que[off] == 2){
                    if(!not_yet) continue;
                    //cout << "B naciska przycisk\n";
                    offset_b++;
                    off++;

                    if( offset_b >= bt_b.size() )
                        b_done = true;
                }
                //continue;
            }else if (bt_b[offset_b] > pos_b){
                //cout << "B przesuwa sie do przodu\n";
                pos_b++;
            } else{
                 //cout << "B przesuwa sie do tylu\n";
                pos_b--;
            }

            if( b_done && o_done )
                break;

           // time++;
        }

        cout << "Case #" << k << ": " << time << "\n";

    }

    return 0;
}
