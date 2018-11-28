#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

inline int abs(int c){
    if(c>=0){
        return c;
    }else{
        return -c;
    }
}

struct Combination{
    int a;
    int b;
    int c;
    bool sur;
    int sum;
    Combination(int a_=0, int b_=0, int c_=0):a(a_),b(b_),c(c_)
    {
        sum=a+b+c;
        if(abs(a-b)==2 || abs(b-c)==2 || abs(a-c)==2){
            sur=true;
        }else{
            sur=false;
        }
    };
};

Combination possibleCombinations[58];

void generate(){
    int N =0;
    for(int i=0; i<=10; i++){
        for(int j=i; j<=10; j++){
            for(int k=j; k<=10; k++){
                if(abs(i-j)<=2 && abs(i-k)<=2 && abs(j-k)<=2){
                    possibleCombinations[N++] = Combination(i,k,j);
                }
            }
        }
    }
}

int maxCount=0;
int maxSur;
int plank;

void test(vector<int>* combs, int i, int& N, int* selected){
    if(i==N){
        int sur=0;
        for(int j=0; j<N; j++){
            cout << selected[j];
            if(possibleCombinations[selected[j]].sur){
                sur++;
                cout<<"_";
            }else{
                cout<<" ";
            }
        }
        if(sur==maxSur){
            cout << " v";
            int count=0;
            for(int j=0; j<N; j++){
                if(possibleCombinations[selected[j]].a >= plank ||
                   possibleCombinations[selected[j]].b >= plank ||
                   possibleCombinations[selected[j]].c >= plank){
                    count++;
                }
            }
            if(maxCount<count){
                maxCount=count;
            }
        }
        cout << endl;
    }else{
        for(int k=0; k<combs[i].size(); k++){
            selected[i] = combs[i][k];
            test(combs,i+1,N,selected);
        }
    }
}

int main(){
    generate();
    ifstream input("input.txt");
    ofstream output("output.txt");

    int T=0;
    input >> T;
    for(int i=0; i<T; i++){
        int N;
        input >> N >> maxSur >> plank;
        int googlers[N];
        vector<int> comb[N];
        for(int j=0; j<N; j++){
            input >> googlers[j];
            for(int p=0; p<58; p++){
                if(possibleCombinations[p].sum==googlers[j]){
                    comb[j].push_back(p);
                    cout << comb[j][comb[j].size()-1] << " ";
                }
            }
            cout << endl;
        }
        maxCount=0;
        int selected[N];
        test(comb, 0, N, selected);

        output << "Case #" << (i+1) << ": " << maxCount << endl;
    }

    input.close();
    output.close();
    return 0;
}
