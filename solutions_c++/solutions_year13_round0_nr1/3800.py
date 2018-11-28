#include<string.h>
#include<map>
#include<iostream>
#include<utility>
#define DBG 0
using namespace std;
void process(char arr[][6]) {
    int status =0;
    if(DBG) cout<<"\nInside process, the arr contains:\n"<<"\n";
    for(int i =0; i<4;i++) {
        if(DBG) cout<<arr[i]<<"\n";
    }
    int numDotR[6], numXR[6], numOR[6], numTR[6], diagX[3];
    int numDotC[6], numXC[6], numOC[6], numTC[6], diagO[3];
    //numDotR[6]= numXR[6]= numOR[6]= numTR[6]={0,0,0,0,0,0};
    //numDotC[6]= numXC[6]= numOC[6]= numTC[6]={0,0,0,0,0,0};
    for(int i=0;i<6;i++) {
        numDotR[i]=0;
        numDotC[i]=0;
        numXR[i]=0;
        numXC[i]=0;
        numOR[i]=0;
        numOC[i]=0;
        numTR[i]=0;
        numTC[i]=0;
    } 
    diagX[0]=0;diagX[1]=0; diagX[2]=0;
    diagO[0]=0;diagO[1]=0; diagO[2]=0;
    
    for(int i =0; i<4;i++) {
        for(int j =0; j<4;j++) {
            switch(arr[i][j]) {
                case 'X':
                    numXR[i]++;
                    numXC[j]++;
                    if(i==j)
                        diagX[0]++;
                    else if ((i+j)==3) 
                        diagX[1]++;
                    break;
                case 'O':
                    numOR[i]++;
                    numOC[j]++;
                    if(i==j)
                        diagO[0]++;
                    else if ((i+j)==3) 
                        diagO[1]++;
                    break;
                case '.':
                    numDotR[i]++;
                    numDotC[j]++;
                    break;
                case 'T':
                    numTR[i]++;
                    numTC[j]++;
                    if(i==j) {
                        diagX[0]++; diagO[0]++;
                    }
                    else if ((i+j)==3) {
                        diagX[1]++; diagO[1]++;
                    } 
                    
                    break;
            } 
            
        }
    }
    int totalDots=0;
    for(int i=0;i<4; i++) {
        //X won
        if(numXR[i]==4 || numXC[i]==4 || ((numXR[i]==3 && numTR[i]==1) || (numXC[i]==3 && numTC[i]==1))) {
            status=1; 
            break;
        }
        //O won
        if(numOR[i]==4 || numOC[i]==4 || ((numOR[i]==3 && numTR[i]==1) || (numOC[i]==3 && numTC[i]==1))) {
            status=2; 
            break;
        }
        totalDots += numDotR[i];
    }
    if(diagX[0]==4 || diagX[1]==4)
        status = 1;
    else if(diagO[0]==4 || diagO[1]==4)
        status = 2;
    if(status==0 && totalDots==0)
        status = 3;
    if(status==0)
        status = 4;
    
    switch(status) {
        case 1:
            cout<<"X won";
            break;
        case 2:
            cout<<"O won";
            break;
        case 3:
            cout<<"Draw";
            break;
        case 4:
            cout<<"Game has not completed";
            break;
    }
}

int main() {
    int T;
    char arr[6][6];
    cin>>T;
    int count=0;
    while(T>0) {
        count++;
        T--;
        if(DBG) cout<<"\nInside main, taking input\n";
        for(int i =0; i<4;i++) {
            cin>>arr[i];
            if(DBG) cout<<arr[i]<<"\n";
        }
        cout<<"Case #"<<count<<": ";
        process(arr);
        cout<<"\n";
    }
    return 0;
}
