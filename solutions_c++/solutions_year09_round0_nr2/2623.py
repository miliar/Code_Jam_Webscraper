//Design By Robert Jiang 2009.09.03
//googlecodeJam 2009
//Dev-C++
//
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())


////////////////////////////////////////////////////////////////////////////////

//googleCodeJam_Q_B.dev
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <deque>

using namespace std;

const int H_max=100,W_max=100, M=1001, MAX=H_max* W_max +1;
const int AM=10000+1;  //alt ���ת��W��
int Map[H_max][W_max], Time[H_max][W_max], Sink[M][2+1], np;
// �}�C Map �O���a��, �}�C Time �O���Ƥ��ɶ�, �}�C Sink �O�������y��
// n �O���a�����, m �O���̤j������, np �O�����������
//�αƤ��ɶ����}�C�N��|�y�V����sink!(�Ϥ��Asink �N�ϦV��X�y�J���I�C��
//   �ýs�W�P�˪� �^��r���C
// Sink[M][2+1]�A�h�[�@�ӡA�O��J���T���Ǫ��^��r�N��

struct Node { int x, y, d; };  //d ��N���^��r��
deque<Node> Q;  //BFS �Φ�C

int minFun(int a, int b, int c,int d){
    int min1=MIN(a,b);
    int min2=MIN(c,d);
    min1=MIN(min1,min2);
    return min1;
}

