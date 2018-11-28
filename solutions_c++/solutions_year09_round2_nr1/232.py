#include <iostream>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

struct node{
    double w;
    string feature;
    node * left;
    node * right;
    node(){
        left=right=0;
    }
};

char text[1024 * 1024];
int size;
int cur;

bool readFeature(string & res){    
    res = "";
    while (!isalpha(text[cur]) && text[cur] != ')')
        cur++;
    if (text[cur] == ')'){
        return false;
    }
    while (isalpha(text[cur])){
        res += text[cur];
        cur++;
    }
    return true;
}

void toBr(){
    while (text[cur] != ')')
        cur++;
}

char dStr[15];

double toD(char * str){
    bool wasDot = false;
    double res = 0;
    double cur10 = 1;
    for (int i = 0; str[i]; i++){
        if (str[i] == '.'){
            wasDot = true;
            continue;
        }
        if (!wasDot){
            res = res * 10 + (int)(str[i] - '0');
        }else{
            cur10 /= 10;
            res = res + cur10 * (int)(str[i] - '0');
        }
    }
    return res;    
}

double readDouble(){
    memset(dStr,0,sizeof(dStr));
    while (!isdigit(text[cur]))
        cur++;
    int i = 0;
    while (isdigit(text[cur]) || text[cur] == '.'){
        dStr[i++] = text[cur];
        cur++;        
    }
    dStr[i] = 0;
    return toD(dStr);
}

node * readNode(){
    node * res = new node();                
    res->w = readDouble();
    string f;
    if (readFeature(f)){
        res->feature = f;
        res->left = readNode();
        res->right = readNode();
    }
    toBr();
    cur++;
    return res;
}

char buffer[1024 * 1024];
void readStrs(int strNumber){
    size = 0;
    for (int i = 0; i < strNumber; i++){
        gets(buffer);
        for (int j = 0; buffer[j]; j++)
            text[size++] = buffer[j];
    }
}

vector<string> fs;

string toStr(){
    string res = "";
    for (int i = 0; buffer[i]; i++)
        res += buffer[i];
    return res;
}

void getAnimal(){
    fs.clear();
    scanf("%s",buffer);
    int n; scanf("%d\n",&n);
    for (int i = 0; i < n; i++){
        scanf("%s",buffer);
        fs.push_back(toStr());        
    }
}

bool has(string & str){
    for (int i = 0; i < fs.size(); i++)
        if (str == fs[i])
            return true;
    return false;
}

double rec(node * v){
    if (!v->left){
        return v->w;
    }
    if (has(v->feature))
        return (v->w) * rec(v->left);
    else
        return (v->w) * rec(v->right);
}

node * root;

void doAnimal(){
    getAnimal();    

    printf("%.10lf\n",rec(root));
}

void  doTest(){
    cur = 0;    
    int strNumber;
    scanf("%d\n",&strNumber);
    readStrs(strNumber);
    root = readNode();
    int animals;
    scanf("%d\n",&animals);
    for (int i = 0; i < animals; i++)
        doAnimal();
}


int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int i = 0; i < T; i++){
        printf("Case #%d:\n",(i+1));
        doTest();
    }

    return 0;
}