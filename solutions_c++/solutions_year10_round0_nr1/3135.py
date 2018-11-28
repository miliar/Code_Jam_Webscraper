#include <QtCore/QCoreApplication>
#include <QFile>
#include <QDebug>
#include <cmath>


int main(int argc, char *argv[])
{
    QFile file("A-large.in");
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
        int N = buf.section(' ',0,0).toInt();
        int K = buf.section(' ',1,1).toInt();
        bool light = true;
        for(int j=0;j<N;j++){
            int swap_time = pow(2,j);
            int result = K/swap_time;
            if(result%2!=1){
                light=false;
                break;
            }
        }
        if(light)
            out<<"Case #"<<i+1<<": ON\n";
        else out<<"Case #"<<i+1<<": OFF\n";
    }
    qDebug()<<"FINISH!!!";
    return 0;
}
