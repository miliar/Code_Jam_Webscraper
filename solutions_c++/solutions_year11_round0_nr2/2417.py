#include<iostream>
#include<vector>
#include<cassert>

using namespace std;

int combine[30][30];
vector <pair<int, int> > oppose;
vector <int> response;



void init() {
    for(int i = 0; i < 30 ; i++)
        for(int j = 0; j < 30 ; j++)
            combine[i][j] = -1;
    oppose.clear();
    response.clear();
}

int ind(char c) {
    assert(c>= 'A' && c<= 'Z');
    return c - 'A';
}

bool combine_strings() {
    if(combine[response[response.size()-1]][response[response.size()-2]] != -1) {
        int t = combine[response[response.size()-1]][response[response.size()-2]];
        response.pop_back();response.pop_back();
        response.push_back(t);
        return true;
    }
    return false;
}

void oppose_strings() {
    bool opposed = false;
    for(int i = 0 ; i < oppose.size() and !opposed; i++) {
        int x = oppose[i].first, y = oppose[i].second;
        if(x == response[response.size() - 1]){
            if( find(response.begin(), response.end(), y) != response.end()){
                opposed = true;
            }
        }
        if(y == response[response.size() - 1]) {
            if( find(response.begin(), response.end(), x) != response.end()){
                opposed = true;
            }
        }
    }
    if(opposed) response.clear();
}

void print_response() {
    for(int i = 0; i<response.size();i++)
        cout<<(char)(response[i] + 'A');
    cout<<endl;
}

int main() {

    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++) {

        init();
        
        int C;
        scanf("%d ", &C);
        for(int i = 0; i < C ; i++) {
            char a,b,c;
            scanf("%c%c%c ",&a,&b,&c);
            combine[ind(a)][ind(b)] = ind(c);
            combine[ind(b)][ind(a)] = ind(c);
        }
        
        int D;
        scanf("%d ", &D);
        for(int i = 0; i < D; i++) {
            char a, b;
            scanf("%c%c ", &a, &b);
            pair<int,int> temp(ind(a), ind(b));
            oppose.push_back(temp);
        }
        
        int L;
        scanf("%d ", &L);
        
        for(int i = 0; i < L; i++) {
            char c;
            scanf("%c", &c);
            
            response.push_back(ind(c));
            if(response.size() == 1) continue;
            if(!combine_strings()) {
                oppose_strings();
            }
            //print_response();
        }
        cout<<"Case #"<<tt<<": [";
        for(int i = 0; i < response.size(); i++) {
            char c = 'A' + response[i];
            cout<<c;
            if(i != response.size() - 1) cout<<", ";
        }
        cout<<"]"<<endl;
    }
    
}
