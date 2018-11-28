#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

typedef pair<int, int> pos;

pair<bool, int> valid(const VVI& board, int p, int q, int sz)
{
    const int c = board[p][q];
    if(c >= 2)
        return make_pair(false, q);
    for(int i=p;i<p+sz;i++) {
        for(int j=q;j<q+sz;j++) {
            int validc = (i-p+j-q)%2 == 0 ? c : 1-c;
            if(board[i][j] != validc)
                return make_pair(false, j > q ? j-1 : j);
        }
    }
    return make_pair(true, q+sz-1);
}

void fill(VVI& board, int p, int q, int sz)
{
    for(int i=p;i<p+sz;i++) {
        for(int j=q;j<q+sz;j++) {
            board[i][j] = 2;
        }
    }
}

void print(const VVI& board)
{
    for(int i=0;i<board.size();i++) {
        for(int j=0;j<board[i].size();j++) {
            cout << board[i][j];
        }
        cout << endl;
    }
    cout <<endl;
}

int main()
{
    int t;
    cin >> t;
    for(int cnt=1;cnt<=t;cnt++) {
        int m, n;
        cin >> m >> n;
        VVI board(m, vector<int>(n, 0));
        for(int i=0;i<m;i++) {
            string s;
            cin >> s;
            for(int j=0;j<n/4;j++) {
                int ss = s[j] >= '0' && s[j] <= '9' ? s[j]-'0' : s[j]-'A'+10;
                board[i][j*4] = (ss&8) > 0 ? 1 : 0;
                board[i][j*4+1] = (ss&4) > 0 ? 1 : 0;
                board[i][j*4+2] = (ss&2) > 0 ? 1 : 0;
                board[i][j*4+3] = (ss&1) > 0 ? 1 : 0;
            }
        }

//        print(board);

        map<int, int> ans;
        for(int sz=max(m, n);sz>=1;sz--) {
            for(int i=0;i<=m-sz;i++) {
                for(int j=0;j<=n-sz;j++) {
                    pair<bool, int> v = valid(board, i, j, sz);
                    if(v.first) {
                        fill(board, i, j, sz);
                        ans[sz]++;
                    }
                    j = v.second;
                }
            }
        }

        cout << "Case #" << cnt << ": " << ans.size() << endl;
        
        map<int, int>::reverse_iterator i;
        for(i=ans.rbegin();i!=ans.rend();i++) {
            cout << i->first << ' ' << i->second << endl;
        }
        
    }
    
    return 0;
}
