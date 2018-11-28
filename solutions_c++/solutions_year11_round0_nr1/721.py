#include <iostream>

using namespace std;

int main(){
  int p_o=1,p_b=1;
  char robot;
  int t, prob_num, step_num, button, i,j, time=0, old_t_o=0, old_t_b=0;
  //old_t_はボタンを押した時間
  //  int o_order[10], b_order[10],o_index=0,b_index=0;
  cin >> prob_num;
  for(j=0; j<prob_num ; j++){
    cin >> step_num;
    time =0;p_o=1;p_b=1;old_t_o=0;old_t_b=0;
    //cout << "step:" << step_num <<endl;
    for(i =0; i < step_num; i++){
      cin >> robot >> button;
      if(robot=='O'){
	t = time-old_t_o;//時間経過
	if((p_o + t > button) &&( p_o - t < button)){//向こうが移動している間に次のに着く
	  //push button
	  time++;
	}else{//向こうが移動している間にはつかない
	  if(button-p_o > 0){
	    time += button-p_o-t+1;
	  }else{
	    time += -button+p_o-t+1;
	  }
	}
	old_t_o=time;
	p_o=button;
	//cout << time <<"  O:" << button <<endl;
      }else{
	t = time -old_t_b;
	if((p_b + t > button) && (p_b - t < button)){
          //push button
	  time++;
        }else{
          if(button-p_b > 0){
            time += button-p_b-t+1;
          }else{
            time += -button+p_b-t+1;
          }
        }
	old_t_b=time;
	p_b=button;
	//cout << time << "  B:" << button << endl;
      }

    }
    cout <<endl<< "Case #" << j+1 << ": " << time;
  }
  cout << endl;
  return 0;
}

