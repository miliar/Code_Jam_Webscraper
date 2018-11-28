#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <sstream>
using namespace std;
map<int, string> properties;
map<int, double> values;
map<string, bool> prophas;
void putItIn(string node, int pos) {
    float value;
    int start = 0, end = (int)node.size() - 1;
    char property[1024];
    while (start < (int)node.size() && node[start] == ' ') start++;
    while (node[end] == ' ' || node[end] == ')') end--;
    node = node.substr(start, end - start + 1);
    int ret = sscanf(node.c_str(), "%f %s", &value, property);
    if (ret == 2) {
        properties[pos] = property;
        values[pos] = value;
        // cout << property << " has " << value << endl;
    } 
    if (ret == 1) {
        properties[pos] = "";
        values[pos] = value;
    }
    //cout << "|" << node << "|" << start << " " << end << " " << pos << endl;
}
void parseTree(string text, int start, int end, int pos) {
    string node = "";
    while (text[start] == ' ') start++; start++;
    while (text[end] == ' ') end--;
    while (start < end) {
        if (text[start] == '(') break;
        node += text[start++];
    }
    if (start == end) {
        putItIn(node, pos);
    } else {
        putItIn(node, pos);
        int counter = 1, ending = start;
        while (counter) {
            ending++;
            if (text[ending] == '(') counter++;
            if (text[ending] == ')') counter--;
        }
        parseTree(text, start, ending, pos * 2 + 1);
        parseTree(text, ending + 1, end, pos * 2 + 2);
    }
}
double goDeep(int pos) {
    if (properties.count(pos)) {
        if (properties[pos] == "") {
            //cout << pos << " " << values[pos] << endl;
            return values[pos];
        }
        if (prophas.count(properties[pos])) {
            //cout << pos << " " << properties[pos] << ":" << values[pos] << endl;
            return values[pos] * goDeep(pos * 2 + 1);
        } else {
            //cout << pos << " " << properties[pos] << ":" << values[pos] << endl;
            return values[pos] * goDeep(pos * 2 + 2);
        }
    }
    return 1;
}
void goProb(string anim, vector<string> probs) {
    prophas.clear();
    for (int x = 0; x < probs.size(); x++) prophas[probs[x]] = true;
    //cout << anim << endl;
    float getter = goDeep(0);
    printf("%.7f\n", getter);
    return;
}
int a_case(int casen) {
    string animal;
    vector<string> props;
    ostringstream tree("");
    string ctree;
    int lines, prop;
    char line[1024];
    properties.clear();
    values.clear();

    cout << "Case #" << casen << ":" << endl;
    scanf("%d\n", &lines);
    for (int x = 0; x < lines; x++) {
        scanf("%[^\n]\n", line);
        tree << line;
    }
    ctree = tree.str();
    parseTree(ctree, 0, (int)ctree.size() - 1, 0);

    scanf("%d\n", &lines);
    for (int x = 0; x < lines; x++) {
        scanf("%s %d", line, &prop);
        animal = line; props.clear();
        for (int y = 0; y < prop; y++) {
            scanf("%s", line);
            props.push_back(line);
        }
        scanf("\n");
        goProb(animal, props);
    }
    return 0;
}
int main(int argc, char **argv) {
    int trees;
    scanf("%d\n", &trees);
    for (int x = 0; x < trees; x++) a_case(x+1);
    return 0;
}

