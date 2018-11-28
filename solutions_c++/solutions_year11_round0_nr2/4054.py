#include <algorithm>
#include <vector>
#include <iostream>
#include <cstdio>
#include <fstream>
#include <QString>
#include <QList>
#include <QRegExp>


using namespace std;


class Magika{

private:

    QList<QString> opps_;
    QList<QRegExp> oppsReg;
    QList<QString> combs_;
    QString seq_;
    QString elements;
    //    vector<char> elements;
public:
    Magika(int C, char**combs, int D, char** opps, int N, char* seq): seq_(seq)  {

        //        Comb = new QStringList;
        while(C--){
            combs_ << combs[C];
        }

        while(D--){
            opps_ << opps[D];
        }

        QString req;
        for (int i = 0 ; i < opps_.size() ; i++){
            req.append(opps_[i][0]);
            req.append(".*");
            req.append(opps_[i][1]);
            QRegExp r(req);
            oppsReg.append(r);
            req.clear();
            req.append(opps_[i][1]);
            req.append(".*");
            req.append(opps_[i][0]);
            QRegExp e(req);
            oppsReg.append(e);

        }

    }


    void checkOpps(){

        for (int i = 0 ; i < oppsReg.size() ; i++){
            if(elements.indexOf(oppsReg[i]) != -1)
                elements.clear();
        }

    }

    void checkCombs(){
        for (int i = 0 ; i < combs_.size() ; i++){
            QString reqex;
            reqex.append(combs_[i][0]);
            reqex.append(combs_[i][1]);
            QString after;
            after.append(combs_[i][2]);
            elements.replace(reqex,after);

            reqex.clear();;
            reqex.append(combs_[i][1]);
            reqex.append(combs_[i][0]);
            after.clear();
            after.append(combs_[i][2]);
            elements.replace(reqex,after);
        }
    }

    QString process(){

        for(int index = 0 ; index <seq_.size() ; index++){
            elements.append(seq_[index]);
            checkCombs();
            checkOpps();
        }

        return elements;
    }




};




int main(){

    FILE* test = fopen("test", "r");

    fstream output;
    output.open("file.out", ios::out);

    if ( test != NULL ) {

        int T;
        fscanf(test, "%d", &T);

        for (int testCases = 0 ; testCases < T ; testCases++){

            //            stringstream TCline;

            // Reading combinations
            int C ;
            fscanf(test, "%d", &C);
            char **combinations = new char*[C];
            for(int i = 0 ; i < C ; i++) combinations[i] = new char[3];

            for(int combs = 0 ; combs < C; combs++){
                fscanf(test , "%s", combinations[combs]);

            }

            // Reading oppositions
            int D ;
            fscanf(test, "%d", &D);
            char **oppositions = new char*[D];
            for(int i = 0 ; i < D ; i++) oppositions[i] = new char[3];
            for(int opps = 0 ; opps < D; opps++){
                fscanf(test , "%s", oppositions[opps]);

            }

            int N ;
            fscanf(test, "%d", &N);

            char* seq = new char[N];
            fscanf(test, "%s", seq);

            Magika M(C,combinations,D,oppositions,N, seq);

            QString out = M.process();

            QString outMod;
            outMod += "Case #" ;

            outMod.append(QString("%1").arg(testCases+1));
            outMod+= ": [";
            if (out.size()) outMod += out[0];
            for (int index = 1 ; index< out.size() ; index++){
                outMod += ", ";
                outMod += out[index];
            }
            outMod += "]\n";
            output << outMod.toStdString().c_str();

            //test ops ends here
        }
//        output<<endl;


    }else
        cout << "Unable to open file";
    return 0;

}
