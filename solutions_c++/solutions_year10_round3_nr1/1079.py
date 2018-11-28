//#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

#define shoeb(x) sort(x.begin(),x.end())
#define pb push_back

void print_result(int cases );
void input(int N) ;
void calculate();
long long cnt = 0 ;

ifstream cin("a.in");
ofstream cout("a.out");
class point {
    public:
        int x;
        int y;
};

bool operator< ( point a, point b ) {
    if( a.x!=b.x)
        return a.x<b.x;

    if( a.y!=b.y)
        return a.y<b.y;

    return false;
}
bool intersect ( point &a, point & b);

vector<point> all_points;
int main(void) {

    int T , N;

    cin>>T;

    for ( int i = 0 ; i < T ; i ++ ) {
        all_points.clear();
        cin>>N;
        input(N);
        calculate();
        print_result(i+1);
    }

    return 0;
}

void input(int N) {
    point f;
    int a , b;
    for ( int i = 0 ; i < N ; i ++ ) {
        cin>>a>>b;
        f.x = a;
        f.y = b;
        all_points.pb(f);
    }
}

void calculate() {

    shoeb(all_points);
    cnt = 0;

    for ( int i = 0 ; i < all_points.size() ; i++ ) {
        for ( int j = i + 1 ; j < all_points.size() ; j ++ ) {
            if(intersect(all_points[i],all_points[j]))
                cnt ++;
        }
    }

}

void print_result(int cases ) {
    cout<<"Case #"<<cases<<": "<<cnt<<endl;
}

bool intersect ( point &a, point & b) {
    if(b.y<a.y)
        return true;

    return false;
}