int main() {
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t, i, j, h, w,  x, y, d;
    Node a;
    //int N=H_max;  //100
    //for (i=0; i<N; i++) // �B�z���B�W���
    //    Map[0][i]=0, Map[i][0]=0;

    fin >> t;
    int testCase=t;
    while (t--)  {
        fout << "Case #" << (testCase-t) << ":" << endl;
        fin >> h >> w;
        //for (i=1, j=n+1; i<=j; i++) // �B�z�k�B�U���
        //    Map[j][i]=0, Map[i][j]=0;
        for (i=0; i<=h+1; i++) // ��J�a��  -->�������k -1 (AM: alt MAXU)
            for (j=0; j<=w+1; j++)
                 Map[i][j]=AM ;


        for (i=1; i<=h; i++) // ��J�a��
            for (j=1; j<=w; j++)
                fin >> Map[i][j];


        for (i=1, np=0; i<=h; i++) // �p��������
            for (j=1; j<=w; j++) {
                int alt=Map[i][j];  //alt �N����
                //�|�g�����@�Ӥp��ڡA�N���Osink
                if ( ( Map[i-1][j]<alt && Map[i-1][j]<AM ) ||
                     ( Map[i][j-1]<alt && Map[i][j-1]<AM ) ||
                     ( Map[i+1][j]<alt && Map[i+1][j]<AM ) ||
                     ( Map[i][j+1]<alt && Map[i][j+1]<AM ) ) continue;
                Sink[np][0]=i, Sink[np][1]=j;  //(y,x)��(H,W)
                np++;
            }
            if ( np>M  ) { // �����ƶW�L�W��
               fout << "Impossible" << endl;
            continue;
        }




        ////check!!!!!!!
        ///print test
        //for (int ii=0;ii<=h+1;ii++) {
        //   for (int jj=0;jj<=w+1;jj++) {
        //        cout << Map[ii][jj]<<",";
        //    }
        //    cout << endl;
        //}
        //�{�b�w���Ҧ��� sink ���y�СC
        //for (int i=0 ; i<np; i++) {
        //    cout << "no" << i << ":" << Sink[i][0] << "," <<Sink[i][1]<< endl;
        //}
        //int ixdf=0;
        //fout << " ok !!!!!!1 " << endl;


        for (i=0; i<=h+1; i++) //�Ƥ��ӷ��A���k�� -1,�ϦV�ݨ���sink
            for (j=0; j<=w+1; j++)
                Time[i][j]=-1;

        Q.clear(); //�N�Ҧ�������m��J��C

        for (i=0, a.d=0; i<np; i++)   {
            a.x=Sink[i][1];
            a.y=Sink[i][0];
            a.d='a'+i;
            Time[a.y][a.x]='a'+i;  //�Ĥ@��a,�ĤG��b,...�̦��C
            Q.push_back(a);
        }
        while ( Q.empty()==0 ) { // BFS
            //�����q�]DFS�A�Y�b��ɳB�A����إH�W��sink�A���I�A
             //   �̸��I���P�_�A�ݨ��̪����׸��p�H�Y�@�ˡA�A�̤�VN,E,S,W
            a=Q.front();
            Q.pop_front();
            x=a.x, y=a.y, d=a.d;
            int alt=Map[y][x];
            if ( Map[y-1][x]>alt ) { // && Time[y-1][x]>d )  {
                ///�T�w�o�Ӱ��I�O������sink�y�H
                if (Time[y-1][x]> -1) { //�Y�w��L�C�h�n�ݬO�_����n�H
                    //�p�G�ڬO�L�|�g���̤p�ȡA�ӥB�O���u������V NWES.
                    //����X�L���g��|�Ӫ��̤p�ȡC
                    int yy=y-1; int xx=x;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];  //�ڪ���V
                    int altmin=minFun(altN,altW,altE,altS); //�P��̧C�ȡC
                    //�|��V��@�V�C�ݽֻPaltmin�۵��C
                    if (altmin==alt){//�p�G�ڪ����׬O�̤p�ȡA�h���u�ܤj�i��v�n�л\�L�I
                        //�p�G�b��o��V�u������V, �����Oaltmin�۵��A�h�ڤ~�u�����л\�I
                        if (altN>altmin && altW>altmin && altE>altmin){
                            Time[yy][xx]=d;  //�����ި���sink.�i�H�Ѹ��I�ݥ|�g�A�T�{�C
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //���n�л\�L�C }

                }else {
                    Time[y-1][x]=d;  //�����ި���sink.�i�H�Ѹ��I�ݥ|�g�A�T�{�C
                    a.y=y-1; a.x=x;  a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y][x-1]>alt  ) { //&& Time[y][x-1]>d )  {
                if (Time[y][x-1]> -1) {
                    //����X�L���g��|�Ӫ��̤p�ȡC
                    int yy=y; int xx=x-1;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1]; //��
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //�P��̧C�ȡC
                    //�|��V��@�V�C�ݽֻPaltmin�۵��C
                    if (altmin==alt){//�p�G�ڪ����׬O�̤p�ȡA�h���u�ܤj�i��v�n�л\�L�I
                        //�p�G�b��o��V�u������V, �����Oaltmin�۵��A�h�ڤ~�u�����л\�I
                        if (altN>altmin && altW>altmin){
                            Time[yy][xx]=d;  //�����ި���sink.�i�H�Ѹ��I�ݥ|�g�A�T�{�C
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //���n�л\�L�C }
                }else {
                    Time[y][x-1]=d;
                    a.y=y;  a.x=x-1;  a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y+1][x]>alt ) { // && Time[y+1][x]>d ) {
                if (Time[y+1][x] > -1 ) {
                    //����X�L���g��|�Ӫ��̤p�ȡC
                    int yy=y+1; int xx=x;
                    int altN=Map[yy-1][xx]; //��
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //�P��̧C�ȡC
                    //�|��V��@�V�C�ݽֻPaltmin�۵��C
                    if (altmin==alt){//�p�G�ڪ����׬O�̤p�ȡA�h���u�ܤj�i��v�n�л\�L�I
                        Time[yy][xx]=d;  //�����ި���sink.�i�H�Ѹ��I�ݥ|�g�A�T�{�C
                        a.y=yy; a.x=xx;  a.d=d;
                        Q.push_back(a);
                    } //else { //���n�л\�L�C }
                }else {
                    Time[y+1][x]=d;
                    a.y=y+1;  a.x=x; a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y][x+1]>alt ) {// && Time[y][x+1]>d ){
                if (Time[y][x+1] > -1 ) {
                    //����X�L���g��|�Ӫ��̤p�ȡC
                    int yy=y; int xx=x+1;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1]; //��
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //�P��̧C�ȡC
                    //�|��V��@�V�C�ݽֻPaltmin�۵��C
                    if (altmin==alt){//�p�G�ڪ����׬O�̤p�ȡA�h���u�ܤj�i��v�n�л\�L�I
                        //�p�G�b��o��V�u������V, �����Oaltmin�۵��A�h�ڤ~�u�����л\�I
                        if (altN>altmin){
                            Time[yy][xx]=d;  //�����ި���sink.�i�H�Ѹ��I�ݥ|�g�A�T�{�C
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //���n�л\�L�C }
                } else {
                    Time[y][x+1]=d;
                    a.y=y;  a.x=x+1; a.d=d;
                    Q.push_back(a);
                }
            }
        }
        //�����W��k�U�����u�����覡�A��϶����N���լ����T���C

        ///�ഫ�����T���Ǫ��N���I
        for (int ii=0;ii<np;ii++){
            Sink[ii][2]=-1;
        }; //Sink(y,x, ���T�N��)

        int npCorrect=0;
        for (int ii=1;ii<=h;ii++) {
           for (int jj=1;jj<=w;jj++) {
                char ccc=Time[ii][jj];
                if (Sink[(ccc-'a')][2]==-1)
                    Sink[(ccc-'a')][2]=npCorrect++;
            }
        }

        //print Time Array
        for (int ii=1;ii<=h;ii++) {
           for (int jj=1;jj<=w;jj++) {
                char ccc=Time[ii][jj];
                //printf("%c",'a'+(Sink[(ccc-'a')][2])) ;
                char cccc='a'+(Sink[(ccc-'a')][2]);
                fout << cccc;   if (jj<w) fout << " ";
            }
            fout << endl;
        }


        //cout << "===========> " << endl;
        //for (int ii=0 ; ii< np ; ii++){
        //    cout << Sink[ii][2] << "," ;
        //}
        //cout << endl;

    }

    // Algorithm:
    // ���ɤO�k�A��X������sink, �A��BFS�t�X�D�N��X���T���϶�
    // ���]�k���X�϶���A
    //    �i�@�B�A��϶�����ɡA�լ��̥��T�C
    // �ӭ^��r�������D�C�̫�A ���ˤ@���A�����W�}�l���^��r��a�A
    //     �̦��V�k�� b, ��n��A
    //  �ש�i�H�L�X���T���}�C�C
    //system("PAUSE");
    return 0;
}

