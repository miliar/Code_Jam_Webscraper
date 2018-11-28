#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>

using namespace std;

const int maxint = 0x7fffffff;
const int max_len = 100 + 10;
const int max_size = 100 + 3;

struct tree_node{
    double val;
    string name;
    
    void out(){
        printf("%.3lf %s\n", val, name.c_str());
    }
    
    int father;
};


struct node {
    string s;
    double p;
    int lf, rt;
};

char s[max_len * max_len], tmp_s[max_len];
int pre[max_len * max_len];
node tree[max_len * max_len];

set<string> data;
int num, n, num_line, m;

void make(char *, int );
void init();

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int nCase;
    scanf("%d", &nCase);
    for (int t=0; t<nCase; t++){
        scanf("%d\n", &num_line);
        
        s[0] = 0;
        
        while (num_line--) {
            gets(tmp_s);
            strcat(s, tmp_s);
            strcat(s, " ");
        }
        
        num = 1;
        for (int i=0; i < max_len * max_len; i++) {
            tree[i].s = string();
            tree[i].p = tree[i].lf = tree[i].rt = 0;
        }
        
        make(s,  strlen(s));
        scanf("%d", &n);
        printf("Case #%d:\n", t + 1);
        
        for (int i=0; i<n; i++) {
            data.clear();
            scanf("%s%d", s, &m);
            
            for (int j=0; j<m; ++j) {
                scanf("%s", tmp_s);
                data.insert(string(tmp_s));
            }
            
            int cur = 1;
            double ans = tree[cur].p;
            while (tree[cur].s[0]) {
                if (data.find(tree[cur].s) != data.end()) {
                    cur = tree[cur].lf;
                } else {
                    cur = tree[cur].rt;
                }
                ans *= tree[cur].p;
            }
            printf("%.7lf\n", ans);
        }
    }
    return 0;
}

void make(char *s, int n) {
    int cur = 0;
    int next;
    
    for (int i = 0; i < n; i = next) {
        next = i + 1;
        
        if (s[i] == ' ') continue;
        
        if (s[i] == '(') {
            
            pre[num] = cur;
            if (tree[cur].lf == 0) tree[cur].lf = num;
            else tree[cur].rt = num;
            cur = num++;
            
        } else if (s[i] == ')') cur = pre[cur];
        else if (isdigit(s[i])) {
            sscanf(s + i, "%lf", &tree[cur].p);
            while (s[next] != ')' && s[next] != ' ') next++;
        } else if (isalpha(s[i])) {
            sscanf(s + i, "%s", tmp_s);
            tree[cur].s = string(tmp_s);
            while (s[next] != ' ') next++;
        }
        
    }
}

void init(){
    // for (int t=0; t<nCase; t++){
        scanf("%d", &num_line);
        getchar();
     //   data.clear(); tree.clear();
        int father = 0; int num = 0;
        
        for (int j=0; j<num_line; j++){
            char tmp[max_len];
            gets(tmp);
            //printf("%s\n", tmp);
            
            tree_node t_node;
            t_node.val = 0; t_node.name = "";
            
            int i = 0, len = strlen(tmp);
            
            while (i < len){
                double cnt = 1; bool flag = true;
                
                if (tmp[i] == '(' ) num++;
                
                if (tmp[i] == ')'){
                    num --;
                    
        //            if (num == 0 && fahter != 0) father = tree[father].father;
                }
                
                if (tmp[i] >= '0' && tmp[i] <='9'){
                    while ((tmp[i] >= '0' && tmp[i] <= '9') || tmp[i] == '.'){
                        if (tmp[i] == '.'){
                            flag = false;
                        }
                        else{
                            if (flag) {
                                //printf("%c", tmp[i]);
                                t_node.val = t_node.val * 10 + tmp[i] - '0';
                                //printf("%d %d\n", t_node.val, tmp[i] - '0');
                            }
                            else {
                                cnt /= 10.0;
                                t_node.val += (tmp[i] - '0' + 0.0) * cnt;
                            }
                        }
                        i++;
                    }
                }
                
               // printf("%d\n", i);
                while (tmp[i] >= 'a' && tmp[i] <= 'z'){
                   // printf("--%c %d", tmp[i], i);
                    t_node.name = t_node.name + tmp[i];
                    i++;
                }
               // printf("\n");
                
                i++;
            }
            
           // t_node.out();
            t_node.father = father;
      //      tree.push_back(t_node);
        }
        
        scanf("%d", &n);
        
        for (int i=0; i<n; i++){
            char tmp[max_len];
            scanf("%s", tmp);
            scanf("%d", &m);
            
            for (int j=0; j<m; j++){
                
                scanf("%s", tmp);
               // printf("%s\n", tmp);
                
        //        data.push_back(tmp);
            }
            
            
        }
}

