#include <QApplication>
#include "traite.h"

Traite                      *Traite::_singleton                     = NULL;

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Traite::getInstance();
    return a.exec();
}
