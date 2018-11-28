#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024*1024];

#define map(x,y) map[(x)*W+(y)]

struct node 
{
    char label; 
    vector<node*> connects;
    int h,w;
    
    int height; 
    explicit node() 
    {
        label=' ';
        height = 0;
        connects.clear();
        h=w=0;
    }
};

int T,H,W;
void getFlow(node*map, int h, int w, int& newh, int &neww)
{
    newh=neww= -1; // nothing
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};
    int min = 10001;
    int myheight = map(h,w).height;

    for(int i=0;i<4;++i)
    {
        int x1 = h+dx[i];
        int y1= w+dy[i];
        if (x1 >=0 && x1<H && y1 >=0 && y1 < W  && myheight > map(x1,y1).height)
        {
            if (map(x1,y1).height < min)
            {
                min = map(x1,y1).height;
                newh=x1;
                neww=y1;
            }
        }
    }
}

void flood(node * map, int h, int w)
{
    deque<node*> q; 
    char color = map(h,w).label;
    q.push_back(&map(h,w));
    while (! q.empty())
    {
        node * p = q.front();
        q.pop_front();
        p->label=color;
        //printf("%d,%d\n", p->h, p->w);
        if (p->h == 7 && p->w == 91)
        {
            int stop = 1;
        }

        for(int i=0;i<p->connects.size();++i)
        {
            if (p->connects.at(i)->label == ' ')
            {
                p->connects.at(i)->label = 'x';
                q.push_back(p->connects.at(i));
                //printf("\t%d,%d\n", p->connects.at(i)->h, p->connects.at(i)->w);
                
            }
        }
    }
}
int main()
{
    freopen("B-large.in", "rt", stdin);
	freopen("output2b.txt", "wt", stdout);

    

    scanf ("%d", &T);
    gets(buf); // get rid of empty line;
    for(int t=0;t<T;++t)
    {
        //printf("tc=%d\n", t);
        scanf("%d%d", &H, &W);
        gets(buf);
        node *map = new node[H*W];
        
        for(int h=0;h<H;++h)
        {
            for(int w=0;w<W;++w)
            {
                int x;
                scanf("%d", &x);
                map(h,w).height = x;
                map(h,w).h = h;
                map(h,w).w = w;
            }
            gets(buf);
        }

        for(int h=0; h<H; ++h)
        {
            for(int w=0;w<W;++w)
            {
                int newh = -1;
                int neww = -1; 

                getFlow(map, h, w, newh, neww);
                if (newh != -1 && neww != -1)
                {
                    map(h,w).connects.push_back(&map(newh,neww));
                    map(newh,neww).connects.push_back(&map(h,w));
                }
            }
        }

        int lastlabel='a';
        for(int h=0; h<H; ++h)
        {
            for(int w=0;w<W;++w)
            {
               // printf("flood %d, %d\n", h, w);
                if (map(h,w).label == ' ')
                {
                    map(h,w).label=lastlabel;
                    lastlabel++;
                    if (lastlabel > 'z') lastlabel = 'a';
                    flood(map,h,w);
                }

            }
        }
        printf("Case #%d:\n", t+1);

        for(int h=0; h<H; ++h)
        {
            printf("%c", map(h, 0).label);
            for(int w=1;w<W;++w)
            {
                printf(" %c", map(h,w).label );
            }
            printf("\n");
        }
    }
}