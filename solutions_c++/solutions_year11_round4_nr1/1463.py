#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QVector>
#include <cstdio>
#include <math.h>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QTextStream in(stdin);
    QTextStream out(stdout);

    int T;
    in >> T;
    in.readLine();

    for (int i = 0; i<T; ++i) {
        int X;
        in >> X;

        double S;
        in >> S;

        double R;
        in >> R;

        double t;
        in >> t;

        int N;
        in >> N;

        QVector<QPair<double, int> > c;
        int lengthOfCs = 0;
        for (int j=0; j<N; ++j) {
            int B;
            in >> B;

            int E;
            in >> E;

            double w;
            in >> w;

            c << qMakePair(w, E-B);

            lengthOfCs += E-B;
        }

        c << qMakePair(double(0), X-lengthOfCs);

        qSort(c);

        double mo = 0;
        bool running = true;
        for (int k=0; k<c.size(); ++k) {
            // time for next c
            double time = c[k].second * (1 / (R + c[k].first));

            if (running) {
                if (t >= time) {
                    mo += time;
                    t -= time;
                } else {
                    mo += t;
                    mo += (c[k].second - (c[k].second * (t/time))) * (1 / (S + c[k].first));
                    running = false;
                }
            } else {
                mo += c[k].second * (1 / (S + c[k].first));
            }
        }

        printf("Case #%d: %.10f\n", i+1, mo);
       // out << "Case #" << i+1 << ": " << mo << endl;
    }

    a.exit();
}
