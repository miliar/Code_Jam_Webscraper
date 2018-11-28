#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QDebug>

#include <QMap>

QMap<QChar, QChar> mapping;

QString solveCase(QTextStream *input) {
    QString line=input->readLine();
    QStringList tokens = line.split(' ');
    ulong start = tokens.takeFirst().toULong();
    ulong end = tokens.takeFirst().toULong();

    QMap<QString, QString> values;

    for(ulong i=start; i<=end; i++) {
        QString num = QString("%1").arg(i);
        for(int j=1; j<num.length(); j++) {
            QString swapped = QString("%1%2").arg(num.right(j), num.left(num.length()-j));
            ulong swappedNum = swapped.toULong();
            if(swappedNum != i && swappedNum >= start && swappedNum <= end && swappedNum < i) {
                if(values.value(num, QString() ) != swapped && values.value(swapped, QString()) != num)
                    values.insertMulti(num, swapped);
            }
        }
    }
    return QString("%1").arg(values.size());
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QStringList params = a.arguments();
    QString filename = params.at(1);
    QFile input(filename);
    input.open(QFile::ReadOnly);
    QTextStream iStream(&input);
    QTextStream output(stdout);
    int cases = iStream.readLine().toInt();
    for(int i=0; i<cases; i++) {
        output << QString("Case #%1: %2\n").arg(i+1).arg(solveCase(&iStream));
    }

    input.close();
    return 0;

}
