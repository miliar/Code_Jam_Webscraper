#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QVector>
#include <cstdio>


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

        int L;
        in >> L;

        int H;
        in >> H;

        QVector<int> f;
        for (int j=0; j<N; ++j) {
            int next;
            in >> next;
            f << next;
        }

        int k;
        for ( k=L; k<=H; ++k) {
            bool good = true;
            for (int l=0; l<N; ++l) {
                if (k % f[l] != 0 && f[l] % k != 0) {
                    good = false;
                    break;
                }
            }
            if (good) break;
        }
        if (k<=H) {
            out << "Case #" << i+1 << ": " << k << endl;
        } else {
            out << "Case #" << i+1 << ": " << "NO" << endl;
        }
       // out << "Case #" << i+1 << ": " << ret << endl;

    }

    a.exit();
}
