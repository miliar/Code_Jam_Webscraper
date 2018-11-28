using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <cassert>

#define out(x) (cout<<#x<<": "<<x<<endl)

template<class T>
inline int lth(const T &x) {return static_cast<int>(x.size()); }
inline int t(char c) { return static_cast<int>(c-'a'); }

int L,D,n;

const int NIL = -1;
int Tree[100000][26];
int touch[100000];
bool Terminal[100000];
int tot;

char buf[1000];
void dfs(int r) {
    bool have=false;
    for(int i=0;i<26;++i) {
        if(Tree[r][i]!=NIL) {
            have=true;
            cout<<(char)(i+'a');
            dfs(Tree[r][i]);
        }
    }
    if(!have) {
        printf("\n");
    }
}

int main(int argc,char **argv) {
    freopen(argv[1],"r",stdin);
    freopen(argv[2],"w",stdout);
    
    scanf("%d%d%d",&L,&D,&n);
    memset(Tree,0xff,sizeof(Tree));

    
    memset(Terminal,0,sizeof(Terminal));
    tot = 1;
    for(int i=0;i<D;++i) {
        scanf("%s",buf);

        int cr = 0;
        for(int j=0;j<L;++j) {
            if(Tree[cr][t(buf[j])]==-1) {
                Tree[cr][t(buf[j])]=tot++;
            }
            cr = Tree[cr][t(buf[j])];
        }
        Terminal[cr] = true;
    }
    //out(tot);///debug
   // dfs(0);///debug


    for(int i=0;i<n;++i) {
        memset(touch,0,sizeof(touch));
        int touchMark = 1;

        scanf("%s",buf);

        queue<int> Q;
        Q.push(0);
        touch[0] = touchMark;

        for(char *p=buf;*p;) {
            if(*p=='(') {
                char *q=p+1;
                while(*q!=')') {
                    ++q;
                }

                while(!Q.empty()) {
                    const int cr = Q.front();
                    if(touch[cr]==touchMark) {
                        Q.pop();
                        for(char *s=p+1;s<q;++s) {
                            const int pto = Tree[cr][t(*s)];
                            if(pto!=NIL) {
                                touch[pto] = touchMark+1;
                                Q.push(pto);
                            }
                        }
                    }else {
                        break;
                    }
                }

                p = q+1;
                ++touchMark;
            } else { 
                while(!Q.empty()) {
                    const int cr = Q.front();
                    if(touch[cr]==touchMark) {
                        Q.pop();
                        const int pto = Tree[cr][t(*p)];
                        if(pto!=NIL) {
                            touch[pto]=touchMark+1;
                            Q.push(pto);
                        }
                    }else {
                        break;
                    }
                }
                ++p;
                ++touchMark;
            }
        }
        int ans=0;
        for(int x=0;x<tot;++x) {
            if(touch[x]==touchMark)
                ++ans;
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}












