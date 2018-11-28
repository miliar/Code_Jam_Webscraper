#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<math.h>

using namespace std;

int Tcases;

struct Node{
    int small;
    int large;
    int count;
};
vector<Node*> cases;

void readfile(){
    ifstream fis ("C-large.in");
    if(!fis){
        cerr<<"File not found!"<<endl;
        exit(-1);
    }

    fis>>Tcases;

    for(int i=0; i<Tcases; i++){
        Node* nd = new Node;         
        fis>>nd->small>>nd->large;
        nd->count = 0;

        cases.push_back(nd);
    }

    fis.close();
}

void process(){
    for(int i=0; i<Tcases; i++){
        int small = cases[i]->small;
        int large = cases[i]->large;
        if(large > 10){
            if(small < 10){
                small = 10;
            }

            for(int j=small; j<=large; j++){
                int num = j;                
                int Nbit = log((double)num)/log(10.0);
                vector<int> rslt;
                bool flag = true;

                for(int n=0; n<Nbit; n++){
                    int remain = num % 10;
                    num = num/10 + remain*pow(10.0,Nbit);
                    if(num>j && num<=large){
                        for(int m=0; m<rslt.size(); m++){
                            if(num == rslt[m]){
                                flag = false;
                                break;
                            }
                        }
                        if(flag){
                            rslt.push_back(num);
                            (cases[i]->count) ++;
                        }
                        
                    }
                }
            }
        }
    }
}

void writefile(){
    ofstream fos ("C-large.out", ios::out);

    for(int i=0; i<Tcases; i++){
        fos<<"Case #"<<i+1<<": "<<cases[i]->count<<endl;
    }

    fos.close();
}

int main(){   
    readfile();
    process();
    writefile();

    return 0;
}