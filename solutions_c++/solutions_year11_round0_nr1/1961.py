#include<iostream>
#include<queue>
#include<string>
#include<vector>


using namespace std;

int but[200];
int bot[200];

queue<int> prog[2];

int main(){
    int tz;
    cin>>tz;
    int cas = 1;
    while(tz-->0){
        int n;
        cin>>n;
        for(int i=0;i<n;i++){
            string col;
            int b;
            cin>>col>>b;
            but[i] = b;
            if(col[0]=='O'){
                bot[i]=0;
            }else{
                bot[i]=1;
            }
            prog[bot[i]].push(but[i]);
        }

        int pos[2]={1,1};
        int i=0;
        int count = 0;
        while(i<n){
            int b = bot[i];
            int p = but[i];
            //first move not b
            //
            int nb = b^1;

            int np = prog[nb].front();
            if(pos[nb]<np)
                pos[nb]++;
            else if(pos[nb]>np)
                pos[nb]--;

            if(pos[b]==but[i]){
                //push
                i++;
                prog[b].pop();
            }else if(pos[b]<but[i])
                pos[b]++;
            else
                pos[b]--;
            count++;
        }
        cout<<"Case #"<<cas<<": "<<count<<"\n";
        cas++;
    }
}
