#include <iostream>
#include <qt4/Qt/QtCore>
#include <sstream>
#include <math.h>

struct Ppl;

class Queue
{
public:


    QList<Ppl*> ppl;
} Queue;

struct Ppl
{
    Ppl(int sizee) { size = sizee; isInKart = false;}

    unsigned long long size;
    bool isInKart;
};

int main()
{
    QFile read("C-small-attempt0.in");
    QFile write("C-small-attempt0.out");

    read.open(QIODevice::ReadOnly | QIODevice::Text);
    write.open(QIODevice::WriteOnly | QIODevice::Text);

    while(!read.atEnd()){
        QString line = read.readLine();
        unsigned long long T = line.toInt();

        for(int counter = 1; counter <= T; counter++){
            line = read.readLine();
            QStringList list = line.split(" ");

            unsigned long long R = list[0].toInt(), k = list[1].toInt(), N = list[2].toInt();
            line = read.readLine();

            QStringList g = line.split(" ");

            foreach(QString s, g){
                Queue.ppl.push_back(new Ppl(s.toInt()));
            }

            QString testCase;
            int money = 0;

            for(int counterR = 1; counterR <= R; counterR++){
                unsigned long long currentOnKart = 0;

                if(Queue.ppl.empty()){
                    break;
                }

                foreach(Ppl* ppl, Queue.ppl){
                    if(currentOnKart + ppl->size <= k){
                        currentOnKart += ppl->size;

                        money += ppl->size;
                        ppl->isInKart = true;
                    }
                    else{
                        break;
                    }
                }

                for(QList<Ppl*>::iterator it = Queue.ppl.begin(), end = Queue.ppl.end(); it != end;){
                    if((*it)->isInKart){
                        Ppl* ppl = *it;

                        ppl->isInKart = false;
                        Queue.ppl.erase(it);

                        Queue.ppl.push_back(ppl);

                        it = Queue.ppl.begin();
                        end = Queue.ppl.end();
                    }
                    else{
                        it++;
                    }
                }
            }

            Queue.ppl.clear();

            testCase = QString("Case #%1: %2\n").arg(QString::number(counter)).arg(QString::number(money));
            write.write(testCase.toAscii());
        }
    }

    read.close();
    write.close();

    return 0;
}

