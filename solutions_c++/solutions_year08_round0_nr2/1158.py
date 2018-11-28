#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
using namespace std;

bool _debug = true;

struct sTime{
    int dHours,dMinutes;

    void operator ++(int pInt){
        dMinutes++;
        if(dMinutes >= 60){
            dMinutes = 0;
            dHours++;
        }
    }
    void operator +=(unsigned pInt){
        dMinutes += pInt;
        while(dMinutes >= 60){
            dMinutes -= 60;
            dHours++;
        }
    }
    bool operator ==(sTime pTime){
        return (pTime.dHours == dHours && pTime.dMinutes == dMinutes);
    }
    void fParse(string &pInput){
        char lBuff[6];
        strcpy(lBuff, pInput.c_str());
        lBuff[2] = '\0';
        dHours = atoi(&lBuff[0]);
        dMinutes = atoi(&lBuff[3]);
    }
    string toString(){
        string lRet = "";
        char lBuff[6];
        if(dHours < 10) lRet += "0";
        lRet += itoa(dHours,lBuff,10);
        lRet += ":";
        if(dMinutes < 10) lRet += "0";
        lRet += itoa(dMinutes,lBuff,10);
        return lRet;
    }
    sTime(string &pInput){
        fParse(pInput);
    }
    sTime(){
        dHours = 0;
        dMinutes = 0;
    }
};

struct sTrip{
    sTime dArrival, dDeparture;
};

struct sStation{
    vector<sTrip> dTrips;
    int dResult, dTrains;

    sStation(){
        dResult = 0;
        dTrains = 0;
    }
};

struct sCase{
    sStation A;
    sStation B;
};

struct sInput{
    vector<sCase> dCases;

    sInput(){
        int N;
        cin >> N;
        for(; N > 0; N--){
            sCase lCurCase;

            int T;
            cin >> T;

            int NA, NB;
            cin >> NA;
            cin >> NB;

            string lBuff;

            for(; NA > 0; NA--){
                sTrip lCurTrip;
                sTime lCurTime;

                cin >> lBuff;
                lCurTime.fParse(lBuff);
                lCurTrip.dDeparture = lCurTime;

                cin >> lBuff;
                lCurTime.fParse(lBuff);
                lCurTime += T;
                lCurTrip.dArrival = lCurTime;

                lCurCase.A.dTrips.push_back(lCurTrip);

                if(_debug) cout << lCurTrip.dDeparture.toString() << " a train quit A, and arrive at "
                    << lCurTrip.dArrival.toString() << endl;

            }

            for(; NB > 0; NB--){
                sTrip lCurTrip;
                sTime lCurTime;

                cin >> lBuff;
                lCurTime.fParse(lBuff);
                lCurTrip.dDeparture = lCurTime;

                cin >> lBuff;
                lCurTime.fParse(lBuff);
                lCurTime += T;
                lCurTrip.dArrival = lCurTime;

                lCurCase.B.dTrips.push_back(lCurTrip);

                if(_debug) cout << lCurTrip.dDeparture.toString() << " a train quit B, and arrive at "
                    << lCurTrip.dArrival.toString() << endl;
            }

            dCases.push_back(lCurCase);
            if(_debug) cout << endl;
        }
    }

    void fSimulate(){
        sTime lCurTime;
        int lIndex, lIndex2;
        for(lIndex = 0; lIndex < dCases.size(); lIndex++){
            lCurTime.dHours = 0;
            lCurTime.dMinutes = 0;
            while(lCurTime.dHours < 24){

                int lTrainArriveA = 0;
                int lTrainQuitA = 0;

                int lTrainArriveB = 0;
                int lTrainQuitB = 0;

                for(lIndex2 = 0; lIndex2 < dCases[lIndex].A.dTrips.size(); lIndex2++){
                    // For each train in A
                    if(dCases[lIndex].A.dTrips[lIndex2].dDeparture == lCurTime){
                        lTrainQuitA++;
                        if(_debug) cout << lCurTime.toString() << " Quit A" << endl;
                    }
                    if(dCases[lIndex].A.dTrips[lIndex2].dArrival == lCurTime){
                        lTrainArriveB++;
                        if(_debug) cout << lCurTime.toString() << " Arriving B" << endl;
                    }
                }

                for(lIndex2 = 0; lIndex2 < dCases[lIndex].B.dTrips.size(); lIndex2++){
                    // For each train in B
                    if(dCases[lIndex].B.dTrips[lIndex2].dDeparture == lCurTime){
                        lTrainQuitB++;
                        if(_debug) cout << lCurTime.toString() << " Quiting B" << endl;
                    }
                    if(dCases[lIndex].B.dTrips[lIndex2].dArrival == lCurTime){
                        lTrainArriveA++;
                        if(_debug) cout << lCurTime.toString() << " Arrive A" << endl;
                    }
                }

                if(lTrainArriveA || lTrainQuitA || lTrainArriveB || lTrainQuitB){
                /*    if(_debug) cout << lCurTime.toString() << " Arriving A/B : " << lTrainArriveA << "/"
                        << lTrainArriveB << " Quiting A/B : "<< lTrainQuitA << "/"
                        << lTrainQuitB << endl;*/

                    dCases[lIndex].A.dTrains += lTrainArriveA;
                    dCases[lIndex].B.dTrains += lTrainArriveB;

                    while(lTrainQuitA > 0){
                        if(dCases[lIndex].A.dTrains == 0){
                            // If no train available, we need to add one at start
                            dCases[lIndex].A.dResult++;
                            if(_debug) cout << "Adding train to A start" << endl;
                        }
                        else{
                            dCases[lIndex].A.dTrains--;
                        }
                        lTrainQuitA--;
                    }

                    while(lTrainQuitB > 0){
                        if(dCases[lIndex].B.dTrains == 0){
                            // If no train available, we need to add one at start
                            dCases[lIndex].B.dResult++;
                            if(_debug) cout << "Adding train to B start" << endl;
                        }
                        else{
                            dCases[lIndex].B.dTrains--;
                        }
                        lTrainQuitB--;
                    }

                    if(_debug) cout << "Station status A/B : " << dCases[lIndex].A.dTrains
                        << "/" << dCases[lIndex].B.dTrains << endl;
                }

                lCurTime++;
            }
            if(_debug) cout << "Results : " << dCases[lIndex].A.dResult << "/"
                        << dCases[lIndex].B.dResult << endl << endl;
        }
    }

    void fOutput(){
        int lIndex;
        for(lIndex = 1; lIndex <= dCases.size(); lIndex++){
            cout << "Case #" << lIndex << ": " << dCases[lIndex-1].A.dResult << " " <<
                dCases[lIndex-1].B.dResult << endl;
        }
    }
};

int main(){
    sInput lInput;
    if(_debug) cout << endl;
    lInput.fSimulate();
    lInput.fOutput();

    return 0;
}
