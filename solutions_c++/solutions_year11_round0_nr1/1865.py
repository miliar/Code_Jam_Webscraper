#include <iostream>
#include <queue>

using namespace std;

queue<char> need;
queue<int> need2;

queue<char> bneed;
queue<int> bneed2;

queue<char> oneed;
queue<int> oneed2;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N;
        cin >> N;
        for(int i = 0; i < N ; i++){
            char a; int b;
            cin >> a >> b;
            //cout <<"in " << a << " " << b<<endl;
            need.push(a);
            need2.push(b);
            if(a == 'O'){
                oneed.push(a);
                oneed2.push(b);
            }else{
                bneed.push(a);
                bneed2.push(b);
            }
        }

        int poso = 1;
        int posb = 1;
        int res = 0;
        int neednext = need2.front(); need2.pop();
        int needtype = need.front(); need.pop();

        int desto = 1;
        if(!oneed2.empty()){
        desto = oneed2.front(); oneed2.pop();
        }
        
        int destb = 1;
        if(!bneed2.empty()){
        destb = bneed2.front(); bneed2.pop();
        }
        while(1){
            //cout << poso << " " << posb << " " << oneed2.size() << " " << bneed2.size() << endl;
            if(neednext == -1){
                if(need.empty()){
                    break;
                }
                neednext = need2.front(); need2.pop();
                needtype = need.front(); need.pop();
                //cout << " getting new target" << endl;
            }
            if(poso < desto){
                poso++;
            }else if(poso > desto){
                poso--;
            }else{
                if(needtype == 'O'){
                //cout << "O pressing" << endl;
                    neednext = -1;
                    needtype = -1;
                    if(!oneed2.empty()){
                        desto = oneed2.front(); oneed2.pop();
                    }
                }
            }
            if(posb < destb){
                posb++;
            }else if(posb > destb){
                posb--;
            }else{
                if(needtype == 'B'){
                //cout << "B pressing" << endl;
                    neednext = -1;
                    needtype = -1;
                    if(!bneed2.empty()){
                        destb = bneed2.front(); bneed2.pop();
                    }
                }
            }
            res++;
//            break;
        }
        cout << "Case #" << t << ": " << res << endl;
    }
}
