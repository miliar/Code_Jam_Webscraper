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
  QFile myFile(argv[1]);
  if (!myFile.open(QIODevice::ReadOnly)) // Open the file
    cout << "Error while opening " << argv[0] << endl;
  QString first_line = myFile.readLine();
  nb_test = first_line.toInt();
  for (unsigned long long test_i=1; test_i<=nb_test; test_i++) {
    QString line_n = myFile.readLine();
    int N = line_n.toInt();
    //qDebug() << "N : " << N;
    // Init tabs:
    // Data tab
    int **tab = (int**)calloc(sizeof(int*),N);
    for (int i=0; i<N;i++) tab[i] = (int*)calloc(sizeof(int),N);
    // WP
    //int **WP_tab = (int**)calloc(sizeof(int*),N);
    float *WP_tab = (float*)calloc(sizeof(float),N);
    //for (int i=0; i<N;i++) WP_tab[i] = (int*)calloc(sizeof(int),N);
    // OWP
    //int **OWP_tab = (int**)calloc(sizeof(int*),N);
    float *OWP_tab = (float*)calloc(sizeof(float),N);
    //for (int i=0; i<N;i++) OWP_tab[i] = (int*)calloc(sizeof(int),N);
    // OOWP
    //int **OOWP_tab = (int**)calloc(sizeof(int*),N);
    float *OOWP_tab = (float*)calloc(sizeof(float),N);
    //for (int i=0; i<N;i++) OOWP_tab[i] = (int*)calloc(sizeof(int),N);
    int *count_tab = (int*)calloc(sizeof(int),N);
    int *sum_tab = (int*)calloc(sizeof(int),N);
    // RPI
    //int **RIP_tab = (int**)calloc(sizeof(int*),N);
    float *RIP_tab = (float*)calloc(sizeof(float),N);
    //for (int i=0; i<N;i++) RIP_tab[i] = (int*)calloc(sizeof(int),N);

    for (int ni=0; ni<N; ni++) {
      QString line = myFile.readLine();
      //qDebug() << line;
      QStringList splitted_line =line.remove("\n").remove("").split("");
      //qDebug() << splitted_line;
      int nj=0;
      foreach (const QString& match_point_str, splitted_line) {
        if(match_point_str != "") {
          //qDebug() << match_point_str;
          int match_point = -1;
          if (match_point_str != ".") {
            match_point = match_point_str.toInt();
          }
          tab[ni][nj] = match_point;
          nj++;
        }
      }
    }
    for (int ni=0; ni<N; ni++) {
      int sum = 0;
      int count = 0;
      for (int nj=0;nj<N;nj++) {
        if (tab[ni][nj] != -1) {
          sum += tab[ni][nj];
          count++;
        }
      }
      WP_tab[ni] = float(sum)/float(count);
      count_tab[ni] = count;
      sum_tab[ni] = sum;
      //qDebug() << "WP " << ni << " : " << WP_tab[ni];
    }
    for (int ni=0; ni<N; ni++) {
      float sum = 0;
      int count = 0;
      for (int nj=0;nj<N;nj++) {
        if (tab[ni][nj] != -1) {
          //sum += tab[ni][nj];
          ////qDebug() << "colutn  " <<count_tab[nj];
          ////qDebug() << "*colutn " <<sum_tab[nj];
          ////qDebug() << " tab i j " << tab[nj][ni];
          ////qDebug() << " tab2    " << sum_tab[nj];
          //sum += (WP_tab[nj]*count_tab[nj] - tab[ni][nj])/(count_tab[nj]-1);
          //cout << "DEBUG: " << float(sum_tab[nj] -tab[nj][ni])/float(count_tab[nj]-1) << endl;
          sum += float(sum_tab[nj] -tab[nj][ni])/float(count_tab[nj]-1);
          ////qDebug() << "sum: " << sum;
          count++;
        }
      }
      OWP_tab[ni] = float(sum)/float(count);
      //qDebug() << "WO " << ni << " : " << OWP_tab[ni];
    }
    for (int ni=0; ni<N; ni++) {
      float sum = 0;
      int count = 0;
      for (int nj=0;nj<N;nj++) {
        if (tab[ni][nj] != -1) {
          sum += OWP_tab[nj];
          count++;
        }
      }
      OOWP_tab[ni] = sum/count;
      //qDebug() << "OOWP: " << OOWP_tab[ni];
    }
    cout << "Case #" << test_i << ": " << endl;
    for (int ni=0; ni<N; ni++) {
      //qDebug() << .25*WP_tab[ni];
      //qDebug() << .5*OWP_tab[ni];
      //qDebug() << .25*OOWP_tab[ni];
      float RPI = .25*WP_tab[ni]+.5*OWP_tab[ni]+.25*OOWP_tab[ni];
      RIP_tab[ni] = RPI;
      //cout.precision(12);
      //cout.setf(ios::fixed,ios::floatfield);
      cout << RPI << endl;
    }
    // for DEBUG
    /*for (int ni=0;ni<N;ni++) {
      for (int nj=0;nj<N;nj++) {
        cout << tab[ni][nj];
      }
      cout << endl;
    }*/
  }

  return 0;
}

