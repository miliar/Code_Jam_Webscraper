#include<iostream>
#include<fstream>
#include<queue>
//#define DEBUG
using namespace std;

int     TANKA = 1;



int main() {
    ofstream        output;
    ifstream        input( "C-small-attempt0.in" );
    output.open( "output.txt", std::ios::out );

    /**
     * 変数宣言
     */
    int         T;      /** テストの回数 */
    int         R;      /** 一日に運行できる回数 */
    int         K;      /** 乗り物の定員数 */
    int         N;      /** グループ数 */
    queue<int>  group;  /** 各グループのキュー */
    int         MONEY;  /** 当日の収入 */         
    int         temp;

    /**
     * テスト回数の読み込み
     */
    input >> T;
#ifdef DEBUG
    cout << "テスト回数：" << T << endl;
#endif

    /** テスト回数分だけループを行う */
    for( int t=1; t<T+1; t++ ) {
        MONEY = 0;
        // キューのクリア
        while( !group.empty() ) {
            group.pop();
        }

        /**
         * R, K, N, Giの各情報を読み込む
         */
        input >> R >> K >> N;   /** R,K,Nの読み込み */
        for( int j=0; j<N; j++ ) {
            input >> temp;
            group.push(temp);
#ifdef DEBUG
            cout << group.front() << ", ";
#endif
        }
#ifdef DEBUG
        cout << endl;
#endif


        /**
         * ここから問題を解き始めるフェーズ
         */
        for( int r=0; r<R; r++ ) {      /** 1日に運行する回数 */
            int g = 0;                  /** この運行で乗車する人数 */
            queue<int>  rider;          /** この運行で乗車する人のキュー */
            while( 1==1 ) {
                if( group.empty() ) {       // キューが空ならループを抜ける
                    break;
                } else if( g + group.front() > K ) {       // 次のグループを乗車させると定員オーバー
                    break;
                } else {
                    /** 次のグループは乗車可能 */
                    g += group.front();
                    rider.push( group.front() );    // 乗車キューに入れる
                    group.pop();
                }
            }

#ifdef DEBUG
            cout << "#####" << g << "人を乗せて出発\n";
#endif
            /** この時点で、乗車できるグループがriderキューに順に格納 */
            MONEY += g * TANKA;
#ifdef DEBUG
            cout << "***" << g << endl;
#endif

            // 次の運行のための準備
            while( !rider.empty() ) {
                group.push( rider.front() );
                rider.pop();
            }
        }
        cout << "Case #" << t << ": " << MONEY << endl;
    }





    output.close();
    input.close();
    return 0;
}
