#include <QtCore>

#define FILE_OUTPUT
#define FILE_INPUT
#define FILE_NAME "A-small-attempt2.in"

#ifdef FILE_INPUT
QTextStream in;
#else
QTextStream in(stdin);
#endif

#ifdef FILE_OUTPUT
QTextStream out;
#else
QTextStream out(stdout);
#endif


QStringList dic;
QStringList possibilities;
QStringList strs;
int posses;

void tryNext(QString cur, int x) {
    bool found = false;
    foreach(const QString &t, dic) {
        if(t.startsWith(cur)) {
            found = true;
            break;
        }
    }

    if(!found)
        return;

    if(x == strs.length()) {
        posses++;
    } else if(strs[x][0] == '(') {
        for(int i=1; i< strs[x].length();i++) {
            tryNext(cur + strs[x][i], x+1);
        }
    } else {
        tryNext(cur + strs[x], x+1);
    }
}

int main()
{
#ifdef FILE_INPUT
    QFile infile(FILE_NAME);
    if(!infile.open(QIODevice::ReadOnly))
        return -1;
    in.setDevice(&infile);
#endif

#ifdef FILE_OUTPUT
    QFile outfile(QString(FILE_NAME).replace(".in",".out"));
    if(!outfile.open(QIODevice::WriteOnly))
        return -1;
    out.setDevice(&outfile);
#endif

    int L, D, N;

    in >> L;
    in >> D;
    in >> N;

    for(int i=0; i<D;i++) {
        QString a;
        in >> a;
        dic.push_back(a);
    }

    dic.sort();

    for(int curCase = 0; curCase < N; curCase++) {
        possibilities.clear();
        strs.clear();
        posses = 0;
        QString c;
        in >> c;
        QString sda = c;

//asda(aasdbc)(aasdbc)asdasda(abc)aasd
        for(int i=0;i<c.length();i++) {
            if(c[i] == '(') {
                QString ns = c.left(i);
                if(!ns.isEmpty())
                    strs.push_back(ns);
                c.remove(0, i);
                i = 0;
            } else if(c[i] == ')') {
                QString ns = c.left(i);
                if(!ns.isEmpty())
                    strs.push_back(ns);
                c.remove(0, i+1);
                i = 0;
            }
        }
        if(!c.isEmpty())
         strs.push_back(c);

        tryNext("", 0);
        out << QString("Case #%1: %2\n").arg(curCase+1).arg(posses);
        out.flush();
    }
    return 0;
}
