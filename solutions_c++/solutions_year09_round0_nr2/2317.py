#include <iostream>
#include <vector>
using namespace std;

int findSink(vector< vector<int> > &inpmap, vector< vector<int> > &outmap, int label, int x, int y)
{
    int nextx=x, nexty=y;
    if(x > 0)
        if(inpmap[x - 1][y] < inpmap[nextx][nexty])
        {
            nextx = x - 1;
            nexty = y;
        }
    if(y > 0)
        if(inpmap[x][y - 1] < inpmap[nextx][nexty])
        {
            nextx=x;
            nexty = y - 1;
        }
    if((y + 1) < inpmap[0].size())
        if(inpmap[x][y + 1] < inpmap[nextx][nexty])
        {
            nextx = x;
            nexty = y + 1;
        }
    if((x + 1) < inpmap.size())
        if(inpmap[x + 1][y] < inpmap[nextx][nexty])
        {
            nextx = x + 1;
            nexty = y;
        }
    outmap[x][y] = label;
    if(outmap[nextx][nexty] == -1)
        outmap[nextx][nexty] = findSink(inpmap, outmap, label, nextx, nexty);
    else return outmap[nextx][nexty];
    return outmap[nextx][nexty];
}
int main(int argc, char** argv)
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int k = 1; k <= t; ++k)
    {
        int h,w;
        cin>>h>>w;
        vector< vector<int> > inpmap(h, vector<int>(w));
        vector< vector<int> > outmap(h, vector<int>(w,-1));
        int cur=0;
        for(int i = 0; i < h; ++i)
            for(int j = 0; j < w; ++j)
                cin>>inpmap[i][j];
        for(int i = 0; i < h; ++i)
            for(int j = 0; j < w; ++j)
                if(outmap[i][j]==-1)
                {
                    outmap[i][j] = findSink(inpmap, outmap, cur, i, j);
                    if(outmap[i][j] == cur) cur++;
                }
        cout<<"Case #"<<k<<": "<<endl;
        for(int i = 0; i < h; ++i)
        {
            for(int j = 0; j < w; ++j)
                printf("%c ", 'a' + outmap[i][j]);
            cout<<endl;
        }
    }
    return (0);
}