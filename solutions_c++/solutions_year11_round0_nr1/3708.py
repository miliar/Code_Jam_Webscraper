#include <iostream>
using namespace std;

const int O=0;
const int B=1;
const int ROBOT=0;
const int BUTTON=1;
const int MAX_N=110;
int command[MAX_N][2];
int nextButtonOfThisRobotsCommand[MAX_N];
int n;

void reset(){
    n=0;
    for (int i=0;i<MAX_N;i++)
        nextButtonOfThisRobotsCommand[i]=0;
}

void preProc(){
    cin >> n;
    char temp; int place;
    for (int i=0;i<n;i++){
        cin >> temp >> place;
        command[i][ROBOT]=(temp=='B');
        command[i][BUTTON]=place;
    }
    int nextO=0,nextB=0;
    for (int i=n-1;i>=0;i--)
        if (command[i][ROBOT]==O){
            nextButtonOfThisRobotsCommand[i]=nextO;
            nextO=command[i][BUTTON];
        }else{
            nextButtonOfThisRobotsCommand[i]=nextB;
            nextB=command[i][BUTTON];
        }
    
}

int solve(){
    int ret=0;
    int next[2]={0,0};
    int curr[2]={1,1};
    for (int i=0;i<n;i++)
        if (command[i][ROBOT]==O) {next[O]=command[i][BUTTON]; break;}
    for (int i=0;i<n;i++)
        if (command[i][ROBOT]==B) {next[B]=command[i][BUTTON]; break;}
    for (int i=0;i<n;i++){
        int thisR=command[i][ROBOT],thatR=1-thisR;
        int time=abs(curr[thisR]-command[i][BUTTON])+1; //+1 baraye zadane dogme
        curr[thisR]=command[i][BUTTON];
        ret+=time;
        //cout << " + "<< time << endl;
        next[thisR]=nextButtonOfThisRobotsCommand[i];
        if (next[thatR] && abs(curr[thatR]-next[thatR])<=time)
            curr[thatR]=next[thatR];
        else if (next[thatR]){
            if (next[thatR] > curr[thatR])
                curr[thatR]+=time;
            else
                curr[thatR]-=time;
        }
    }
    return ret;

}

int Main(){
    int TEST;
    cin >> TEST;
    for (int test=1;test<=TEST;test++){
        reset();
        preProc();
        cout << "Case #" << test << ": " << solve() << endl;
    }
    return 0;
}

int main(){
    return Main();
}