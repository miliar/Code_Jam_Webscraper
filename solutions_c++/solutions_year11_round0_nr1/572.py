#include<fstream>
#include<vector>
using namespace std;
ifstream in("A.in");ofstream out("A.out");
int main(){
    vector<int> nextblue, nextorg;
    int N,T,bluepos,orgpos,next[101],bluedone,orgdone,time,tot;
    char c[101];
    in>>T;
    for (int t=0;t<T;t++){
        nextblue.clear(); nextorg.clear();
        in>>N;
        bluepos=orgpos=1; bluedone=orgdone=time=0;
        for (int n=0;n<N;n++){
            in>>c[n];
            in>>next[n];
            if (c[n]=='B') nextblue.push_back(next[n]);
            else nextorg.push_back(next[n]);
        }
        nextblue.push_back(100); nextorg.push_back(100);
        while((tot=bluedone+orgdone)<N){
            time++;
            if ((c[tot]=='O') && (orgpos==nextorg[orgdone])){
                    orgdone++;
            }
            else{
                if (orgpos>nextorg[orgdone]) orgpos--;
                if (orgpos<nextorg[orgdone]) orgpos++;
            }
            if ((c[tot]=='B') && (bluepos==nextblue[bluedone])){
                    bluedone++;
            }
            else {
                if (bluepos>nextblue[bluedone]) bluepos--;
                if (bluepos<nextblue[bluedone]) bluepos++;
            }
        }
        out<<"Case #"<<t+1<<": "<<time<<"\n";
    }

}
