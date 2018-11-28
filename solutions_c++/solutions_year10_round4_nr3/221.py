////////////////////////////////////////////////////
//              ���鼯ģ��(UFS) v1.2              //
////////////////////////////////////////////////////
//                                                //
// 1. SZ:         ���鼯���Ԫ������(ģ�����);   //
// 2. make_set:   ��ʼ�� N ��Ԫ�صĲ��鼯;        //
// 3. find_set:   �ҳ�ĳ��Ԫ�����ڵļ���;         //
// 4. union_set:  �ϲ���������;                   // 
// 5. get_sets:   ���ز��鼯�Ӽ��ĸ���;           //
// 6. get_size:   ����Ԫ�������Ӽ��Ĵ�С;         //
//                                                //
// v1.2 �����ԣ�                                  // 
//   ����ʽ���ԣ� ���Ⱥϲ���·��ѹ��              //
//   �����ӿڣ�   �Ӽ��������Ӽ���С              // 
//                                                //
////////////////////////////////////////////////////
//            2008 CopyRight(c) by elf            //
////////////////////////////////////////////////////

template<int SZ> class UFS {

    int p[SZ+1], rank[SZ+1], size[SZ+1], sets; 

public:
    
    void make_set( int sz ) {
        for( int i = 0; i <= sz; ++i ) {
            p[i] = i;
            rank[i] = 0;
            size[i] = 1;
        }
        sets = sz;
    }
    
    int find_set( int x ) {
        if( x != p[x] )
            p[x] = find_set( p[x] );
        return  p[x];
    }

    bool union_set( int x, int y ) {
        x = find_set( x );
        y = find_set( y );
        if( x == y )    return  false;
        --sets;
        if( rank[x] > rank[y] ) {
            size[x] += size[y];
            p[y] = x;
        }
        else {
            size[y] += size[x];
            p[x] = y;
        }
        if( rank[x] == rank[y] )
            ++rank[y];
        return  true;
    }
    
    int get_sets() const { return sets; }
    
    int get_size( int x ) { return size[find_set( x )]; }
    
};

////////////////////////////////////////////////////
//            2008 CopyRight(c) by elf            //
////////////////////////////////////////////////////


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Rect {
    int t, b, l, r;
};

bool conn(Rect a, Rect b) {
    if(a.t > b.t) swap(a, b);
    if(a.l <= b.l) {
        return b.t <= a.b + 1 && b.l <= a.r + 1 && !(b.t == a.b + 1 &&  b.l == a.r + 1);
    }
    else {
        return b.r >= a.l - 1 && b.t <= a.b + 1;
    }
}

int main() {
    UFS<1000> ufs;
    int T;
    cin >> T;
    for(int c = 1; c <= T; ++c) {
        int R;
        cin >> R;
        ufs.make_set(R);
        vector<Rect> V;
        for(int i = 0; i < R; ++i) {
            Rect tmp;
            cin >> tmp.t >> tmp.l >> tmp.b >> tmp.r;
            V.push_back(tmp);
        }
        for(int i = 0; i < R; ++i) {
            for(int j = i + 1; j < R; ++j) {
                if(conn(V[i], V[j])) {
                    ufs.union_set(i, j);
                }
            }
        }
        int last = 0;
        for(int i = 0; i < R; ++i) {
//                cout << ufs.find_set(i) << ' ';
            int b = 0, r = 0, v = INT_MAX;
            for(int j = 0; j < R; ++j) {
                if(ufs.find_set(j) == i) {
                    v <?= V[j].t + V[j].l;
                    b >?= V[j].b;
                    r >?= V[j].r;
                }
            }
            if(v != INT_MAX) {
                last >?= (b + r - v + 1);
            }
        }
        printf("Case #%d: %d\n", c, last);
    }
}
