
#include <iostream>
#include <list>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

struct Node {
    list<unsigned int> *sean;
    list<unsigned int> *patrick;
    unsigned int position;
    unsigned int xoredSumSean;
    unsigned int xoredSumPatrick;
};

struct Comp {
    bool operator()(const struct Node *a, const struct Node *b) {
        return a->position > b->position;
    }
};

priority_queue<struct Node *, vector<struct Node *>, Comp> nodes;


unsigned int sum(list<unsigned int> &l) {
    unsigned int value = 0;
    for (list<unsigned int>::iterator it = l.begin(); it != l.end(); ++it) {
        value += *it;
    }
    return value;
}

unsigned int xoredSum(list<unsigned int> &l) {
    unsigned int value = 0;
    for (list<unsigned int>::iterator it = l.begin(); it != l.end(); ++it) {
        value ^= *it;
    }
    return value;
}

void printList(const list<unsigned int> &l) {
    cout << '[';
    for (list<unsigned int>::const_iterator it = l.begin(); it != l.end(); ++it) {
        cout << *it << " ";
    }

    cout << ']' << endl;
}

void doTestcase() {
    unsigned int n;
    cin >> n;

    while (!nodes.empty()) {
        delete nodes.top()->sean;
        delete nodes.top()->patrick;
        delete nodes.top();
        nodes.pop();
    }

    struct Node *node = new struct Node();
    node->sean = new list<unsigned int>();
    node->patrick = new list<unsigned int>();
    node->position = 0;
    node->xoredSumSean = 0;
    node->xoredSumPatrick = 0;

    for (unsigned int i = 0; i < n; ++i) {
        unsigned int candy;
        cin >> candy;
        node->sean->push_back(candy);
    }

    node->sean->sort();
    node->xoredSumSean = xoredSum(*(node->sean));
    nodes.push(node);

    if (node->xoredSumSean != 0) {
        cout << "NO";
        return;
    }

    while (!nodes.empty()) {
        node = nodes.top();
        nodes.pop();




        if (!node->patrick->empty() && node->xoredSumPatrick == node->xoredSumSean) {
            cout << sum(*(node->sean));
            delete node->sean;
            delete node->patrick;
            delete node;
            return;
        }

        for (list<unsigned int>::iterator it = node->sean->begin(); it != node->sean->end(); ++it) {
            struct Node *newNode = new struct Node();
            newNode->sean = new list<unsigned int>();
            newNode->patrick = new list<unsigned int>();
            newNode->patrick->insert(newNode->patrick->end(), node->patrick->begin(), node->patrick->end());
            newNode->patrick->push_back(*it);
            newNode->sean->insert(newNode->sean->end(), node->sean->begin(), it);
            newNode->sean->insert(newNode->sean->end(), ++it, node->sean->end());
            --it;
            newNode->position = node->position + *it;
            newNode->xoredSumPatrick = node->xoredSumPatrick ^ *it;
            newNode->xoredSumSean = node->xoredSumSean ^ *it;
            nodes.push(newNode);
        }
        delete node->sean;
        delete node->patrick;
        delete node;
    }

    cout << "NO";
}

int main(int argc, char *argv[]) {
    unsigned int t;
    cin >> t;

    for (unsigned int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        doTestcase();
        cout << endl;
    }
    return 0;
}

