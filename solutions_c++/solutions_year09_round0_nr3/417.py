#include <QtCore>

QTextStream in(stdin);
QTextStream out(stdout);

QString wel = "welcome to code jam";
QString text;
int dp[20][501];

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
    int N;
    in >> N;
    in.readLine();

    QRegExp rx("[^welcomtdja ]");


    for(int cas = 1; cas <= N; cas++) {
        text = in.readLine();
        text.remove(rx);

        for(int x=0;x<20;x++)
            for(int y=0;y<501;y++)
                dp[x][y] = -1;

        out << QString("Case #%1: %2\n").arg(cas).arg(findNext(0, 0),4,10,QLatin1Char('0'));
    }
    return 0;
}
