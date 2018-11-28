#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int Tcases;

struct Node{
    int NDncer;
    int Sur;
    int p;
    int* TPnt;

    int result;
};
vector<Node*> cases;

void readfile(){
    ifstream fis ("B-large.in");
    if(!fis){
        cerr<<"File not found!"<<endl;
        exit(-1);
    }

    fis>>Tcases;

    for(int i=0; i<Tcases; i++){
        Node* nd = new Node;
        fis>>nd->NDncer;
        fis>>nd->Sur;
        fis>>nd->p;

        nd->TPnt = new int[nd->NDncer];

        for(int j=0; j<nd->NDncer; j++){
            fis>>nd->TPnt[j];

        }
        cases.push_back(nd);
    }

    fis.close();
}

void process(){
    int brder_h, brder_l, crut_pnt, p;
    int count_l = 0, count_m = 0;
        for(int i=0; i<Tcases; i++){
            p=cases[i]->p;
            if(p>1){
                brder_l = cases[i]->p * 3 - 4;
                brder_h = cases[i]->p * 3 - 2;

                for(int j=0; j<cases[i]->NDncer; j++){
                    crut_pnt = cases[i]->TPnt[j];
                    if(crut_pnt<brder_h && crut_pnt>=brder_l){
                        count_m ++;
                    }
                    if (crut_pnt<brder_l){
                        count_l ++;
                    }
                }
                int off = (count_m - cases[i]->Sur < 0)?0:count_m - cases[i]->Sur;

                cases[i]->result = cases[i]->NDncer - off - count_l;
                count_m = 0;
                count_l = 0;
            }

            if(p==1){      
                cases[i]->result = cases[i]->NDncer;
                for(int j=0; j<cases[i]->NDncer; j++){
                    if (cases[i]->TPnt[j]==0){
                        (cases[i]->result) --;
                    }
                }
            }

            if(p==0){
                cases[i]->result = cases[i]->NDncer;
            }    
    }
}

void writefile(){
    ofstream fos ("B-large.out", ios::out);

    for(int i=0; i<Tcases; i++){
        fos<<"Case #"<<i+1<<": "<<cases[i]->result<<endl;
    }
    
    fos.close();
}

int main(){   
    readfile();
    process();
    writefile();

    return 0;
}