#include <iostream>
#include <qt4/Qt/QtCore>
#include <sstream>
#include <math.h>

int main()
{
    QFile read("A-large.in");
    QFile write("A-large.out");

    read.open(QIODevice::ReadOnly | QIODevice::Text);
    write.open(QIODevice::WriteOnly | QIODevice::Text);

    while(!read.atEnd()){
        QString line = read.readLine();
        unsigned long long times = line.toInt();

        for(int counter = 1; counter <= times; counter++){
            line = read.readLine();
            QStringList list = line.split(" ");

            int N = list[0].toInt(), K = list[1].toInt();

            QString testCase = QString("Case #%1: %2\n").arg(QString::number(counter)).arg((((K % (1 << N)) == ((1 << N) -1)) ? "ON" : "OFF"));
            write.write(testCase.toAscii());
        }
    }

    read.close();
    write.close();

    return 0;
}

