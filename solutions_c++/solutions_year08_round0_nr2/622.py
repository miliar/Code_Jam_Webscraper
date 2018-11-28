#include <cstdio>
#include <queue>
using namespace std;

FILE *in = fopen("blarge.in", "r");
FILE *out = fopen("blarge.out", "w");

int n, t, na, nb;

int readtime(){
    int hh, mm;
    fscanf(in, "%d:%d", &hh, &mm);
    return 60 * hh + mm;
}

pair<int, int> solve(){
    fscanf(in, "%d", &t);
    fscanf(in, "%d %d", &na, &nb);   

    priority_queue< pair< pair<int, int>, int> > rides;
    priority_queue< int > atA, atB;
    
    for(int i = 0; i < na; i++){
        pair< pair<int, int>, int> times;
        times.first.first  = -readtime();
        times.first.second = -readtime();
        times.second       = 0; 
        //printf("A -> B, %d to %d\n", times.first.first, times.first.second);
        rides.push(times);
    }

    for(int i = 0; i < nb; i++){
        pair< pair<int, int>, int> times;
        times.first.first  = -readtime();
        times.first.second = -readtime();
        times.second       = -1; 
        //printf("B -> A, %d to %d\n", times.first.first, times.first.second);
        rides.push(times);
    }

    pair<int, int> ans = make_pair(0, 0);
    while(!rides.empty()){
        int timeFrom = -rides.top().first.first;
        int timeTo   = -rides.top().first.second;
        int type     = rides.top().second;
        rides.pop();
        if(type == 0){
            if(atA.size() == 0){
                ans.first++;
            } else {
                int nxtA = -atA.top();
                if(nxtA + t <= timeFrom){
                    atA.pop();
                } else {
                    ans.first++;
                }
            }
            atB.push(-timeTo);
        } else {
            if(atB.size() == 0){
                ans.second++;
            } else {
                int nxtB = -atB.top();
                if(nxtB + t <= timeFrom){
                    atB.pop();
                } else {
                    ans.second++;
                }
            }
            atA.push(-timeTo);
        }
    }

    return ans;   
}

int main(){
    fscanf(in, "%d", &n);
    for(int c = 1; c <= n; c++){
        pair<int, int> ans = solve();
        fprintf(out, "Case #%d: %d %d\n", c, ans.first, ans.second);
 
   }
    return 0;
}

