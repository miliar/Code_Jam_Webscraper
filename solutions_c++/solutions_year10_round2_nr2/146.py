#include<iostream>
#include<queue>
#include<vector>

using namespace std;

struct Chick{
    double speed;
    double pos;
};

struct State{
    vector<Chick> chicks;
    int swaps;
};

    

int main(){
    int cases;
    std::cin>>cases;
    for(int cno = 1;cno<=cases;cno++)
    {
        int n,k,b,t;
        std::cin>>n>>k>>b>>t;
        vector<Chick> chicks;
        for(int i=0;i<n;i++){
            Chick c;
            std::cin>>c.pos>>c.speed;
        }

        State start;
        start.chicks = chicks;
        start.swaps=0;

        std::queue<State> q;
        q.push(start);
        while(q.size()){
            State s = q.top();
            q.pop();
        }
    }
}
