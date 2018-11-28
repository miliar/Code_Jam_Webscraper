#include <QTextStream>
#include <QStringList>
#include <QMap>
#include <QSet>

void estemtop(int p, int cur, int& cntpass, int& cntpass_s)
{
    int min = cur / 3;
    int mod = cur % 3;
    if (min >= p)
    {
        ++cntpass;
        return;
    }
    if (mod >= 1 && min + 1 >= p)
    {
        ++cntpass;
        return;
    }
    if (mod >= 2 && min + 2 >= p)
    {
        ++cntpass_s;
        return;
    }
    if (cur > 1 && min + 1 >= p) // && mod == 0
    {
        ++cntpass_s;
        return;
    }
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        int N, S, P, cntpass = 0, cntpass_s = 0;
        ins >> N >> S >> P;

        for (int j = 0; j < N; ++j)
        {
            int cur;
            ins >> cur;
            estemtop(P, cur, cntpass, cntpass_s);
        }
        out << QString("Case #%1: %2\n").arg(QString::number(i + 1), QString::number(cntpass + std::min(cntpass_s, S)));
    }

    return 0;
}
