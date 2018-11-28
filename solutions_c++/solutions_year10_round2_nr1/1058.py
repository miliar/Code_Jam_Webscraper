#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

typedef struct _node node;

struct ltstr
{
      bool operator()(const char* s1, const char* s2) const
            {
                    return strcmp(s1, s2) < 0;
                      }
};

struct _node {
    char *name;
    map<string, _node*> childs;
};

int main() {
    int cases;
    scanf("%d\n", &cases);

    FOR(tcase, cases) {
        int n, m;
        int mk = 0;
        char buffer[110];

        scanf("%d %d\n", &n, &m);

        node root;
        root.name = strdup("/");

        FOR(i, n) {
            fgets(buffer, sizeof(buffer), stdin);
            node *curr = &root;
            char *token;
            char *str = buffer;
            while((token = strtok(str, "/\n")) != NULL) {
                if (curr->childs.find(token) == curr->childs.end()) {
                    node *nnode = new node;
                    nnode->name = strdup(token);
                    curr->childs[token] = nnode;
                }
                curr = curr->childs[token];
                str = NULL;
            }
        }

        FOR(i, m) {
            fgets(buffer, sizeof(buffer), stdin);
            node *curr = &root;
            char *token;
            char *str = buffer;
            while((token = strtok(str, "/\n")) != NULL) {
                if (curr->childs.find(token) == curr->childs.end()) {
                    node *nnode = new node;
                    nnode->name = strdup(token);
                    curr->childs[token] = nnode;
                    mk++;
                } else {
                }
                curr = curr->childs[token];
                str = NULL;
            }
        }

        printf("Case #%d: %d\n", tcase+1, mk);
    }

    return 0;
}
