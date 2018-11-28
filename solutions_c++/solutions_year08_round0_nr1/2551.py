#include<fstream>
#include<map>
using namespace std;

long Q, S;
int n_cases;

string s_arr[101];
long shortest[101];
map<string, int> m;
inline long min_not_index(int index);

int main(){
    //read in
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    in >> n_cases;
    string curq;
    for(int curcase=0; curcase<n_cases; curcase++){
        in >> S;
        getline(in, curq);
        for(int i=0; i<S; i++){
            getline(in, s_arr[i]);
            shortest[i] = 0;
            m[s_arr[i]]= i; //reverse association
        }
        in >> Q;
        long best=0;
        if(Q>0){
            int cur, prev;
            getline(in, curq);
            getline(in, curq);
            cur = m[curq];
            for(int i=1;i<Q; i++){
                getline(in, curq);
                prev = cur;
                cur = m[curq];
                shortest[prev] = 1+min_not_index(prev);
            }
            shortest[cur] = 1+min_not_index(cur);
            best = min_not_index(-1);
        }else best = 0;
        out << "Case #" << curcase+1 << ": " << best << endl;
    }   
    
}

inline long min_not_index(int index){
    long minv = shortest[0];
    if(index==0)minv = shortest[1];
    for(int i=0; i<S; i++)if(shortest[i]<minv && i!=index)minv=shortest[i];
    return minv;
}
