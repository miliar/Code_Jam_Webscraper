#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int returnCount(queue< pair<char,int> > &q, queue<int> &o_next, queue<int> &b_next)
{
    int o, b, count;
    o = 1;
    b = 1;
    count = 0;
    
    while (!q.empty()) {
        if (q.empty()) {
            break;
        }
        if((q.front().first == 'O') && (o == q.front().second)) {
            count++;
            q.pop();
            o_next.pop();
            if(b>b_next.front()) {
                b--;
            } else if(b < b_next.front()) {
                b++;
            }
        } else if((q.front().first == 'B') && (b == q.front().second)) {
            count++;
            q.pop();
            b_next.pop();
            if(o>o_next.front()) {
                o--;
            } else if(o < o_next.front()) {
                o++;
            }
        } else {
            if(o>o_next.front()) {
                o--;
            } else if(o < o_next.front()) {
                o++;
            }
            if(b>b_next.front()) {
                b--;
            } else if(b < b_next.front()) {
                b++;
            }
            count++;
        }
    }
    return count;
}

int main(void)
{
    queue<int> o_next, b_next;
    queue< pair<char,int> > q;
    int T, n;
    char ch;
    int num;
    scanf("%d", &T);
    for (int i=0; i < T; i++) {
        scanf("%d", &n);
        for (int j=0; j < n; j++) {
            scanf("%s", &ch);
            scanf("%d", &num);
            q.push(pair<char,int>(ch,num));
            if(ch == 'O') {
                o_next.push(num);
            } else {
                b_next.push(num);
            }
        }
        printf("Case #%d: %d\n", i+1, returnCount(q, o_next, b_next));
    }
}