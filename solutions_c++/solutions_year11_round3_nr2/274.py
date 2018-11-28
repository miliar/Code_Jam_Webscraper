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

    long long int T;
    in >> T;
    in.readLine();

    for (long long int i = 0; i<T; ++i) {
        long long int L;
        in >> L;

        long long int t;
        in >> t;

        long long int N;
        in >> N;

        long long int C;
        in >> C;

        QVector<long long int> a;
        for (long long int j=0; j<C; ++j) {
            long long int next;
            in >> next;
            a << next;
        }

        QVector<long long int> b;
        while (b.size()<N) {
            b << a;
        }
        b.remove(N, b.size()-N);

        t /= 2;

        long long int tc = 0;
        long long int k;
        for (k=0; k<b.size(); ++k) {
            if ((tc + b[k]) <= t) {
                tc += b[k];
            } else {
                break;
            }
        }

        if (k < b.size()) {
            b[k] -= t - tc;
            b.insert(k, t - tc);
        }

        QVector<long long int> bfast = b;
        bfast << 0;
        bfast.remove(0, k+1);

        QVector<long long int> bslow = b;
        bslow << 0;
        bslow.remove(k+1, bslow.size()-k-1);

        qSort(bfast);
        long long int ret = 0;
        for (long long int j=0; j<L && bfast.size()>0; ++j) {
            ret += bfast.back();
            bfast.pop_back();
        }

        for (long long int j=0; j<bfast.size(); ++j) {
            ret += bfast[j] * 2;
        }
        for (long long int j=0; j<bslow.size(); ++j) {
            ret += bslow[j] * 2;
        }

        out << "Case #" << i+1 << ": " << ret << endl;

       // qDebug() << b << bfast << bslow << k;
    }

    a.exit();
}
