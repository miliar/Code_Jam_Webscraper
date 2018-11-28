#include <iostream>
#include <vector>
#include <string>
//#include <deque>
#include <algorithm>
using namespace std;
struct Node
{
    int dep;
    int arr;
};
int flag[1500] = {0};

int cmp( const void *a , const void *b )
{
struct Node *c = (Node *)a;
struct Node *d = (Node *)b;
if(c->dep != d->dep) return c->dep - d->dep;
else return d->arr - c->arr;
}
void init(int arrA[1500], int arrB[1500])
{
    for( int i = 0; i < 1500; ++i )
    {
        flag[i] = 0;
        arrA[i] = 0;
        arrB[i] = 0;
    }
}
int getTime()
{
    int h, minT;
    char c;
    cin >> h >> c >> minT;
    return h * 60 + minT;
}
void makeFlag(int x)
{
    flag[x] = 1;
}
void output(int ncase, int yoyo, int anum, int bnum)
{
    cout << "Case #"<<yoyo - ncase<<": ";
    cout << anum << " " << bnum << endl;
}

bool isDep(vector<Node> v, int x, int curr)
{
    Node temp = v[curr];
    int t = temp.dep;
    if( t == x )
        return 1;
    return 0;
}
void change( int x )
{
    cout << x/ 60 << ":" << x%60 << endl;
}

int main()
{
    int ncase;
    cin >> ncase;
    int yoyo = ncase;
    while(ncase--)
    {

        int a = 0, b = 0; //A B train
        int anum, bnum;
        int turn;
        int resultA = 0, resultB = 0;
        int arrA[1500];
        int arrB[1500];
        int currA = 0, currB = 0;
        init(arrA, arrB);
        vector<Node> NA;
        vector<Node> NB;
        cin >> turn;
        cin >> anum >> bnum;
        for( int i = 0; i < anum; ++i )
        {
            Node node;
            node.dep = getTime();
            node.arr = getTime() + turn;
            makeFlag(node.dep);
            makeFlag(node.arr);
            NA.push_back(node);
        }

        //cout << "one ncase" << endl;
        for( int i = 0; i < bnum; ++i )
        {
            Node node;
            node.dep = getTime();
            node.arr = getTime() + turn;
            makeFlag(node.dep);
            makeFlag(node.arr);
            NB.push_back(node);
        }

        if( anum == 0 || bnum == 0 )
        {
            output(ncase, yoyo, anum, bnum);
            continue;
        }
        qsort(&NA[0], NA.size(), sizeof(NA[0]), cmp);
        qsort(&NB[0], NB.size(), sizeof(NB[0]), cmp);

        for( int i = 0; i < 1440; ++i )
        {
            if(flag[i] == 0 )
               continue;
//            cout << "////////////  time is ";
//            change(i);

            while( arrA[i] != 0 )
            {
                ++a;
                --arrA[i];
//                cout << "Arrive at A " << endl;
//                cout << "now a = " << a << endl;
            }
            while( arrB[i] != 0 )
            {
                ++b;
                --arrB[i];
//                cout << "Arrive at B " << endl;
//                cout << "now b = " << b << endl;
            }
            while( isDep(NA, i, currA) )
            {
//                cout << "Dep from A " << endl;

                if(a >=1)
                    --a;
                else
                {
//                    cout << "****** new train *******" << endl;
                    ++resultA;
                }

                Node node = NA[currA];
                ++arrB[node.arr];
                ++currA;
            }
            while( isDep(NB, i, currB) )
            {
//                cout << "Dep from B " << endl;
                if( b >= 1)
                    --b;
                else
                {
                    ++resultB;
//                    cout << "****** new train *******" << endl;
                }

                Node node = NB[currB];
                ++arrA[node.arr];
                ++currB;

            }

        }
        output(ncase, yoyo, resultA, resultB);
        NA.resize(0);
        NB.resize(0);
    }
}

