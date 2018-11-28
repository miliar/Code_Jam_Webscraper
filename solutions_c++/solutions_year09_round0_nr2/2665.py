#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <functional>

using namespace std;

#define Rep(i,n) for (int i(0),_n(n); i<_n; ++i)
#define Vs vector<string>
#define Vsi vector<string>::iterator
#define Vi vector<int>
#define Vii vector<int>::iterator
#define Wilv(v,iter,iter_end) (iter)=(v).begin(),(iter_end)=(v).end();while( (iter)!=(iter_end) )

typedef pair<int,int> Point;

char gmap[100][100];
int altitudes[100][100];
int H, W;

Point* gonext(int i, int j)
{
    Point* pos=new Point;
    int min=altitudes[i][j];
    if(i-1>=0)
    {
        if(min>altitudes[i-1][j])
        {
            min = altitudes[i-1][j];
            pos->first = i-1;
            pos->second = j;
        }
    }
    if(j-1>=0)
    {
        if(min>altitudes[i][j-1])
        {
            min = altitudes[i][j-1];
            pos->first = i;
            pos->second = j-1;
        }
    }
    if(j+1<W)
    {
        if(min>altitudes[i][j+1])
        {
            min = altitudes[i][j+1];
            pos->first = i;
            pos->second = j+1;
        }
    }
    if(i+1<H)
    {
        if(min>altitudes[i+1][j])
        {
            min = altitudes[i+1][j];
            pos->first = i+1;
            pos->second = j;
        }
    }
    if(min==altitudes[i][j])
        return NULL;
    else
        return pos;
}

int main()
{
    int T;

    cin >> T;

    Rep(n,T)
    {
        cin >> H >> W;
        Rep(i,H)
        {
            Rep(j,W)
            {
                gmap[i][j] = 0;
                cin >> altitudes[i][j];
            }
        }

        char curr='a';
        Rep(i,H)
        {
            Rep(j,W)
            {
                if(gmap[i][j]==0)
                {
                    vector<Point> stack;
                    stack.push_back(make_pair(i,j));
                    Point* p;
                    int i_tmp=i, j_tmp=j;
                    while((p = gonext(i_tmp, j_tmp))!=NULL)
                    {
                        char c = gmap[p->first][p->second];
                        if(c != 0)
                        {
                            Rep(k, stack.size())
                            {
                                gmap[stack[k].first][stack[k].second] = c;
                            }
                            break;
                        }
                        stack.push_back(*p);
                        i_tmp = p->first;
                        j_tmp = p->second;
                        delete p;
                    }
                    if(NULL==p)
                    {
                        Rep(k, stack.size())
                        {
                            gmap[stack[k].first][stack[k].second] = curr;
                        }
                        curr++;
                    }
                }
            }
        }

        cout << "Case #" << n+1 << ":" <<endl;
        Rep(i,H) 
        {
            Rep(j,W)
            {
                cout << gmap[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}

