#include <QtCore/QCoreApplication>
#include <QFile>
#include <QDebug>
#include <cmath>
#include <QQueue>


int main(int argc, char *argv[])
{
    QFile file("C-small-attempt0.in");
    if(!file.open(QIODevice::ReadOnly|QIODevice::Text)){
        return 0;
    }
    QFile out_file("output.txt");
    if(!out_file.open(QIODevice::WriteOnly|QIODevice::Text)){
        return 0;
    }
    QTextStream in(&file);
    QTextStream out(&out_file);

    int case_number = in.readLine().toInt();
    for(int i = 0;i<case_number;i++){
        QString buf = in.readLine();
        int R = buf.section(' ',0,0).toInt();
        int k = buf.section(' ',1,1).toInt();
        int N = buf.section(' ',2,2).toInt();
        buf = in.readLine();

        int all_profit=0;
        QQueue<int> qUsed,qHave;
        for(int j=0;j<N;j++){
            qHave.enqueue(buf.section(' ',j,j).toInt());
        }
        //qDebug()<<R<<k<<N;
        for(int j =0;j<R;j++){
            int tmpPeople = 0;
            for(int l=0;l<N;l++){
                tmpPeople+=qHave.head();
                if(tmpPeople<=k){
                    qUsed.enqueue(qHave.dequeue());
                    continue;
                }else{
                    tmpPeople-=qHave.head();
                    break;
                }
            }
            all_profit+=tmpPeople;
            while(!qUsed.isEmpty())
                qHave.enqueue(qUsed.dequeue());
        }
        out<<"Case #"<<i+1<<": "<<all_profit<<"\n";

    }
    qDebug()<<"Finish";
    return 1;
}
