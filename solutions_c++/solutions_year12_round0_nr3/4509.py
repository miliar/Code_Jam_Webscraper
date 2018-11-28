#include <iostream>
#include <string>
#include <cmath>
#include <set>

#include <QDebug>
#include <QFile>
#include <QMap>
#include <QStringList>

using namespace std;

int main(int argc, char **argv) {
  unsigned long long nb_test = 0;
  QFile myFile(argv[1]);
  if (!myFile.open(QIODevice::ReadOnly)) // Open the file
    cout << "Error while opening " << argv[0] << endl;
  QString first_line = myFile.readLine();
  nb_test = first_line.toInt();
  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    QString line = myFile.readLine();
    QStringList nm_line = line.split(" ");
    unsigned int A = nm_line[0].toInt();
    unsigned int B = nm_line[1].toInt();
    unsigned int count = 0;
    //QSet<int> res_set;
    for (unsigned long long n = A; n < B; n++) {
      QString n_str = QString::number(n);
      QSet<int> res_set;
      //qDebug() << "";
      //qDebug() << n_str;
      //qDebug() << "";
      // for each possibility, construct a new string
      for (int ni = 1; ni < n_str.size(); ni++) {
        //std::set<int> res_set;
        QString n_str_2(n_str.size(), '\0');
        for (int nj = 0; nj < n_str.size(); nj++) {
          n_str_2[nj] = n_str[(nj + ni) % n_str.size()];
        }
        //qDebug() << n_str_2;
        int n2 = n_str_2.toInt();
        if (n2 <= B && n2 > n) {
          //qDebug() << "Found :" << n_str_2;
          //qDebug() << n2;
          //qDebug() << res_set.contains(n2);
          res_set.insert(n2);
          //count++;
        }
      }
      count += res_set.size();
    }
    //count = res_set.size();

    cout << "Case #" << test_i << ": " << count << endl;
  }

  return 0;
}

