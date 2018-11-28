#include <iostream>
#include <string>
#include <cmath>

#include <QDebug>
#include <QFile>
#include <QMap>
#include <QStringList>

using namespace std;

inline QString otherRobot(const QString& robot) {
  if (robot == "O") return "B";
  else /*if (robot == "B")*/ return "O";
}

inline int min(int a, int b) {
  return a < b ? a : b;
}

int main(int argc, char **argv) {
  unsigned long long nb_test = 0;
  QFile myFile(argv[1]);
  if (!myFile.open(QIODevice::ReadOnly)) // Open the file
    cout << "Error whil opening " << argv[0] << endl;
  QString first_line = myFile.readLine();
  nb_test = first_line.toInt();

  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    int result = 0;
    QString line = myFile.readLine();
    QStringList splitted_line = line.split(" ");
    int splitted_line_pos = 0;

    // Init robot data structures
    QMap<QString, int> buffer_map;
    QMap<QString, int> pos_map;
    pos_map["O"] = 1;
    buffer_map["O"] = 0;
    pos_map["B"] = 1;
    buffer_map["B"] = 0;

    int nb_actions = splitted_line[splitted_line_pos++].toInt();
    qDebug() << "nb_action: " << nb_actions;
    QString previous_robot = "X";
    for (int action_i=0; action_i<nb_actions; action_i++) {
      QString robot = splitted_line[splitted_line_pos++];
      int next_pos = splitted_line[splitted_line_pos++].toInt();
      qDebug() << "robot: " << robot;
      qDebug() << "next_pos: " << next_pos;

      int time_to_go = abs(next_pos - pos_map[robot]); //TODO; time for pushing button
      qDebug() << "timeTogo: " << time_to_go;
      //qDebug() << buffer_map[otherRobot(robot)];
      //qDebug() << buffer_map[robot];
      int buffer_can_use = min(time_to_go, buffer_map[otherRobot(robot)]);
      qDebug() << "buffer can use: " << buffer_can_use;
      time_to_go -= buffer_can_use;
      buffer_map[otherRobot(robot)] = 0; // I can use buffer only once: reset it
      buffer_map[robot] += time_to_go + 1;
      //qDebug() << buffer_map[robot];
      //qDebug() << buffer_map["B"];
      //qDebug() << buffer_map["O"];
      result += time_to_go + 1; // time to push button
      pos_map[robot] = next_pos;
      previous_robot = robot;
    }

    cout << "Case #" << test_i << ": ";
    cout << result;
    cout << endl;
  }
  return 0;
}

