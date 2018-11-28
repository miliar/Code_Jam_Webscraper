#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;


string status[4]={"X won","O won","Draw","Game has not completed"};

class board{
    public:
    char arr[4][4];
    
    bool hasDot();
    bool checkWin(char ch);
    int getStat();
    int getStatus();
    void print();
};

bool
board::hasDot(){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(arr[i][j]=='.'){
                return true;
            }
        }
    }
    return false;  
}

int 
board::getStat(){
    //X win, return 0; O win, return 1; No one win, return 2;
    //check sum of rows
    for(int i=0;i<4;i++){
        int sum=0;
        for(int j=0;j<4;j++){
            sum+=(arr[i][j]-'.');
        }
        //cout<<sum<<endl;
        if(sum==168 || sum==164){return 0;}
        else if(sum==132 || sum==137){return 1;}
    }
    //check sum of cols
    for(int j=0;j<4;j++){
        int sum=0;
        for(int i=0;i<4;i++){
            sum+=(arr[i][j]-'.');
        }
        //cout<<sum<<endl;
        if(sum==168 || sum==164){return 0;}
        else if(sum==132 || sum==137){return 1;}
    }
    //check diagonals
    int sum1=arr[0][0]-'.'+arr[1][1]-'.'+arr[2][2]-'.'+arr[3][3]-'.';
    int sum2=arr[0][3]-'.'+arr[1][2]-'.'+arr[2][1]-'.'+arr[3][0]-'.';
    //cout<<sum1<<endl;
    //cout<<sum2<<endl;
    if(sum1==168 || sum1==164){return 0;}
        else if(sum1==132 || sum1==137){return 1;}
    if(sum2==168 || sum2==164){return 0;}
        else if(sum2==132 || sum2==137){return 1;}
    return 2;
}


int 
board::getStatus(){
    int val=getStat();
    if(hasDot()){
        if(val==0){return 0;}
        else if(val==1){return 1;}
        else if(val==2){return 3;}
    }else{
        if(val==0){return 0;}
        else if(val==1){return 1;}
        else if(val==2){return 2;}
    }    
    return 0;
}

void
board::print(){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            printf("%c ", arr[i][j]);
        }
        cout<<endl;
    }
}

int main(){
    int casenum;
    
    scanf("%d\n",&casenum);

    for(int k=0;k<casenum;k++){
        board bd;
        for(int i=0;i<4;i++){
            scanf("%c %c %c %c\n",&bd.arr[i][0],&bd.arr[i][1],&bd.arr[i][2],&bd.arr[i][3]);
        }
        int res=bd.getStatus();
        //bd.print();
        printf("Case #%d: ",k+1);
        cout<<status[res]<<endl;
    }

    return 0;
}
