/* 
 * File:   main.cpp
 * Author: whoAreYou
 *
 * Created on 2011年5月7日, 下午 4:47
 */

#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

class staterb{
public:
    int position, target;
    bool ontarget(){
        return position==target;
    }

    void onestep(){
        if (target>position)
            position++;
        else if(target<position)
            position--;
    }
    

};

/*
 * 
 */
int main() {
    int caseno, buno, currno=1;
    char oor[101];
    int step[101], opointer[101], bpointer[101], oc, bc;

    cin >> caseno;

    while (caseno>=currno){
        for (int i=0; i<101; i++){
            opointer[i]=bpointer[i]=0;
        }
        oc=bc=0;
        cin >> buno;

        for (int i=0; i< buno; i++){
            cin >> oor[i] >> step[i];
            if(oor[i]=='O')
                opointer[oc++]=i;
            else
                bpointer[bc++]=i;
        }

//        for (int i=0; i< buno; i++){
//            cout << oor[i] << "" << step[i] << endl;
//        }
//        cout << endl << endl;
//        for (int i=0; i < oc; i++) cout << opointer[i] << " ";
//        cout << endl;
//        for (int i=0; i<bc; i++) cout << bpointer[i] << " ";
//        cout << endl;

        staterb ostate, bstate;
        bstate.position=ostate.position=1;
        int time=0,oc1=0, bc1=0;
        //if (oor[0]=='O')
        for(int bucount=0;buno> bucount;bucount++){
            ostate.target=step[opointer[oc1]];
            bstate.target=step[bpointer[bc1]];

            int diff;
            if (oor[bucount]=='O')
                diff=abs(step[bucount]-ostate.position);
            else
                diff=abs(step[bucount]-bstate.position);

            for (int i=0; i< diff; i++){
                if (!ostate.ontarget()){ostate.onestep();}
                if (!bstate.ontarget()){bstate.onestep();}
                time++;
            }
            time++;//pass button, the rb can move when pass button.....
            if (!ostate.ontarget()){ostate.onestep();}
            if (!bstate.ontarget()){bstate.onestep();}

            if (oor[bucount]=='O')
                oc1++;
            else
                bc1++;
        }

        cout << "Case #" << currno << ": " << time << endl;

        currno++;
    }



    return 0;
}

