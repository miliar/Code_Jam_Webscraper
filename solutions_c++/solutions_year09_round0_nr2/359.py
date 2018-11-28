#include<iostream>
#include<queue>
#include<string.h>
#include<stdio.h>
using namespace std;
#define maxn 10011

int rank[maxn], pnt[maxn];

void makeset(int x) {
    rank [pnt[x] = x] = 0;
}

int findUnionSet(int x) {
    int px = x, i;
    while (px != pnt[px]) {
        px = pnt[px];
    }
    while (x != px) {
        i = pnt[x];
        pnt[x] = px;
        x = i;
    }
    return px;
}

void mergeUnionSet(int x, int y) // or just pnt[find(x)]=find(y)
{
    if (rank[x = findUnionSet(x)] > rank[y = findUnionSet(y)])
        pnt[y] = x;
    else {
        pnt[x] = y;
        rank[y] += (rank[x] == rank[y]);
    }
}

struct node {
    int x, y, id;

    node() {
    }

    node(int a, int b, int c) : x(a), y(b), id(c) {
    }

    bool operator<(const node & a)const {
        return id < a.id;
    }
};
int h, w;
int board[128][128];
int visit[128][128];

int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0}; //North, West, East, South.

priority_queue<node> que;

bool check(int x, int y) {
    return x >= 0 && y >= 0 && x < h && y < w;
}

void flow(node tem, int mark) {
    visit[tem.x][tem.y] = mark;
    int i, tx, ty, lx, ly, least = tem.id;
    for (i = 0; i < 4; i++) {
        tx = tem.x + dir[i][0];
        ty = tem.y + dir[i][1];
        if (check(tx, ty) && board[tx][ty] < least) {
            least = board[tx][ty];
            lx = tx;
            ly = ty;
        }
    }
    if (least == tem.id)return;
    if (visit[lx][ly]) {
        mergeUnionSet(visit[lx][ly], visit[tem.x][tem.y]);
    } else {
        flow(node(lx, ly, board[lx][ly]), mark);
    }

}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("data.txt","w",stdout);
    int cas, T;
    int i, j, cnt;
    node tem;
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas++) {

        while (!que.empty())que.pop();
        memset(visit, 0, sizeof (visit));
        for (i = 1; i <= maxn; i++)makeset(i);

        scanf("%d %d", &h, &w);
        for (i = 0; i < h; i++)
            for (j = 0; j < w; j++) {
                scanf("%d", &board[i][j]);
                que.push(node(i, j, board[i][j]));
            }
        cnt = 1;
        while (!que.empty()) {
            tem = que.top();
            que.pop();
            while (!que.empty() && visit[tem.x][tem.y]) {
                tem = que.top();
                que.pop();
            }
            if (!visit[tem.x][tem.y])
                flow(tem, cnt++);
//                        printf("%d %d %d\n",tem.x, tem.y, tem.id);
//                        for (i = 0; i < h; i++) {
//                            for (j = 0; j < w - 1; j++)
//                                printf("%d ", visit[i][j]);
//                            printf("%d\n", visit[i][j]);
//                        }
//                        printf("\n");
        }

        memset(rank, 0, sizeof (rank));
        cnt = 'a';
        for (i = 0; i < h; i++)
            for (j = 0; j < w; j++) {
                visit[i][j] = findUnionSet(visit[i][j]);
                if (!rank[visit[i][j]]) {
                    rank[visit[i][j]] = cnt;
                    cnt++;
                }
            }
        printf("Case #%d:\n", cas);
        //            for(i = 0; i < h; i++)
        //            {
        //                for(j = 0; j < w-1; j++)
        //                printf("%d ",visit[i][j]);
        //                printf("%d\n",visit[i][j]);
        //            }
        for (i = 0; i < h; i++) {
            for (j = 0; j < w - 1; j++)
                printf("%c ", rank[visit[i][j]]);
            printf("%c\n", rank[visit[i][j]]);
        }

    }
}

/*
 2
 1 10
0 1 2 3 4 5 6 7 8 7
 */