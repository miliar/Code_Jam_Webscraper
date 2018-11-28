#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

struct train {
    int hour, min;
    int aHour, aMin;
    bool operator<( const train &t ) const {
        if( hour==t.hour ) return min>t.min;
        return hour>t.hour;
    }
    train( int dh, int dm, int ah=-1, int am=-1 ) {
        hour=dh; min=dm; aHour=ah; aMin=am;
    }
    train() {}
};

bool tComp(const train &a, const train &b) {
    return (a.hour==b.hour)?a.min<b.min:a.hour<b.hour;
}

FILE * in=fopen("in.txt","r");
FILE * out=fopen("out.txt","w");

const int MAXNA=500;
int N;

train getNextTrain( train cur, int T ) {
    int dH, dM, aH, aM, newATotal, newDTotal;
    newDTotal=cur.aHour*60+cur.aMin+T;
    return train( newDTotal/60, newDTotal%60 );
}

int main() {
    fscanf(in,"%d",&N);
    for( int test=1; test<=N; test++ ) {
        int T, NA, NB;
        train startA[MAXNA], startB[MAXNA];
        priority_queue<train> sA, sB;
        fscanf(in,"%d\n",&T);
        fscanf(in,"%d %d\n",&NA,&NB);
        for( int i=0; i<NA; i++ ) {
            char buf[100], buf2[100];
            int dHour, dMin, aHour, aMin;
            fscanf(in,"%s %s",buf,buf2);
            sscanf(buf,"%d:%d",&dHour,&dMin);
            sscanf(buf2,"%d:%d",&aHour,&aMin);
            startA[i]=train(dHour, dMin, aHour, aMin);
        }
        for( int i=0; i<NB; i++ ) {
            char buf[100], buf2[100];
            int dHour, dMin, aHour, aMin;
            fscanf(in,"%s %s",buf,buf2);
            sscanf(buf,"%d:%d",&dHour,&dMin);
            sscanf(buf2,"%d:%d",&aHour,&aMin);
            startB[i]=train(dHour, dMin, aHour, aMin);
        }
        sort( startA, startA+NA, tComp );
        sort( startB, startB+NB, tComp );

        int curA=0, curB=0, ansA=0, ansB=0;
        while(curA<NA || curB<NB) {
            cout << "==========" << endl;
            cout << ansA << " " << ansB << endl;
            cout << curA << " " << curB << endl;
            if( curA<NA && (curB>=NB || tComp(startA[curA],startB[curB])) ) {
                //take a train from A to B
                //check if there's one available waiting
                if(sA.empty() || tComp(startA[curA],sA.top()) ) {
                    //nothing available
                    sB.push( getNextTrain(startA[curA],T) );
                    ansA++;
                    cout << "nothing at A! ansA++" << endl;
                }
                else {
                    //use the available train
                    cout << "using train at A as " << startA[curA].hour << ":" << startA[curA].min << " leaves later than " << sA.top().hour << ":" << sA.top().min  << endl;
                    sA.pop();
                    sB.push( getNextTrain(startA[curA],T) );

                }
                curA++;
            }
            else {
                if(sB.empty() || tComp(startB[curB],sB.top()) ) {
                    //nothing available
                    sA.push( getNextTrain(startB[curB],T) );
                    ansB++;
                    cout << "nothing at B! ansB++" << endl;
                }
                else {
                    //use the available train
                    cout << "using train at B as " << startB[curB].hour << ":" << startB[curB].min << " leaves later than " << sB.top().hour << ":" << sB.top().min  << endl;

                    sB.pop();
                    sA.push( getNextTrain(startB[curB],T) );
                }
                curB++;
            }
        }

        fprintf(out,"Case #%d: %d %d\n",test,ansA,ansB);
    }

    return 0;
}

