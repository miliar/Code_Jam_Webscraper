#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef struct Node* NodePtr;
struct Node {
    int group;
    NodePtr next;
};

void enQueue(NodePtr &head, NodePtr &tail, int group) {
    NodePtr node = new Node();
    node->group = group;
    node->next = NULL;
    if(head == NULL) {
        head = node;
        tail = node;
    }
    else {
        tail->next = node;
        tail = node;
    }
}

int isEmpty(NodePtr node) {
    if(node == NULL) {
        return 1;
    }
    
    return 0;
}

int deQueue(NodePtr &head) {
    if(isEmpty(head)) {
        return 0;
    }    
    
    NodePtr temp = head;
    int data = temp->group;
    head = head->next;
    delete temp;
    
    return data;
}

int getTop(NodePtr head) {
    if(head != NULL) {
        return head->group;
    }
    
    return 0;
}

int delQueue(NodePtr &head) {
    while(head != NULL) {
        NodePtr temp = head;
        head = head->next;
        delete temp;
    }
    
    return 0;
}

int solve(int R, int k, int N, NodePtr &head, NodePtr &tail) {
    int money = 0;
    for(int i = 0; i < R; i++) {
        int carry = 0;
        bool check = true;
        NodePtr temp = head;
        int time = 0;
        while(carry <= k && time < N) {
            carry += getTop(head);
            if(carry > k) {
                break;
            }
            if(isEmpty(head)) {
                time = N+1;
            }
            int t = deQueue(head);
            money += t;
            enQueue(head, tail, t);
            time++;
        }
    }
    
    return money;
}

int main() {
    char t[100];
    cin.getline(t, 99);
    
    ifstream fin(t);
    ofstream fout("output.txt");
    int cases;
    fin >> cases;
    
    for(int i = 1; i <= cases; i++) {
        NodePtr head, tail;
        head = NULL;
        tail = NULL;
        int N, k, R, num;
        fin >> R >> k >> N;
        //cout << "RkN " << R << " " << k << " " << N << "\n";
        for(int j = 0; j < N; j++) {
            fin >> num;
            enQueue(head, tail, num);
        }
        
        int temp = solve(R, k, N, head, tail);
        fout << "Case #" << i << ": " << temp << "\n";
        delQueue(head);
    }
    
    fin.close();
    fout.close();
    return 0;
}
