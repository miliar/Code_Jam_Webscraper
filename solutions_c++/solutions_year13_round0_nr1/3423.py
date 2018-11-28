#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{

    ofstream output_large ("out_large.txt");
    ifstream given_input("A-small-attempt0.in");

    int T;
    const int tic_tac_dim = 4;
    int tic_tac[tic_tac_dim][tic_tac_dim] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
    char temp_player;
    int sum_check=0;
    bool exist_incomplete = false;
    bool enter_columns = false;
    bool enter_diagonals = false;
    bool enter_sec_diagonal = false;
    bool still_not_found_winner = false;
    given_input >> T;

    for(int tc_count=1; tc_count<= T; tc_count++){
       exist_incomplete = false;
       enter_columns = false;
       enter_diagonals = false;
       enter_sec_diagonal = false;
       still_not_found_winner = false;
        for(int i=0; i< tic_tac_dim; i++ ){
            for(int j=0; j< tic_tac_dim; j++){
                given_input >> temp_player;
                switch (temp_player){
                case 'X':
                {
                    tic_tac[i][j] = 30;

                    break;
                }

                case 'O':
                {
                    tic_tac[i][j] = 0;
                    break;
                }

                case 'T':
                {
                    tic_tac[i][j] = 5;
                    break;
                }

                case '.':
                {
                    tic_tac[i][j] = 200;
                    break;
                }


               default:
                {
                    break;
                }
             }

        }
        }

        //Analysis
        for(int i=0; i< tic_tac_dim; i++ ){ // row_check
             sum_check = 0;
                 for(int j=0; j< tic_tac_dim; j++){
                cout << i << " " << j << "   "<< tic_tac[i][j]<<endl;
                sum_check += tic_tac[i][j]; //row summation
            }
            cout << "------------->" << sum_check <<endl;
                if(sum_check ==120 || sum_check ==95 ){
                    //X won
                   enter_columns = false;
                   still_not_found_winner = false;
                   output_large << "Case #"<< tc_count <<": "<< "X won"<< endl;
                   cout << sum_check << endl << tc_count;
                   break;
                }
                else if(sum_check ==5 || sum_check ==0){
                        //O won
                     enter_columns = false;
                     still_not_found_winner = false;
                     output_large << "Case #"<< tc_count <<": "<< "O won"<< endl;
                     cout << "row_choice" << endl;
                     break;
                }
                else if(sum_check >= 200){
                    exist_incomplete = true;
                }
                else{
                    //draw
                }
        still_not_found_winner = true;
        enter_columns= true;

        }
            //column_check
                if(enter_columns){
                 for(int i=0; i< tic_tac_dim; i++ ){
                    sum_check =0;
                  for(int j=0; j< tic_tac_dim; j++){
                    cout << j << " " << i << "   "<< tic_tac[j][i]<<endl;
                    sum_check += tic_tac[j][i]; //row summation
                   }
                 cout << "------------->" << sum_check << endl;
                    if(sum_check ==120 || sum_check ==95 ){
                        //X won
                       enter_diagonals = false;
                       still_not_found_winner = false;
                       output_large << "Case #"<< tc_count <<": "<< "X won"<< endl;

                       break;
                    }
                    else if(sum_check ==5 || sum_check ==0){
                            //O won
                         enter_diagonals = false;
                         still_not_found_winner = false;
                         output_large << "Case #"<< tc_count <<": "<< "O won"<< endl;
                         cout << "col_choice" << endl;
                         break;
                    }
                    else if(sum_check >= 200){
                        exist_incomplete = true;
                    }
                    else{
                        //draw
                    }


                    cout<< "--------------------------------> I got here \n";
still_not_found_winner = true;
enter_diagonals= true;
             }

      }

//Diagonal_1 check
        if(enter_diagonals){
             enter_sec_diagonal= true;
                sum_check =0;
            for(int i=0; i< tic_tac_dim; i++ ){

                for(int j=0; j< tic_tac_dim; j++){

                    if(i==j){
                        cout << i << " " << j << "   "<< tic_tac[i][j]<<endl;
                        sum_check += tic_tac[i][j];
                    }
                }
            }
               cout << "------------->" << sum_check << endl;
                    if(sum_check ==120 || sum_check ==95 ){
                        //X won
                       enter_sec_diagonal = false;
                       still_not_found_winner = false;
                       output_large << "Case #"<< tc_count <<": "<< "X won"<< endl;
                      // break;
                    }
                    else if(sum_check ==5 || sum_check ==0){
                            //O won
                         enter_sec_diagonal = false;
                         still_not_found_winner = false;
                         output_large << "Case #"<< tc_count <<": "<< "O won"<< endl;
                         cout << "diag1_choice" << endl;
                     //    break;
                    }
                    else if(sum_check >= 200){
                        exist_incomplete = true;
                    }
                    else{
                        //draw
                    }


}

//Diagonal_2 check
        if(enter_sec_diagonal){
            sum_check =0;
            still_not_found_winner = true;
            for(int i=0; i< tic_tac_dim; i++ ){

                for(int j=0; j< tic_tac_dim; j++){

                    if((i+j+1) == tic_tac_dim){
                        cout << i << " " << j << "   "<< tic_tac[i][j]<<endl;
                        sum_check += tic_tac[i][j];
                    }
            }
            }
             cout << "------------->" << sum_check << endl;
                    if(sum_check ==120 || sum_check ==95 ){
                        //X won
                       still_not_found_winner = false;
                       output_large << "Case #"<< tc_count <<": "<< "X won"<< endl;
                      // break;
                    }

                    else if(sum_check ==5 || sum_check ==0){
                            //O won
                         still_not_found_winner = false;
                         output_large << "Case #"<< tc_count <<": "<< "O won"<< endl;
                         cout << "diag2_choice" << endl;
                        // break;
                    }

                    else if(sum_check >= 200){
                        exist_incomplete = true;
                    }

                    else{
                        //draw
                    }



        }



        if(exist_incomplete && still_not_found_winner){
            output_large << "Case #"<< tc_count <<": "<< "Game has not completed"<< endl;
            continue;
        }
        else if(still_not_found_winner){
             output_large << "Case #"<< tc_count <<": "<< "Draw"<< endl;
            continue;
        }
        else{
            continue;
        }
 }
    output_large.close();
    given_input.close();
    return 0;
}

