#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

#include <QFile>
#include <QStringList>
#include <QString>
#include <QTextStream>
#include <QMap>
#include <QDebug>

struct Node {
    public:
      QMap<QString, Node*> n;
  };


using namespace std;
int main(int argc, char** argv) {
  QFile file(argv[1]);
  file.open( QIODevice::ReadOnly );
  QTextStream stream( &file ); // Set the stream to read from myFile

  int nbTestCases;
  stream >> nbTestCases;


  Node* curNode;
  for (int i = 0; i<nbTestCases; ++i ) {
  //    cout << "****" << endl;
      Node* root = new Node;
      int res = 0;

      int n, m;
      stream >> n >> m;
      stream.readLine();
      for (int j=0;  j<n; ++j) {
        QString path = stream.readLine();
        QStringList elms = path.split("/", QString::SkipEmptyParts);
//        qDebug() << elms << "\n";
        curNode = root;
        for (int cptp = 0; cptp<elms.size(); cptp++ ){
            if (!curNode->n.contains( elms[cptp] ) ) {
              curNode->n[ elms[cptp] ] = new Node;
            }
            curNode = curNode->n[ elms[cptp] ];
        }
      }
      for (int j=0;  j<m; ++j) {
        QString path = stream.readLine();\
        QStringList elms = path.split("/", QString::SkipEmptyParts);
//                qDebug() << elms << "\n";

        curNode = root;
        for (int cptp = 0; cptp<elms.size(); cptp++ ){
            if (!curNode->n.contains( elms[cptp] ) ) {
              curNode->n[ elms[cptp] ] = new Node;
              res++;
            }
            curNode = curNode->n[ elms[cptp] ];
        }

      }
      cout << "Case #" << (i+1) << ": " << res << endl;
  }
}
