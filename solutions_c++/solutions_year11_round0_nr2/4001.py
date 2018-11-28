#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QList>

QChar combine(QString list, const QList<QString> & comb) {
    if (list.size() < 2) return '0';
    for (int i=0; i<comb.size(); ++i) {
        if (comb[i][0] == list[list.size()-2] && comb[i][1] == list[list.size()-1]
            || comb[i][1] == list[list.size()-2] && comb[i][0] == list[list.size()-1]) {
            return comb[i][2];
        }
    }
    return '0';
}

bool canOppose(QString list, QList<QString> & opp) {
    if (list.size() < 2) return false;
    for (int i=0; i<opp.size(); ++i) {
        if (list.contains(opp[i][0]) && list.contains(opp[i][1])) return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QFile file("B-large.in");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << file.errorString();
        return 1;
    }

    QFile data("outlarge.txt");
    data.open(QFile::WriteOnly | QFile::Truncate);

    QTextStream in(&file);
    QTextStream out(&data);

    int T;
    in >> T;
    in.readLine();

    for (int i = 0; i<T; ++i) {
        int C;
        in >> C;
        QList<QString> comb;
        for (int j = 0; j < C; ++j) {
            QString x;
            in >> x;
            comb << x;
        }
     //   qDebug() << comb;

        int D;
        in >> D;
        QList<QString> opp;
        for (int k = 0; k < D; ++k) {
            QString x;
            in >> x;
            opp << x;
        }
      //  qDebug() << opp;

        int N;
        in >> N;

        QString invoked;
        in >> invoked;
        //qDebug() << invoked;
        QString list;

        for (int l = 0; l < N; ++l) {
           list.push_back(invoked[l]);
           QChar le = combine(list, comb);
           if (le != '0') {
               list.chop(2);
               list += le;
           } else if (canOppose(list, opp)) {
               list.clear();
           }
        }

        if (list.size() == 0) out << "Case #" << i+1 << ": []" << endl;
        else {
           out << "Case #" << i+1 << ": [";
           for (int m = 0; m < list.size()-1; ++m) {
               out << list[m] << ", ";
           }
           out << list[list.size()-1] << "]";
           out << endl;
        }
    }

    file.close();

    a.exit();
}
