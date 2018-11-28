#include <cstdlib>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int rel[105];
bool used[105];
int nCell, nRel;

int foo() {
    for(int a=0; a<nCell; a++) used[a] = false;
    int score = 0;
    for(int a=0; a<nRel; a++) {
        used[rel[a]]= true;
        for(int b=rel[a]+1; b<nCell&&!used[b]; b++,score++);
        for(int b=rel[a]-1; b>=0&&!used[b]; b--,score++);
    }
    return score;
}

int main() {
    int nCase;
    cin>>nCase;
    for(int n=1; n<=nCase; n++) {
        cout<<"Case #"<<n<<": ";
        cin>>nCell>>nRel;
        for(int a=0; a<nRel; a++) {
            cin>>rel[a];
            rel[a]--;
            used[a] = false;
        }
        int win = foo();
        while(next_permutation(rel,rel+nRel)) {
            int score = foo();
            if(score<win) win = score;
        }
        cout<<win<<endl;
    }
    return 0;
}
