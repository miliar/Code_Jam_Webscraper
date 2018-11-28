#include <QtCore/QCoreApplication>

#include <QStringList>
#include <QFile>
#include <QTextStream>

class Test
{
public:
    QStringList picture;

    QStringList res;

    int R;
    int C;

};

Test*
  readTest(QTextStream& in)
{
    Test* res = new Test;

    in >> res->R;
    in >> res->C;
    QString buf;
    for (int i =0 ; i < res->R; i++)
    {
        in >> buf;
        res->picture.append(buf);
    }

    return res;
};

void
        solve(Test *test)
{

    bool possible = true;
    for (int r = 0; r < test->R; r++)
    {
        if (!possible)
            break;
        for (int c = 0; c <test-> C; c++)
        {
            int ind = test->picture[r].indexOf("##", c);
            if (ind != -1)
            {
                test->picture[r][ind] = '/';
                test->picture[r][ind+1] = '\\';

                if (r==test->R-1)
                {
                    possible = false;
                    break;
                }

                if (test->picture[r+1][ind] == '#' &&
                    test->picture[r+1][ind+1] == '#')
                {
                    test->picture[r+1][ind] = '\\';
                     test->picture[r+1][ind+1] = '/';
                }
                else
                {
                    possible = false;
                    break;
                }
            }
            //replace conseq two hashes with /\
           //test->picture[r].replace(QRegExp("*\#\#*"), "/\");
        }
    }

    //if picture is valid, res = picture
    foreach(QString s, test->picture)
        if ( s.indexOf('#') != -1)
            possible = false;

    if (possible)
    test->res = test->picture;
    else
        test->res.append("Impossible");


}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QFile file("in.txt");
    QFile outfile("out.txt");

    QTextStream in (&file);
    QTextStream out (&outfile);

    outfile.open(QIODevice::WriteOnly
             | QIODevice::Text);
    if (!file.open(QIODevice::ReadOnly
            | QIODevice::Text))
        out << "no in file";

    int tests = 0;
    in >> tests;

    for (int i=0; i< tests; i++)
    {
        Test *test = readTest(in);
        solve(test);
        out << "Case #" << i+1 << ": " << "\n" << test->res.join("\n") << "\n";
    }

   return 0;
}
