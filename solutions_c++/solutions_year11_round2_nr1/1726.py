#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QVector>
#include <cstdio>
#include <QPair>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QTextStream in(stdin);
    QTextStream out(stdout);

    int T;
    in >> T;
    in.readLine();

    for (int i = 0; i<T; ++i) {
        int N;
        in >> N;
        in.readLine();
        //qDebug() << N;

        QVector<QVector<char> >  matrix;
        for (int j=0; j<N; ++j) {
            matrix << QVector<char>();
            for (int k=0; k<N; ++k) {
               char next;
               in >> next;
               matrix.back() << next;
            }
            in.readLine();
        }

        QVector<QPair<double, double> > wp(N);
        for (int j=0; j<N; ++j) {
            for (int k=0; k<N; ++k) {
                switch(matrix[j][k]) {
                case '.':
                    break;
                case '0':
                    ++wp[j].second;
                    break;
                case '1':
                    ++wp[j].second;
                    ++wp[j].first;
                    break;
                }
            }
        }

        QVector<double> owp;
        for (int j=0; j<N; ++j) {
            double cowp = 0;
            double noo = 0;
            for (int k=0; k<N; ++k) {
                switch(matrix[j][k]) {
                case '.':
                    break;
                case '0':
                    ++noo;
                    cowp += (wp[k].first - 1) / (wp[k].second - 1);
                    break;
                case '1':
                    ++noo;
                    cowp += (wp[k].first) / (wp[k].second - 1);
                    break;
                }
            }
            owp << cowp/noo;
        }

        QVector<double> oowp;
        for (int j=0; j<N; ++j) {
            double coowp = 0;
            double noo = 0;
            for (int k=0; k<N; ++k) {
                if (matrix[j][k] != '.') {
                    ++noo;
                    coowp += owp[k];
                }
            }
            oowp << coowp / noo;
        }

        out << "Case #" << i+1 << ":" << endl;

        for (int j=0; j<N; ++j) {
            printf("%.10f\n", (0.25*wp[j].first/wp[j].second + 0.5*owp[j] + 0.25*oowp[j]));
        }

       // qDebug() << matrix;
    }
    a.exit();
}
