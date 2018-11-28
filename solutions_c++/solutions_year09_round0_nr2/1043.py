#include <stdio.h>
#include <string>
#include <set>
#include <vector>
using namespace std;

int ncase;
int w, h;
int tu[200][200];
int i, j;
int ans[200][200];
bool debug = false;

set<pair<int, int> > tmpSet;


void init() {
    scanf("%d%d", &h, &w);
    for (i=0; i<h; ++i)
        for (j=0; j<w; ++j)
            scanf("%d", &tu[i][j]);
}

int movex[] = {-1, 0, 0, 1};
int movey[] = {0, -1, 1, 0};
void genSet(int x, int y) {
    int targetX, targetY;
    targetX = targetY = -1;
    tmpSet.insert(make_pair(x, y));
    int minv = tu[x][y];
    for (int p=0; p<4; ++p) {
        int tx = x+ movex[p];
        int ty = y + movey[p];
        if (tx>=0 && ty>=0 && tx<h && ty<w) {
            if (minv > tu[tx][ty]) { 
                minv = tu[tx][ty];
                targetX = tx;
                targetY = ty;
            }    
        }    
    }    
    
    if (minv != tu[x][y]) {
        genSet(targetX, targetY);
    }    
}    

void deal() {
    memset(ans, 0, sizeof(ans));
    int cnt = 1;
    for (i=0; i<h; ++i)
        for (j=0; j<w; ++j) {
            if (ans[i][j] != 0) continue;
            tmpSet.clear();
            genSet(i, j);  
            if (debug) {
                printf("----for %d %d\n", i, j);
                for (set<pair<int, int> >::iterator pos=tmpSet.begin(); pos!=tmpSet.end(); ++pos) {
                    printf("gen (%d,%d)\n", (*pos).first, (*pos).second);
                } 
            }
            int mark = 0;
            for (set<pair<int, int> >::iterator pos=tmpSet.begin(); pos!=tmpSet.end(); ++pos) {
                    int x = (*pos).first;
                    int y = (*pos).second;
                    if (ans[x][y] != 0) {
                        mark = ans[x][y];
                        break;
                    }    
            } 
            if (mark == 0) {
                mark = cnt ++;
            } 
            for (set<pair<int, int> >::iterator pos=tmpSet.begin(); pos!=tmpSet.end(); ++pos) {
                    int x = (*pos).first;
                    int y = (*pos).second;
                    if (ans[x][y] == 0) {
                        ans[x][y] = mark;
                    }    
            }    
                   
        }     
}

void getAns(int v, char ch) {
    for (i=0; i<h; ++i)
        for (j=0; j<w; ++j) 
            if (ans[i][j] == v) 
                ans[i][j] = ch;
}    

void output(int icase) {
    int i, j;
    char ch = 'a';
    for (i=0; i<h; ++i)
        for (j=0; j<w; ++j) {
            if (ans[i][j]>='a' && ans[i][j]<='z') continue;
            getAns(ans[i][j], ch);
            ch++;
        }    
    
    // output
    printf("Case #%d:\n", icase);
    for (i=0; i<h; ++i, printf("\n"))
        for (j=0; j<w; ++j) 
            printf("%c ", ans[i][j]);

}            
int main()
{
    int i;

    freopen("B-2.in", "r", stdin);
    freopen("B-2.out", "w", stdout);
    
    scanf("%d", &ncase);
    for (i=0; i<ncase; ++i) {
        init();
        deal();
        output(i+1);
    }    
    
    return 0;
}    
/*
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8

*/

