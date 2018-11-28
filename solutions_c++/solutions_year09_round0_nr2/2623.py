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
const int AM=10000+1;  //alt 高度的上限
int Map[H_max][W_max], Time[H_max][W_max], Sink[M][2+1], np;
// 陣列 Map 記錄地形, 陣列 Time 記錄排水時間, 陣列 Sink 記錄幫浦座標
// n 記錄地形邊長, m 記錄最大幫浦數, np 記錄實際幫浦數
//用排水時間的陣列代表會流向那個sink!(反之，sink 將反向找出流入的點。並
//   並編上同樣的 英文字母。
// Sink[M][2+1]，多加一個，是放入正確順序的英文字代號

struct Node { int x, y, d; };  //d 放代表的英文字母
deque<Node> Q;  //BFS 用佇列

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
    //for (i=0; i<N; i++) // 處理左、上邊界
    //    Map[0][i]=0, Map[i][0]=0;

    fin >> t;
    int testCase=t;
    while (t--)  {
        fout << "Case #" << (testCase-t) << ":" << endl;
        fin >> h >> w;
        //for (i=1, j=n+1; i<=j; i++) // 處理右、下邊界
        //    Map[j][i]=0, Map[i][j]=0;
        for (i=0; i<=h+1; i++) // 輸入地形  -->先全部歸 -1 (AM: alt MAXU)
            for (j=0; j<=w+1; j++)
                 Map[i][j]=AM ;


        for (i=1; i<=h; i++) // 輸入地形
            for (j=1; j<=w; j++)
                fin >> Map[i][j];


        for (i=1, np=0; i<=h; i++) // 計算幫浦數
            for (j=1; j<=w; j++) {
                int alt=Map[i][j];  //alt 代表高度
                //四週有任一個小於我，就不是sink
                if ( ( Map[i-1][j]<alt && Map[i-1][j]<AM ) ||
                     ( Map[i][j-1]<alt && Map[i][j-1]<AM ) ||
                     ( Map[i+1][j]<alt && Map[i+1][j]<AM ) ||
                     ( Map[i][j+1]<alt && Map[i][j+1]<AM ) ) continue;
                Sink[np][0]=i, Sink[np][1]=j;  //(y,x)或(H,W)
                np++;
            }
            if ( np>M  ) { // 幫浦數超過上限
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
        //現在已找到所有的 sink 的座標。
        //for (int i=0 ; i<np; i++) {
        //    cout << "no" << i << ":" << Sink[i][0] << "," <<Sink[i][1]<< endl;
        //}
        //int ixdf=0;
        //fout << " ok !!!!!!1 " << endl;


        for (i=0; i<=h+1; i++) //排水來源，先歸為 -1,反向看那個sink
            for (j=0; j<=w+1; j++)
                Time[i][j]=-1;

        Q.clear(); //將所有幫浦位置放入佇列

        for (i=0, a.d=0; i<np; i++)   {
            a.x=Sink[i][1];
            a.y=Sink[i][0];
            a.d='a'+i;
            Time[a.y][a.x]='a'+i;  //第一個a,第二個b,...依此。
            Q.push_back(a);
        }
        while ( Q.empty()==0 ) { // BFS
            //先儘量跑DFS，若在交界處，有兩種以上的sink再於那點，
             //   依該點的判斷，看那裡的高度較小？若一樣，再依方向N,E,S,W
            a=Q.front();
            Q.pop_front();
            x=a.x, y=a.y, d=a.d;
            int alt=Map[y][x];
            if ( Map[y-1][x]>alt ) { // && Time[y-1][x]>d )  {
                ///確定這個高點是往那個sink流？
                if (Time[y-1][x]> -1) { //若已填過。則要看是否有更好？
                    //如果我是他四週的最小值，而且是最優先的方向 NWES.
                    //先找出他的週邊四個的最小值。
                    int yy=y-1; int xx=x;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];  //我的方向
                    int altmin=minFun(altN,altW,altE,altS); //周圍最低值。
                    //四方向選一向。看誰與altmin相等。
                    if (altmin==alt){//如果我的高度是最小值，則有「很大可能」要覆蓋他！
                        //如果在比這方向優先的方向, 都不是altmin相等，則我才真正的覆蓋！
                        if (altN>altmin && altW>altmin && altE>altmin){
                            Time[yy][xx]=d;  //先不管那個sink.可以由該點看四週再確認。
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //不要覆蓋他。 }

                }else {
                    Time[y-1][x]=d;  //先不管那個sink.可以由該點看四週再確認。
                    a.y=y-1; a.x=x;  a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y][x-1]>alt  ) { //&& Time[y][x-1]>d )  {
                if (Time[y][x-1]> -1) {
                    //先找出他的週邊四個的最小值。
                    int yy=y; int xx=x-1;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1]; //我
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //周圍最低值。
                    //四方向選一向。看誰與altmin相等。
                    if (altmin==alt){//如果我的高度是最小值，則有「很大可能」要覆蓋他！
                        //如果在比這方向優先的方向, 都不是altmin相等，則我才真正的覆蓋！
                        if (altN>altmin && altW>altmin){
                            Time[yy][xx]=d;  //先不管那個sink.可以由該點看四週再確認。
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //不要覆蓋他。 }
                }else {
                    Time[y][x-1]=d;
                    a.y=y;  a.x=x-1;  a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y+1][x]>alt ) { // && Time[y+1][x]>d ) {
                if (Time[y+1][x] > -1 ) {
                    //先找出他的週邊四個的最小值。
                    int yy=y+1; int xx=x;
                    int altN=Map[yy-1][xx]; //我
                    int altW=Map[yy][xx-1];
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //周圍最低值。
                    //四方向選一向。看誰與altmin相等。
                    if (altmin==alt){//如果我的高度是最小值，則有「很大可能」要覆蓋他！
                        Time[yy][xx]=d;  //先不管那個sink.可以由該點看四週再確認。
                        a.y=yy; a.x=xx;  a.d=d;
                        Q.push_back(a);
                    } //else { //不要覆蓋他。 }
                }else {
                    Time[y+1][x]=d;
                    a.y=y+1;  a.x=x; a.d=d;
                    Q.push_back(a);
                }
            }
            if ( Map[y][x+1]>alt ) {// && Time[y][x+1]>d ){
                if (Time[y][x+1] > -1 ) {
                    //先找出他的週邊四個的最小值。
                    int yy=y; int xx=x+1;
                    int altN=Map[yy-1][xx];
                    int altW=Map[yy][xx-1]; //我
                    int altE=Map[yy][xx+1];
                    int altS=Map[yy+1][xx];
                    int altmin=minFun(altN,altW,altE,altS); //周圍最低值。
                    //四方向選一向。看誰與altmin相等。
                    if (altmin==alt){//如果我的高度是最小值，則有「很大可能」要覆蓋他！
                        //如果在比這方向優先的方向, 都不是altmin相等，則我才真正的覆蓋！
                        if (altN>altmin){
                            Time[yy][xx]=d;  //先不管那個sink.可以由該點看四週再確認。
                            a.y=yy; a.x=xx;  a.d=d;
                            Q.push_back(a);
                        }
                    } //else { //不要覆蓋他。 }
                } else {
                    Time[y][x+1]=d;
                    a.y=y;  a.x=x+1; a.d=d;
                    Q.push_back(a);
                }
            }
        }
        //按左上到右下水平優先的方式，把區塊的代號調為正確的。

        ///轉換為正確順序的代號！
        for (int ii=0;ii<np;ii++){
            Sink[ii][2]=-1;
        }; //Sink(y,x, 正確代號)

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
    // ●暴力法，找出全部的sink, 再用BFS配合題意找出正確的區塊
    // 先設法分出區塊後，
    //    進一步，把區塊的交界，調為最正確。
    // 而英文字母的問題。最後再 掃瞄一次，讓左上開始的英文字為a，
    //     依次向右為 b, 找好後，
    //  終於可以印出正確的陣列。
    //system("PAUSE");
    return 0;
}

