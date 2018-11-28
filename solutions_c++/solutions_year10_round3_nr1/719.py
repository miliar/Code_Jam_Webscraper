#include <cassert>
#include <utility>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Tree{

    Tree(int _start, int _stop){
        start=_start;
        stop=_stop;
        count=0;
        left=right=0;
        if (start!=stop){
            left = new Tree(start, (start+stop)/2);
            right= new Tree((start+stop)/2+1, stop);
        }
    }

    int start, stop, count;
    Tree *left, *right;
    
    void insert(int x){
        if ( x<start or x>stop )
            return;
        count++;
        if (start==stop)
            return;
        
        assert(left and right);

        left->insert(x);
        right->insert(x);
    }

    int find(int x,int y){
        if (x>stop or y<start)
            return 0;
        if (x<=start and y >=stop)
            return count;

        assert(start!=stop);

        return left->find(x,y) + right->find(x,y);

    }

    ~Tree(){
        if (left){
            delete left;
            delete right;
        }
    }

};

pair<int,int> a[1000];

int T, N;



int main(){
    

    scanf("%i", &T);
    
    for (int ttt=1; ttt<=T; ttt++){
        Tree tr(0,10000);
        int cnt=0;
        scanf("%i", &N);
        for (int i=0; i<N; i++){
            scanf("%d %d", &(a[i].first), &(a[i].second));
        }
        sort(a, a+N);
        
        for (int i=0; i<N; i++){
            cnt+=tr.find(a[i].second, 10001);
            tr.insert(a[i].second);
        }
        printf("Case #%i: %i\n", ttt, cnt); 
    }

}
