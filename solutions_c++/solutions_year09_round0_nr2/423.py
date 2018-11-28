
#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;

char mm[100][100];
int alt[100][100];
int H, W;

pair<int,int>* nextpos(int i, int j)
{
    pair<int,int>* np=new pair<int,int>;
    int min=alt[i][j], h;
    if(i-1>=0) {
        h = alt[i-1][j];
        if(min>h) {
            min = h;
            np->first = i-1;
            np->second = j;
        }
    }
    if(j-1>=0) {
        h = alt[i][j-1];
        if(min>h) {
            min = h;
            np->first = i;
            np->second = j-1;
        }
    }
    if(j+1<W) {
        h = alt[i][j+1];
        if(min>h) {
            min = h;
            np->first = i;
            np->second = j+1;
        }
    }
    if(i+1<H) {
        h = alt[i+1][j];
        if(min>h) {
            min = h;
            np->first = i+1;
            np->second = j;
        }
    }
    if(min==alt[i][j])
        return NULL;
    return np;
}

int main()
{
    int N;
    freopen("..\\in.txt", "r", stdin);
    freopen("..\\out.txt", "w", stdout);

    scanf("%d", &N);
    string str;

    for(int ncase=0; ncase<N; ncase++) {
        int count=0;

        scanf("%d%d", &H, &W);
        for(int i=0; i<H; i++) {
            for(int j=0; j<W; j++) {
                mm[i][j] = 0;
                scanf("%d", &alt[i][j]);
            }
        }

        char currch='a';
        for(int i=0; i<H; i++) {
            for(int j=0; j<W; j++) {
                if(mm[i][j]==0) {
                    vector<pair<int,int>> stack;
                    stack.push_back(make_pair(i,j));
                    pair<int,int>* next;
                    int ik=i, jk=j;
                    while(NULL != (next=nextpos(ik, jk))) {
                        char ch = mm[next->first][next->second];
                        if(ch != 0) {
                            int s = stack.size();
                            for(int k=0; k<s; k++) {
                                mm[stack[k].first][stack[k].second] = ch;
                            }
                            break;
                        }
                        stack.push_back(*next);
                        ik = next->first;
                        jk = next->second;
                        delete next;
                    }
                    if(NULL==next) {
                        int s = stack.size();
                        for(int k=0; k<s; k++) {
                            mm[stack[k].first][stack[k].second] = currch;
                        }
                        currch++;
                    }
                
                }
            }
        }

        printf("Case #%d:\n", ncase+1);
        for(int i=0; i<H; i++) {
            for(int j=0; j<W; j++) {
                printf("%c ", mm[i][j]);
            }
            putchar('\n');
        }
    }
    return 0;
}

