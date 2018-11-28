#include <QtCore/QCoreApplication>
#include <iostream>
#include <QHash>
#include <QString>
#include <QStringList>
#include <QFile>
#include <QTextStream>
#include <QIODevice>
#define NL '\n'

using namespace std;
void init();
QHash<QChar,QChar> mapping_list;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    std::cout<< "Program started \n";

    QHash<QChar, QChar>::const_iterator itr;
    init();

    QFile file("c://out.txt");
    file.open(QIODevice::ReadOnly | QIODevice::Text);
    QTextStream in(&file);
    QString line = in.readAll();
    file.close();


    QString str = line;
    QString message;
    message = "";
    int i = 0;
    while(NULL != str[i])
    {
        std::cout << str[i].toAscii();
        for (itr = mapping_list.constBegin(); itr != mapping_list.constEnd(); ++itr)
        {
            if(str[i] == itr.key())
            {
                message += itr.value();
            }

        }
        i++;
    }
    std::cout<< "\n\n";

    std::cout<< "convert string\t " << message.toStdString();

    QFile outfile("c://output.txt");
    outfile.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream out(&outfile);
    out << message;
    outfile.close();
    std::cout<< "\nProgram End\n";
    return a.exec();
}

void init()
{
    mapping_list['a'] = 'y';
    mapping_list['b'] = 'h';
    mapping_list['c']  = 'e';
    mapping_list['d']  = 's';
    mapping_list['e']  = 'o';
    mapping_list['f']  = 'c';
    mapping_list['g']  = 'v';
    mapping_list['h']  = 'x';
    mapping_list['i']  = 'd';
    mapping_list['j']  = 'u';
    mapping_list['k']  = 'i';
    mapping_list['l']  = 'g';
    mapping_list['m']  = 'l';
    mapping_list['n']  = 'b';
    mapping_list['o']  = 'k';
    mapping_list['p']  = 'r';
    mapping_list['q']  = 'z';
    mapping_list['r']  = 't';
    mapping_list['s']  = 'n';
    mapping_list['t']  = 'w';
    mapping_list['u']  = 'j';
    mapping_list['v']  = 'p';
    mapping_list['w']  = 'f';
    mapping_list['x']  = 'm';
    mapping_list['y']  = 'a';
    mapping_list['z']  = 'q';
    mapping_list[' ']  = ' ';
    mapping_list['A'] = 'Y';
    mapping_list['B'] = 'H';
    mapping_list['C']  = 'E';
    mapping_list['D']  = 'S';
    mapping_list['E']  = 'O';
    mapping_list['F']  = 'C';
    mapping_list['G']  = 'V';
    mapping_list['H']  = 'X';
    mapping_list['I']  = 'D';
    mapping_list['J']  = 'U';
    mapping_list['K']  = 'I';
    mapping_list['L']  = 'G';
    mapping_list['M']  = 'L';
    mapping_list['N']  = 'B';
    mapping_list['O']  = 'K';
    mapping_list['P']  = 'R';
    mapping_list['Q']  = 'Z';
    mapping_list['R']  = 'T';
    mapping_list['S']  = 'N';
    mapping_list['T']  = 'W';
    mapping_list['U']  = 'J';
    mapping_list['V']  = 'P';
    mapping_list['W']  = 'F';
    mapping_list['X']  = 'M';
    mapping_list['Y']  = 'A';
    mapping_list['Z']  = 'Q';
    mapping_list[NL]  = NL;

}
