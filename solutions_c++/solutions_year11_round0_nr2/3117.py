#include <iostream>
#include <string>
#include <cmath>

#include <QDebug>
#include <QFile>
#include <QMap>
#include <QStringList>

using namespace std;

int main(int argc, char **argv) {
  unsigned long long nb_test = 0;
  //cin >> nb_test;
  QFile myFile(argv[1]);
  if (!myFile.open(QIODevice::ReadOnly)) // Open the file
    cout << "Error whil opening " << argv[0] << endl;
  QString first_line = myFile.readLine();
  nb_test = first_line.toInt();
  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    QString result;
    int C;
    int D;
    int N;
    //QMap<QString, QString> C_map;
    QMap<QString, QChar> C_map;
    QMap<QString, QString> D_map;

    QString line = myFile.readLine();
    QStringList splitted_line = line.split(" ");
    int splitted_line_pos = 0;

    // C (base)
    C = splitted_line[splitted_line_pos].toInt();
    splitted_line_pos++;
    qDebug() << "C: " << C << endl;
    for (int ci=0; ci<C; ci++) {
      QString C_pair = splitted_line[splitted_line_pos];
      qDebug() << C_pair;
      QString base = C_pair.left(2);
      qDebug() << base;
      QChar replacement = C_pair.right(1).data()[0];
      qDebug() << replacement;
      C_map[base] = replacement;
      // For in reverse order
      QString inverted_base;
      inverted_base.append(base.data()[1]);
      inverted_base.append(base.data()[0]);
      C_map[inverted_base] = replacement;
      splitted_line_pos++;
    }
    qDebug() << C_map;

    // D (clear list)
    D = splitted_line[splitted_line_pos++].toInt();
    for (int di=0; di<D; di++) {
      QString D_pair = splitted_line[splitted_line_pos];
      QString left = D_pair.left(1);
      QString right = D_pair.right(1);
      D_map[left] = right;
      D_map[right] = left;
      splitted_line_pos++;
    }
    qDebug() << D_map;

    N = splitted_line[splitted_line_pos++].toInt();
    QString string_problem = splitted_line[splitted_line_pos++];
    // check
    if (N != string_problem.size()-1) qDebug() << "ERROR: should be equal: " << string_problem.size()-1 << ", " << N;
    qDebug() << string_problem;
    QChar current_char = NULL, previous_char = NULL;
    QChar *data = string_problem.data();
    previous_char = data[0];
    current_char  = data[1];
    result += QString(previous_char);
    for (int i=1; i<string_problem.size()-1 /* don't care about \n */; i++) {
      QString current_pair;
      current_char = data[i];
      previous_char = result[result.size()-1];
      current_pair.append(current_char);
      current_pair.append(previous_char);
      if (C_map.contains(current_pair)) {
        qDebug() << "FOUND! C_map: " << C_map[current_pair];
        result[result.size()-1] = C_map[current_pair];
      } else {
        result += current_char;
      }
      qDebug() << "result: " << result;
      if (result.contains(D_map[result.data()[result.size()-1]])
        && D_map[result.data()[result.size()-1]] != "") {
        qDebug() << result.data()[result.size()-1];
        qDebug() << "ERASE, with D_map: " << D_map[result.data()[result.size()-1]];
        result = "";
      }
    }

    cout << "Case #" << test_i << ": [";
    for (int i=0; i<result.size(); i++) {
      if(i != 0) cout << ", ";
      cout << result[i].toAscii();
    }
    cout << "]" <<endl;
  }
  return 0;
}
