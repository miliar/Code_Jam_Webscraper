#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QDebug>

#include <QHash>

QMap<QChar, QChar> mapping;

QString solveCase(QTextStream *input) {
    QObject autodelete;
    QString line=input->readLine();
    QStringList tokens = line.split(' ');
    int googlers = tokens.takeFirst().toInt();
    int surprising = tokens.takeFirst().toInt();
    int p = tokens.takeFirst().toInt();
    int result = 0;

    QList<int> scores;
    foreach(QString score, tokens) {
        scores << score.toInt();
    }

    qSort(scores);
    qDebug() << "googlers: " << googlers << ", surprising: " << surprising << ", p: " << p;
    qDebug() << "scores: " << scores;
    foreach(int score, scores) {
        int remaining = score - p;
        qDebug() << "remaining for score " << score << ": " << remaining;
        if(remaining<0) continue;
        if(surprising>0) {
            if(p-(remaining/2) <=2) {
                result++;
                surprising--;
            }
        } else {
            if(p-(remaining/2) <=1) result++;
        }
    }

    return QString("%1").arg(result);
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
