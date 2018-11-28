#include <QtCore>

#define FILE_OUTPUT
#define FILE_INPUT
#define FILE_NAME "C-large.in"

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

QString wel = "welcome to code jam";
QString text;
int dp[19][500];

int findNext(int charIndex, int from)
{
    if(charIndex == wel.length()) {
        dp[charIndex][from] = 1;
        return 1;
    }

    if(dp[charIndex][from] != -1)
        return dp[charIndex][from];

    int j = from;
    int count = 0;
    while((j = text.indexOf(wel[charIndex], j)) != -1) {
        count += findNext(charIndex+1, j) % 10000;
        ++j;
    }
    count = count % 10000;

    dp[charIndex][from] = count;
    return count;
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

    uint numCases;
    in >> numCases;
    in.readLine();

    QRegExp rx("[^welcomtdja ]");

    for(uint curCase = 0; curCase < numCases; curCase++) {
        text = in.readLine();
        text.remove(rx);

        for(int x=0;x<19;x++)
            for(int y=0;y<500;y++)
                dp[x][y] = -1;

        int num = findNext(0, 0);

        out << QString("Case #%1: %2\n").arg(curCase+1).arg(num,4,10,QLatin1Char( '0'));
    }
    return 0;
}
