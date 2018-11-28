#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class Time {
public: 
    int h;
    int m;
    void add(int i) {
        m += i;
        while(m>=60) {
            m-=60;
            h+=1;
        }
    };
    void subtract(int i) {
        m -= i;
        while(m<0) {
            m+=60;
            h-=1;
        }
    };
    int compare(Time t) {
        return (h-t.h)*60 + m-t.m;
    };
    static vector <Time> sortTime (vector <Time> toSort) {
        int i, j;
        vector <Time> SORTED;
        //if(i==CHK) cout<<"Before sorting: ";
        //for(i = 0; i<toSort.size(); i++) {
        //    if(i==CHK) cout<<"["<<toSort[i].h<<"h"<<toSort[i].m<<"]";
        //}
        //if(i==CHK) cout<<endl;
        int times = toSort.size();
        for(i = 0; i<times; i++) {
            int min = 0;
            for(j = 0; j<toSort.size(); j++) {
                if(toSort[j].compare(toSort[min])<0) {
                    min = j;
                };
            }
            SORTED.push_back(toSort[min]);
            toSort.erase(toSort.begin()+min);
        }
        //if(i==CHK) cout<<"After sorting: ";
        //for(i = 0; i<SORTED.size(); i++) {
        //    if(i==CHK) cout<<"["<<SORTED[i].h<<"h"<<SORTED[i].m<<"]";
        //}
        //if(i==CHK) cout<<endl;
        return SORTED;
    };
};

class TrainTimetable {
private: 
    vector <Time> ABd;
    vector <Time> ABa;
    vector <Time> BAd;
    vector <Time> BAa;
public: 
    void doit() {
        int CHK = -1;
        ifstream fin("B-large.in");
        ofstream fout("A.out.txt");
        int N;
        int T;
        int NA, NB;
        fin>>N;
        fin.ignore(1,'\n');
        int i, j, k;
        Time temp_time;
        for(i = 0; i<N; i++) {
            fin>>T;
            fin.ignore(1,'\n');
            fin>>NA;
            fin.ignore(1,' ');
            fin>>NB;
            fin.ignore(1,'\n');
            for(j = 0; j<NA; j++) {
                fin>>temp_time.h;
                fin.ignore(1,':');
                fin>>temp_time.m;
                fin.ignore(1,' ');
                ABd.push_back(temp_time);
                fin>>temp_time.h;
                fin.ignore(1,':');
                fin>>temp_time.m;
                fin.ignore(1,'\n');
                ABa.push_back(temp_time);
            }
            for(j = 0; j<NB; j++) {
                fin>>temp_time.h;
                fin.ignore(1,':');
                fin>>temp_time.m;
                fin.ignore(1,' ');
                BAd.push_back(temp_time);
                fin>>temp_time.h;
                fin.ignore(1,':');
                fin>>temp_time.m;
                fin.ignore(1,'\n');
                BAa.push_back(temp_time);
            }
            int A = 0;
            int B = 0;
            int train_used = 0;
            ABd = Time::sortTime(ABd);
            BAd = Time::sortTime(BAd);
            for(j = 0; j<NA; j++) {
                if(i==CHK) cout<<"Process A to B: "<<ABd[j].h<<"h"<<ABd[j].m<<endl;
                int train_free = 0;
                bool found = false;
                //dept a to b needs a train
                for(k = 0; k<NB; k++) {
                    Time t = BAa[k];
                    t.add(T);
                    if(t.compare(ABd[j])<=0) {
                        if(i==CHK) cout<<" Train arrived: "<<BAa[k].h<<"h"<<BAa[k].m<<endl;
                        if(i==CHK) cout<<" Ready: "<<t.h<<"h"<<t.m<<endl;
                        train_free += 1;
                    };
                }
                if(train_free>train_used) {
                    found = true;
                    train_used += 1;
                    if(i==CHK) cout<<" Using an existing train"<<endl;
                };
                if(!found) {
                    A += 1;
                    if(i==CHK) cout<<A<<endl;
                };
            }
            train_used = 0;
            for(j = 0; j<NB; j++) {
                if(i==CHK) cout<<"Process B to A: "<<BAd[j].h<<"h"<<BAd[j].m<<endl;
                int train_free = 0;
                bool found = false;
                //dept b to a needs a train
                for(k = 0; k<NA; k++) {
                    Time t = ABa[k];
                    t.add(T);
                    if(t.compare(BAd[j])<=0) {
                        if(i==CHK) cout<<" Train arrived: "<<ABa[k].h<<"h"<<ABa[k].m<<endl;
                        if(i==CHK) cout<<" Ready: "<<t.h<<"h"<<t.m<<endl;
                        train_free += 1;
                    };
                }
                if(train_free>train_used) {
                    found = true;
                    train_used += 1;
                    if(i==CHK) cout<<" Using an existing train"<<endl;
                };
                if(!found) {
                    B += 1;
                    if(i==CHK) cout<<B<<endl;
                };
            }
            fout<<"Case #"<<i+1<<": ";
            fout<<A<<" "<<B;
            fout<<endl;
            if(i==CHK) cout<<"Case #"<<i+1<<": ";
            if(i==CHK) cout<<A<<" "<<B;
            if(i==CHK) cout<<endl;
            ABd.clear();
            ABa.clear();
            BAd.clear();
            BAa.clear();
        }
        fin.close();
        fout.close();
    };
};

int main() {
    TrainTimetable S;
    S.doit();
    //system("PAUSE");
    return 0;
};
