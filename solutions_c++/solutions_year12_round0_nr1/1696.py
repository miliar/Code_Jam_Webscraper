#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int Tcases;

struct Node{
    string str_in;
    string str_out;
};
vector<Node*> cases;

void readfile(){
    ifstream fis ("A-small-attempt0.in");
    if(!fis){
        cerr<<"File not found!"<<endl;
        exit(-1);
    }

    fis>>Tcases;

    //line 0 is empty...
    for(int i=0; i<=Tcases; i++){
        Node* nd = new Node;        
        getline(fis, nd->str_in);

        cases.push_back(nd);
    }

    fis.close();
}

void process(){
    for(int i=1; i<=Tcases; i++){
        int len = cases[i]->str_in.size();
        char ch_orgn[101];
        strcpy(ch_orgn, cases[i]->str_in.c_str());
        char ch_rslt[101];

        for(int j=0; j<len; j++){
            switch(ch_orgn[j]){
                case 'a':
                    ch_rslt[j]='y';
                    break;
                case 'b':
                    ch_rslt[j]='h';
                    break;
                case 'c':
                    ch_rslt[j]='e';
                    break;
                case 'd':
                    ch_rslt[j]='s';
                    break;
                case 'e':
                    ch_rslt[j]='o';
                    break;
                case 'f':
                    ch_rslt[j]='c';
                    break;
                case 'g':
                    ch_rslt[j]='v';
                    break;
                case 'h':
                    ch_rslt[j]='x';
                    break;
                case 'i':
                    ch_rslt[j]='d';
                    break;
                case 'j':
                    ch_rslt[j]='u';
                    break;
                case 'k':
                    ch_rslt[j]='i';
                    break;
                case 'l':
                    ch_rslt[j]='g';
                    break;
                case 'm':
                    ch_rslt[j]='l';
                    break;
                case 'n':
                    ch_rslt[j]='b';
                    break;
                case 'o':
                    ch_rslt[j]='k';
                    break;
                case 'p':
                    ch_rslt[j]='r';
                    break;
                case 'q':
                    ch_rslt[j]='z';
                    break;
                case 'r':
                    ch_rslt[j]='t';
                    break;
                case 's':
                    ch_rslt[j]='n';
                    break;
                case 't':
                    ch_rslt[j]='w';
                    break;
                case 'u':
                    ch_rslt[j]='j';
                    break;
                case 'v':
                    ch_rslt[j]='p';
                    break;
                case 'w':
                    ch_rslt[j]='f';
                    break;
                case 'x':
                    ch_rslt[j]='m';
                    break;
                case 'y':
                    ch_rslt[j]='a';
                    break;
                case 'z':
                    ch_rslt[j]='q';
                    break;
                case ' ':
                    ch_rslt[j]=' ';
                    break;
                default:
                    cerr<<"Error occurred!";
                    break;
            }
        }
        ch_rslt[len]='\0';
        cases[i]->str_out = string(ch_rslt);
        cout<<cases[i]->str_out<<endl;
    }
}

void writefile(){
    ofstream fos ("A-small.out", ios::out);

    for(int i=1; i<=Tcases; i++){
        fos<<"Case #"<<i<<": "<<cases[i]->str_out<<endl;
    }

    fos.close();
}

int main(){   
    readfile();
    process();
    writefile();

    return 0;
}