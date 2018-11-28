#include<iostream>

using namespace std;

class train {
    public:
        int t;
        char pos, state;
        train(int t, char pos, char state):t(t), pos(pos), state(state) {}
        train() {}
        
        bool operator<(const train& t) const {
            if(this->t != t.t) return this->t < t.t;
            else return state == 'e';
        }
};

int parse(const string& buf) {
    int h = (buf[0]-'0')*10 + (buf[1]-'0');
    int m = (buf[3]-'0')*10 + (buf[4]-'0');
    return h*60+m;
}

int main() {
    int n;
    string buf;
    train tr[500];
    cin >> n;
    for(int c=1; c<=n; c++) {
        int t, na, nb;
        cin >> t >> na >> nb;
        
        train* ptr = tr;
        for(int i=0; i<na; i++) {
            cin >> buf;
            *ptr++ = train(parse(buf), 'A', 's');
            cin >> buf;
            *ptr++ = train(parse(buf)+t, 'A', 'e');
        }
        
        for(int i=0; i<nb; i++) {
            cin >> buf;
            *ptr++ = train(parse(buf), 'B', 's');
            cin >> buf;
            *ptr++ = train(parse(buf)+t, 'B', 'e');
        }
        
        sort(tr, ptr);
        
        int xa=0, xb=0;
        int a=0, b=0;
        for(train* p=tr; p<ptr; p++) {
            if(p->pos == 'A') {
                if(p->state == 's') {
                    if(a == 0) xa++;
                    else a--;
                }
                else {
                    b++;
                }
            }
            else {
                if(p->state == 's') {
                    if(b == 0) xb++;
                    else b--;
                }
                else {
                    a++;
                }
            }
        }
        
        cout << "Case #" << c << ": " << xa << ' ' << xb << endl;
    }
}
