#include <iostream>
#include <cstring>

using namespace std;

struct node {
    char name[100]; // eg. "/", "home", gcj
    int name_len;
    node *children[200];
    int child_count;
};

node* root;

node* create_node(char *name, int len) {
    node *p= new node();
    bzero(p, sizeof(node));
    strncpy(p->name, name, len);
    p->name_len= len;
    return p;
}

node* append_child(char *name, int len, node* n) {
    if(n->children[n->child_count] == NULL)
        n->children[n->child_count] = create_node(name, len);
    else {
        strncpy(n->children[n->child_count]->name, name, len);
        n->children[n->child_count]->name_len= len;
        n->children[n->child_count]->child_count= 0;
    }
    n->child_count++;
}


int add_path(char *path, int start, node* n) {
    int end= start;
    while(path[end] != '/' && path[end] != '\0')
        end++;
    node *child;
    for(int i= 0; i < n->child_count; i++) {
        child= n->children[i];
        if(child->name_len != end - start)
            continue;
        if(strncmp(path + start, child->name, child->name_len) == 0) {
            if(path[end] == '\0')
                return 0;
            return add_path(path, end + 1, child);
        }
    }
    append_child(path + start, end - start, n);
    if(path[end] != '\0')
        return 1 + add_path(path, end + 1, n->children[n->child_count - 1]);
    else
        return 1;
}

void remove_node(node *n) {
    for(int i= 0; i < n->child_count; i++) {
        remove_node(n->children[i]);
    }
    n->child_count= 0;
}

char line[101];
char root_name[2] = "/";

int main() {
    int T, N, M, i, j, k;
    cin >> T;
    root= create_node(root_name, 1);
    for(i= 1; i <= T; i++) {
        cin >> N >> M;
        int sum= 0;
        for(j= 0; j < N; j++) {
            cin >> line;
            add_path(line, 1, root);
        }
        for(j= 0; j < M; j++) {
            cin >> line;
            sum+= add_path(line, 1, root);
        }
        remove_node(root);
        cout << "Case #" << i << ": " << sum << endl;
    }
    return 0;
}
