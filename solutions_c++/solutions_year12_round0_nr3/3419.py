#include <QMap>
#include <QSet>
#include <QTextStream>

int fact(int n)
{
    int ret = 1;
    for(int i = 2; i <= n; ++i)
    {
        ret *= i;
    }
    return ret;
}

int cnb2(int n)
{
    return fact(n) / (2 * fact(n - 2));
}

int checknumber(int A, int B, QSet<int>& used, int cur)
{
    int cnt = 0;
    QSet<int> locused;
    locused.insert(cur);
    QString num = QString::number(cur);
    int ndig = num.size();
    QString buf = num + num;
    for(int i = 1; i < ndig; ++i)
    {
        if(buf[i] == '0')
        {
            continue;
        }
        int next = buf.mid(i, ndig).toInt();
        if (next == cur || next < A || next > B || locused.contains(next))
        {
            continue;
        }
        ++cnt;
        used.insert(next);
        locused.insert(next);
    }
    return cnt != 0 ? (cnt == 1 ? 1 : cnb2(cnt + 1)) : 0;
}

int cntpairs(int A, int B)
{
    long sum = 0;
    QSet<int> used;

    for (long i = A; i <= B; ++i)
    {
        if (used.contains(i))
        {
            continue;
        }
        sum += checknumber(A, B, used, i);
    }
    return sum;
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        int A, B;
        ins >> A >> B;

        out << QString("Case #%1: %2\n").arg(QString::number(i + 1), QString::number(cntpairs(A, B)));
    }

    return 0;
}
